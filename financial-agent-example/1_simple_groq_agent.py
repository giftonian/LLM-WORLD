from phi.agent import Agent
from phi.model.groq import Groq
from dotenv import load_dotenv

# Load the environment variables from the .env file
load_dotenv()

agent = Agent(
    model = Groq(id="llama-3.3-70b-versatile")
)

print("Welcome to LLM exercise...using Groq Agent")

agent.print_response("Write 2 sentence advice for senior backend developers to learn Math for the Machine learning")