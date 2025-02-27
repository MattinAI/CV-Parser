import requests
import json
import os

# Get the directory where the script is located
script_dir = os.path.dirname(os.path.abspath(__file__))
output_path = os.path.join(script_dir, "profesional_profile.md")

url = "http://localhost:7860/api/v1/run/9c3bea74-9f3b-4623-bdd3-8d163f75a907?stream=false"

headers = {
    "Content-Type": "application/json"
}

data = {
    "output_type": "chat",
    "input_type": "text",
    "tweaks": {
  "ChatOutput-jIvSv": {},
  "Agent-qWFNL": {},
  "Agent-nSCJT": {},
  "Agent-Ft4dA": {},
  "File-EreAn": {
      "path": "/home/anoya/proyectos/CV-Parser/langflow/cv_parser_sequential_multiagent/SteeveRubenQATester.pdf"
  },
  "Prompt-RLaWJ": {},
  "TextInput-yBvJD": {
      "input_value": "Programming Languages, Soft Skills, Project Management, Certifications, Hobbies"
  },
  "ParseData-qovzV": {},
  "Prompt-s2vj2": {},
  "ParseData-6vBOo": {}
    }
}

response = requests.post(url, headers=headers, data=json.dumps(data))
print(response.json())
if response.status_code == 200:
    response_data = response.json()
    
    # Initialize variable to store combined messages
    combined_message = ""
    
    # Extract all messages from all outputs
    try:
        first_output = response_data['outputs'][0]['outputs'][0]
        if 'results' in first_output and 'message' in first_output['results']:
            message_text = first_output['results']['message']['text']

        with open(output_path, "w") as file:
            file.write(message_text)

        print("Successfully extracted and saved the first message to profesional_profile.md")
    except KeyError as e:
        print(f"Error extracting message: {e}")
        print("Response structure:", json.dumps(response_data, indent=2))
else:
    print(f"Error: Received status code {response.status_code}")
    print(response.text)
