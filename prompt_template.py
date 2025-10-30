from langchain import PromptTemplate

template = """You are an experienced editor. When given an input text in the variable {text}, produce section:
Bulleted Summary:
- Provide 3-6 concise bullet points that capture the key ideas. Each bullet should be one short sentence or phrase.

Return the output exactly in this format.

Input:
{text}
"""

summary_prompt = PromptTemplate(input_variables=["text"], template=template)



