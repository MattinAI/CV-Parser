# CV-Parser
This AI agent extracts and categorizes skills from a CV based on predefined knowledge categories, assigning a proficiency level from 1 to 5 for each skill. It also generates a summary highlighting the professional’s most relevant expertise. 

## Main Agents

1. **Skills Categorization Specialis**

- Analyze the CV to identify all skills
- Categorize skills according to predefined categories
- Assigns levels of expertise (1-5) for each skill
- Evaluates context and experience to determine levels

2. **CV Summarizer**

- Generates the executive summary of the profile
- Identifies and highlights the most relevant skills
- Synthesizes the most significant experiences
- Produces a cohesive analysis of the professional profile

## Usage

1. Update the `pdf_path` variable in `main.py` with the path to your CV in PDF format
2. Run the parser using:
```bash
crewai run