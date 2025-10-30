from langchain_google_genai import ChatGoogleGenerativeAI
from prompt_template import summary_prompt
from config import GOOGLE_API_KEY

def main():
    # Initialize the chat model
    chat_model = ChatGoogleGenerativeAI(
        model="gemini-pro",
        google_api_key=GOOGLE_API_KEY
    )

    # Example text to summarize
    text = "Artificial intelligence is transforming various industries by automating tasks, enhancing decision-making, and improving customer experiences. It leverages machine learning algorithms to analyze large datasets, identify patterns, and make predictions. As AI continues to evolve, it is expected to create new job opportunities while also raising ethical considerations regarding privacy and bias."
    
    # Format the prompt with the text
    formatted_prompt = summary_prompt.format(text=text)
    
    # Get the response from the model
    response = chat_model.invoke(formatted_prompt)
    
    # Print the response
    print(response.content)

if __name__ == "__main__":
    main()