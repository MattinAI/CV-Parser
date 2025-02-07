# import sys
import warnings
import pdfplumber

from datetime import datetime

from cv_analysis_crewai.crew import CvAnalysisCrewai

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

def run():
    """
    Run the crew.
    """
    pdf_path = '/home/anoya/proyectos/multiagent-platform/cv_analysis_crewai/tests/cv_examples/SteeveRubenQATester.pdf'
    with pdfplumber.open(pdf_path) as pdf:
        cv_text = ' '.join(page.extract_text() for page in pdf.pages)

    inputs = {
        'cv_text': cv_text,
        'categories': ["Programming Languages", "Frameworks & Libraries", "Database Technologies", "Cloud Platforms", "Soft Skills"]
    }
    
    try:
        CvAnalysisCrewai().crew().kickoff(inputs=inputs)
    except Exception as e:
        raise Exception(f"An error occurred while running the crew: {e}")

def train():
    """
    Train the crew for a given number of iterations.
    """
    inputs = {
        "topic": "AI LLMs"
    }
    try:
        CvAnalysisCrewai().crew().train(n_iterations=int(sys.argv[1]), filename=sys.argv[2], inputs=inputs)

    except Exception as e:
        raise Exception(f"An error occurred while training the crew: {e}")

def replay():
    """
    Replay the crew execution from a specific task.
    """
    try:
        CvAnalysisCrewai().crew().replay(task_id=sys.argv[1])

    except Exception as e:
        raise Exception(f"An error occurred while replaying the crew: {e}")

def test():
    """
    Test the crew execution and returns the results.
    """
    inputs = {
        "topic": "AI LLMs"
    }
    try:
        CvAnalysisCrewai().crew().test(n_iterations=int(sys.argv[1]), openai_model_name=sys.argv[2], inputs=inputs)

    except Exception as e:
        raise Exception(f"An error occurred while testing the crew: {e}")
