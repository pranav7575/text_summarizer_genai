# Text Summarizer GenAI

A Python application that uses Google's Generative AI (Gemini) to create concise bullet-point summaries of large text documents. This tool leverages LangChain to streamline interactions with the Google Generative AI API.

## 📋 Table of Contents

- [Features](#features)
- [Project Structure](#project-structure)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Configuration](#configuration)
- [Usage](#usage)
- [How It Works](#how-it-works)
- [Dependencies](#dependencies)
- [License](#license)

## ✨ Features

- **AI-Powered Text Summarization**: Uses Google's Gemini Pro model to generate intelligent summaries
- **Bullet-Point Format**: Automatically formats summaries into 3-6 concise bullet points
- **Easy to Use**: Simple Python interface for quick summarization tasks
- **LangChain Integration**: Built with LangChain for seamless AI interactions
- **Environment Variable Management**: Secure API key handling with `.env` files

## 📁 Project Structure

```
text_summarizer_genai/
├── main.py                 # Main application entry point
├── prompt_template.py      # AI prompt template for summarization
├── config.py              # Configuration and environment variable management
├── .env                   # Environment variables (not committed to git)
├── .env.example           # Example environment variables template
├── .gitignore             # Git ignore rules
└── README.md              # This file
```

## 📦 Prerequisites

- Python 3.8 or higher
- Google API Key (from Google Cloud Console)
- pip (Python package manager)

## 🚀 Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/pranav7575/text_summarizer_genai.git
   cd text_summarizer_genai
   ```

2. **Create a virtual environment** (recommended):
   ```bash
   python -m venv venv
   
   # On Windows
   .\venv\Scripts\activate
   
   # On macOS/Linux
   source venv/bin/activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```
   
   Or install packages manually:
   ```bash
   pip install langchain langchain-google-genai python-dotenv
   ```

## ⚙️ Configuration

1. **Get your Google API Key**:
   - Go to [Google Cloud Console](https://console.cloud.google.com/)
   - Create a new project
   - Enable the Generative Language API
   - Generate an API key
   - Save your API key securely

2. **Create a `.env` file**:
   - Copy `.env.example` to `.env`
   - Add your Google API key:
     ```
     GOOGLE_API_KEY="your-api-key-here"
     ```
   - **Important**: Never commit `.env` to version control

## 🎯 Usage

### Basic Usage

```python
from main import main

# Text to summarize
text = "Your long text here..."

# Run the summarizer
main(text)
```

### Example

```python
from main import main

sample_text = """
Artificial intelligence is transforming various industries by automating tasks, 
enhancing decision-making, and improving customer experiences. It leverages 
machine learning algorithms to analyze large datasets, identify patterns, and 
make predictions. As AI continues to evolve, it is expected to create new job 
opportunities while also raising ethical considerations regarding privacy and bias.
"""

main(sample_text)
```

### Running from Command Line

```bash
python main.py
```

## 🔧 How It Works

1. **Load Configuration**: The app loads your Google API key from the `.env` file via `config.py`
2. **Initialize Model**: Creates an instance of `ChatGoogleGenerativeAI` with the Gemini Pro model
3. **Format Prompt**: Uses a predefined prompt template from `prompt_template.py` to format your input text
4. **Generate Summary**: Sends the formatted prompt to the AI model
5. **Output Result**: Prints the bullet-point summary to the console

### Prompt Template

The application uses a structured prompt that instructs the AI to:
- Act as an experienced editor
- Extract 3-6 key bullet points
- Keep each point concise and clear
- Return only the formatted summary

## 📚 Dependencies

| Package | Version | Purpose |
|---------|---------|---------|
| `langchain` | Latest | LLM framework and tools |
| `langchain-google-genai` | Latest | Google Generative AI integration |
| `python-dotenv` | Latest | Environment variable management |
| `google-generativeai` | Latest | Google AI API client |

## 🔒 Security

- **API Key Protection**: API keys are stored in `.env` which is not committed to git
- **Environment Variables**: Uses `python-dotenv` for secure credential management
- **No Hardcoded Secrets**: All sensitive data is externalized

## 💡 Tips & Best Practices

1. Keep your `.env` file private and never share your API key
2. Use `.env.example` as a template for documentation
3. Test with small texts first to understand the output format
4. Monitor your Google API usage to avoid unexpected charges
5. Consider caching results for frequently summarized texts

## 🐛 Troubleshooting

### Issue: "GOOGLE_API_KEY is not set"
**Solution**: Make sure `.env` file exists and contains your API key

### Issue: "Invalid input type" error
**Solution**: Ensure you're passing a string to `main()` function

### Issue: API Rate Limit
**Solution**: Add delays between requests or upgrade your API plan

## 📝 License

This project is open source and available under the MIT License.

## 👤 Author

**Pranav** - [GitHub](https://github.com/pranav7575)

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📞 Support

For issues and questions, please open an issue on the [GitHub repository](https://github.com/pranav7575/text_summarizer_genai/issues)