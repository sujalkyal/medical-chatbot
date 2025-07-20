# Medical Chatbot

A conversational AI web application designed to answer medical queries using a locally stored medical book and a powerful language model. The chatbot leverages document retrieval and large language models to provide accurate, context-aware responses.

## Features

- **Conversational Interface:** Chat with the bot via a simple web UI.
- **Document Retrieval:** Uses Pinecone vector store to search relevant medical information from a PDF book.
- **LLM Integration:** Powered by Llama-2 (via CTransformers) for generating human-like answers.
- **Custom Prompting:** Utilizes custom prompt templates for context-rich responses.
- **Extensible:** Modular codebase for easy experimentation and extension.

## Project Structure

```
medical-chatbot/
│
├── app.py                  # Main Flask web application
├── store_index.py          # Script to index medical book into Pinecone
├── requirements.txt        # Python dependencies
├── setup.py                # Package setup
├── README.md               # Project documentation
│
├── data/
│   └── Medical_book.pdf    # Source medical book
│
├── experiment/
│   └── experiment.ipynb    # Jupyter notebook for prototyping
│
├── src/
│   ├── __init__.py
│   ├── helper.py           # Utility functions (PDF loading, embedding, etc.)
│   └── prompt.py           # Custom prompt templates
│
├── static/
│   └── style.css           # Frontend styles
│
└── templates/
    └── index.html          # Web UI template
```

## How It Works

1. **Indexing:**  
   - Run `store_index.py` to process the medical book PDF, split it into chunks, and store embeddings in Pinecone.

2. **Web App:**  
   - `app.py` launches a Flask server.
   - User queries are embedded and matched against the indexed medical book.
   - The most relevant context is passed to the Llama-2 model for answer generation.

3. **Experimentation:**  
   - Use `experiment/experiment.ipynb` for testing and prototyping new features or models.

## Setup Instructions

1. **Clone the repository:**
   ```sh
   git clone https://github.com/sujalkyal/medical-chatbot.git
   cd medical-chatbot
   ```

2. **Install dependencies:**
   ```sh
   pip install -r requirements.txt
   ```

3. **Download Model & Data:**
   - Place the Llama-2 model file in the `model/` directory.
   - Place the medical book PDF in the `data/` directory.

4. **Index the medical book:**
   ```sh
   python store_index.py
   ```

5. **Run the web application:**
   ```sh
   python app.py
   ```
   - Access the chatbot at [http://localhost:5000](http://localhost:5000).

## Requirements

- Python 3.8+
- See `requirements.txt` for all Python packages.

## Customization

- **Model:** Change the model path or type in `app.py` for different LLMs.
- **Prompt:** Edit `src/prompt.py` to modify the prompt template.
- **Frontend:** Update `templates/index.html` and `static/style.css` for UI changes.

## License

This project is for educational and research purposes only. Please consult a medical professional for real medical advice.