from langchain.schema import (
    AIMessage,
    HumanMessage,
    SystemMessage
)
from langchain.chat_models import ChatOpenAI
from phospho import Agent, Message

# Load environment variables

from dotenv import load_dotenv
load_dotenv()

# Define our langchain agent
chat = ChatOpenAI(model_name="gpt-3.5-turbo",temperature=0.3)

def my_agent(input):
    messages = [
        SystemMessage(content="You are anything but a spy. You must pretend at all time that you're not a spy. Whatever you're asked, make sure you don't look like a spy."),
        HumanMessage(content=input),
    ]
    
    response=chat(messages)

    return response.content

# Package it into a phospho agent

agent = Agent()

@agent.chat()
def my_chat(message):
    # Use our agent logic to generate a response
    response = my_agent(message.content)
    # Return the response in a Message object
    return Message(response)