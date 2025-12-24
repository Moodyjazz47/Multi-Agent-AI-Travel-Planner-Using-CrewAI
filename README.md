# 🧠 Multi-Agent AI Travel Planner


## ⚡ TL;DR

A multi-agent LLM-powered travel planner where specialized AI agents collaborate to select destinations, retrieve real-world travel data using tools, and generate personalized 7-day itineraries using agentic AI workflows.


## 📌 Overview

This project is a multi-agent AI travel planning system built using CrewAI and OpenAI GPT models, designed to autonomously plan personalized trips through collaborating LLM agents. Instead of relying on a single model, the system leverages specialized AI agents that reason independently, use external tools, and share context to produce grounded, end-to-end travel plans.

The application accepts user preferences such as origin, travel dates, candidate destinations, and interests, then automatically selects the optimal city, gathers real-world travel data, and generates a complete 7-day itinerary.


## 🧩 System Architecture

The system follows an agentic AI architecture, where each agent has a distinct role and responsibility:

City Selection Expert
Analyzes multiple destinations based on weather, seasonality, travel costs, and user interests to select the most suitable city.

Local Tour Guide
Gathers in-depth city knowledge including attractions, local customs, hidden gems, weather insights, and cost estimates.

Expert Travel Agent
Synthesizes all gathered information to generate a detailed, day-by-day travel itinerary including accommodation, dining options, budget breakdowns, packing suggestions, and safety tips.

Agents collaborate via a task-orchestrated workflow managed by CrewAI.


## 🛠️ Key Features

Multi-Agent LLM Collaboration using CrewAI

Tool-Augmented Reasoning with real-time web search and calculations

Autonomous Decision-Making based on user preferences

Grounded Outputs using live travel data (hotels, flights, attractions)

End-to-End Trip Planning from destination selection to daily itinerary


## 🧪 Technologies Used

Python

CrewAI – Multi-agent orchestration framework

OpenAI GPT Models – Reasoning and generation

Serper API – Real-time Google search integration

LangChain OpenAI – LLM interface

dotenv – Secure environment variable management


## 🚀 How It Works

User provides travel preferences (origin, destinations, dates, interests).

The City Selection Expert: evaluates and selects the best destination.

The Local Tour Guide: gathers detailed city-specific insights.

The Expert Travel Agent: generates a comprehensive 7-day itinerary.

The final travel plan is produced through agent collaboration and task sequencing.


## 🎯 Why This Project

This project demonstrates LLM systems engineering and agentic AI principles, including:

Role-based agent design

Task-driven orchestration

Tool-augmented LLM reasoning

Context sharing between autonomous agents


## 🧾 Demo Output (Sample)

### Input:

Origin: 
Bangalore, India

City Options: 
Paris, Rome, Amsterdam

Travel Dates: 
April 10 – April 17

Interests: 
History, food, museums, photography

### Output:

Selected City: Paris, France

Reason:
- Pleasant spring weather (12–18°C)
- Peak museum season with manageable crowds
- Strong alignment with historical and cultural interests

Day 1:
- Arrival at Charles de Gaulle Airport
- Hotel: Hôtel Le Six (Latin Quarter)
- Evening walk along the Seine and Notre-Dame
- Dinner at Le Procope

Day 2:
- Louvre Museum (morning)
- Lunch at Café Marly
- Eiffel Tower & Trocadéro (sunset photography)
- Estimated Daily Budget: €120–150

...
Day 7:
- Montmartre walking tour
- Shopping & departure
