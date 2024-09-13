"""
Install the Google AI Python SDK

$ pip install google-generativeai
"""

import os
import google.generativeai as genai

genai.configure(api_key=os.environ["API_KEY"])

# Create the model
generation_config = {
  "temperature": 0.25,
  "top_p": 0.95,
  "top_k": 64,
  "max_output_tokens": 8192,
  "response_mime_type": "text/plain",
}

model = genai.GenerativeModel(
  model_name="gemini-1.5-pro-exp-0827",
  generation_config=generation_config,
  # safety_settings = Adjust safety settings
  # See https://ai.google.dev/gemini-api/docs/safety-settings
  system_instruction="categorize the following (Thai) message into these categories if it fits otherwise return \"out of scope\"\n\"\"\"\nPre and Post-Run Preparation\nBody Care, Injury Prevention and Recovery\nGear\nTechnique and Performance Improvement\nGoal Setting, Motivation, and Training Plans\nTime Management and Overtraining Prevention\n\"\"\"\n\n\n\nonly anwer the categories and make sure they lies in running context",
)

chat_session = model.start_chat(
  history=[
  ]
)

while True:
    message = input("Enter the message: ")
    
    if message.lower() == 'q':
        print("Exiting chat...")
        break
    
    response = chat_session.send_message(message)
    print(response.text)