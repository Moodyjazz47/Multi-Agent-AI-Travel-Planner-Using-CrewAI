from crewai import Agent
from textwrap import dedent
from langchain_openai import ChatOpenAI
from crewai.tools import BaseTool
import json
import os
import requests
from dotenv import load_dotenv
import pathlib

# Ensure environment variables are loaded with explicit path
current_dir = pathlib.Path(__file__).parent.resolve()
root_dir = current_dir.parent
env_path = root_dir / '.env'

# Load from project root .env file - print for debugging
print(f"Looking for .env at: {env_path}")
load_dotenv(dotenv_path=env_path)

# Double check if keys are loaded
print(f"SERPER_API_KEY loaded: {'SERPER_API_KEY' in os.environ}")


class SearchInternetTool(BaseTool):
    name: str = "search_internet"
    description: str = "Searches the internet for a given query and returns relevant results."

    def _run(self, query: str) -> str:
        top_result_to_return = 4
        url = "https://google.serper.dev/search"
        payload = json.dumps({"q": query})

        # Get API key with proper error handling
        api_key = os.environ.get('SERPER_API_KEY')
        if not api_key:
            # Try to load again for the specific call
            load_dotenv(dotenv_path=env_path, override=True)
            api_key = os.environ.get('SERPER_API_KEY')
            if not api_key:
                return "Error: SERPER_API_KEY not found in environment variables. Please check your .env file."

        headers = {
            'X-API-KEY': api_key,
            'content-type': 'application/json'
        }

        try:
            response = requests.post(url, headers=headers, data=payload)
            response_json = response.json()

            if 'organic' not in response_json:
                return "No organic search results found. There might be an issue with your Serper API key or the query."

            results = response_json['organic']
            string = []
            for result in results[:top_result_to_return]:
                try:
                    string.append('\n'.join([
                        f"Title: {result['title']}",
                        f"Link: {result['link']}",
                        f"Snippet: {result['snippet']}",
                        "\n-----------------"
                    ]))
                except KeyError:
                    continue
            return '\n'.join(string)
        except Exception as e:
            return f"Error searching the internet: {str(e)}"


class CalculatorTool(BaseTool):
    name: str = "calculate"
    description: str = "Performs a mathematical calculation from a string expression."

    def _run(self, operation: str) -> str:
        try:
            return str(eval(operation))
        except Exception as e:
            return f"Error: {str(e)}"


class TravelAgents:
    def __init__(self):
        # Ensure environment variables are loaded for OpenAI as well
        api_key = os.environ.get('OPENAI_API_KEY')
        if not api_key:
            print("Warning: OPENAI_API_KEY not found in environment variables!")

        self.OpenAIGPT35 = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0.7)
        self.OpenAIGPT4 = ChatOpenAI(model_name="gpt-4", temperature=0.7)

        # Create tool instances
        self.search_tool = SearchInternetTool()
        self.calculator_tool = CalculatorTool()

    def expert_travel_agent(self):
        return Agent(
            role="Expert Travel Agent",
            backstory=dedent(
                """Expert in travel planning and logistics. I have decades of experience making travel itineraries."""),
            goal=dedent(
                """Create a 7-day travel itinerary with detailed per-day plans, including budget, packing suggestions, and safety tips."""),
            verbose=True,
            llm=self.OpenAIGPT4,
            tools=[self.search_tool, self.calculator_tool]
        )

    def city_selection_expert(self):
        return Agent(
            role="City Selection Expert",
            backstory=dedent("""Expert at analyzing travel data to pick ideal destinations"""),
            goal=dedent("""Select the best cities based on weather, season, prices, and traveler interests"""),
            verbose=True,
            llm=self.OpenAIGPT4,
            tools=[self.search_tool]
        )

    def local_tour_guide(self):
        return Agent(
            role="Local Tour Guide",
            backstory=dedent(
                """Knowledgeable local guide with extensive information about the city, its attractions and customs"""),
            goal=dedent("""Provide the BEST insights about the selected city"""),
            verbose=True,
            llm=self.OpenAIGPT4,
            tools=[self.search_tool]
        )