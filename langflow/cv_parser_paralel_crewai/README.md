# CV Parser Paralel CrewAI

This project is designed to parse and analyze CVs using a multi-agent system. The system categorizes skills from a CV based on predefined categories and assigns proficiency levels to each skill. It also generates a summary highlighting the professional’s most relevant expertise.

## Overview

The main components of this project are:

1. **Skills Categorization Specialist**: Analyzes the CV to identify and categorize skills according to predefined categories, assigning levels of expertise (1-5) for each skill.
2. **CV Summarizer**: Generates an executive summary of the profile, highlighting the most relevant skills and experiences.

The idea is this case is to try to buil a paralel execution in CrewAi with two chat outputs. Then we use them to build a common .md with a general result (Summary + Skill Categorization).

## Prerequisites

- You need an active OpenAI API key to use this project.

## Usage

1. **Langflow Flow**: The flow for the multi-agent system is defined in the JSON file "CV Analysis CrewAI Paralel.json" This file contains the configuration and logic for the multi-agent system.

2. **Testing the Flow**: You can test the flow using the provided Python script: test.py

This script sends a request to the Langflow API to run the flow.

3. **Running the Parser**: Update the `file path` in the script with the path to your CV in PDF format and run the parser using:
```bash
python [test_flow.py]
```

## Customization

You can customize change the summary that is sent to the fine system.
