from langchain_google_genai import ChatGoogleGenerativeAI
from prompt_template import template
from config import GOOGLE_API_KEY
from langchain_core.messages import SystemMessage, HumanMessage



def main(text):
    # Initialize the chat model
    chat_model = ChatGoogleGenerativeAI(
        model="gemini-2.5-pro",
        google_api_key=GOOGLE_API_KEY
    )

    # # Example text to summarize
    # query = HumanMessage(content=text)
    
    # messages = [
    #     SystemMessage(template.format(text=query)),
    #     query
    # ]

    prompt = template.format(text=text)
    # Get the response from the model
    
    response = chat_model.invoke(prompt)
    
    # Print the response
    print(response.content)

if __name__ == "__main__":
    text = "Artificial intelligence is transforming various industries by automating tasks, enhancing decision-making, and improving customer experiences. It leverages machine learning algorithms to analyze large datasets, identify patterns, and make predictions. As AI continues to evolve, it is expected to create new job opportunities while also raising ethical considerations regarding privacy and bias."
    main(text)