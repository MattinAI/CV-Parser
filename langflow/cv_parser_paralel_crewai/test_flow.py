import requests
import json
import os

# Get the directory where the script is located
script_dir = os.path.dirname(os.path.abspath(__file__))
output_path = os.path.join(script_dir, "profesional_profile.md")

url = "http://localhost:7860/api/v1/run/f0dd2978-803b-45ac-bab2-e7030d3c476f?stream=false"

headers = {
    "Content-Type": "application/json"
}

data = {
    "input_value": "message",
    "output_type": "chat",
    "input_type": "text",
    "tweaks": {
  "Prompt-H3pqt": {},
  "ParseData-3749s": {},
  "CrewAIAgentComponent-Ajx5Q": {},
  "SequentialTaskComponent-xLSW3": {},
  "ChatOutput-ft7gp": {},
  "SequentialCrewComponent-8pSHu": {},
  "OpenAIModel-zD3LX": {},
  "CrewAIAgentComponent-ESkgb": {},
  "SequentialTaskComponent-iCFaW": {},
  "Prompt-A3bbR": {},
  "SequentialCrewComponent-FbsM1": {},
  "ChatOutput-t8KHP": {},
  "File-vTzaK": {
      "path": "/home/anoya/proyectos/CV-Parser/langflow/cv_parser_paralel_crewai/SteeveRubenQATester.pdf"
    }
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
        # Iterate through all outputs
        for output_group in response_data['outputs']:
            for output in output_group['outputs']:
                if 'results' in output and 'message' in output['results']:
                    message_text = output['results']['message']['text']
                    # Add to combined message with a separator
                    if combined_message:
                        combined_message += "\n\n" + "=" * 50 + "\n\n"  
                    combined_message += message_text
        
        # Write the combined message to the file
        with open(output_path, "w") as file:
            file.write(combined_message)
        
        print(f"Successfully extracted and saved all messages to {output_path}")
    except KeyError as e:
        print(f"Error extracting message: {e}")
        print("Response structure:", json.dumps(response_data, indent=2))
else:
    print(f"Error: Received status code {response.status_code}")
    print(response.text)
