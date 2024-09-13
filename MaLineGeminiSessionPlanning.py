import google.generativeai as genai
import typing_extensions as typing
import os

genai.configure(api_key=os.environ["API_KEY"])

# Define the schema for Running Session using TypedDict
class RunningSession(typing.TypedDict):
    desired_session_type: str  # 'duration' or 'quantity'
    desired_date: str  # Date in 'YYYY-MM-DD' format
    last_session_type: str  # 'duration' or 'quantity'
    start_date: str  # Date in 'YYYY-MM-DD' format
    amount: float  # Amount of time or quantity
    zone: str  # E.g., 'moderate', 'intense'
    average_heart_rate: int
    max_heart_rate: int
    total_time: float  # Total time of the session in minutes

class WorkoutRecommendation(typing.TypedDict):
    amount: float
    pre_workout: str
    post_workout: str
    suggestion: str

# Initialize the Gemini model
model = genai.GenerativeModel("gemini-1.5-pro-latest")

# Prompt to generate a running session recommendation
prompt = """
Generate a JSON output that contains a running session recommendation.

The running session should have the following structure:
- desired_session_type: 'duration' or 'quantity'
- desired_date: 'YYYY-MM-DD'
- last_session_type: 'duration' or 'quantity'
- start_date: 'YYYY-MM-DD'
- amount: The amount of time or quantity based on the type of session
- zone: A string indicating the workout intensity zone
- average_heart_rate: The average heart rate of the last session
- max_heart_rate: The maximum heart rate during the last session
- total_time: The total time spent in the last session in minutes

Use this information to provide:
- a recommended 'amount' for the next session
- 'pre_workout' advice
- 'post_workout' advice
- a 'suggestion' based on performance in the last session

Return the response in JSON format.

Example schema:
{
  "desired_session_type": str,
  "desired_date": str,
  "last_session_type": str,
  "start_date": str,
  "amount": float,
  "zone": str,
  "average_heart_rate": int,
  "max_heart_rate": int,
  "total_time": float
}
"""

# Generate content with structured response schema
result = model.generate_content(
    prompt,
    generation_config=genai.GenerationConfig(
        response_mime_type="application/json",
        response_schema=RunningSession  # Ensure that the output conforms to the schema
    )
)

# Print the result
print(result)
