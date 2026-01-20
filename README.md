# MediChat Pro

> A lightweight medical PDF chat assistant using embeddings and a local vectorstore.

## Technologies

- **Language:** Python 3.9+
- **Web UI:** Streamlit (optional) via `app/ui.py`
- **NLP / Embeddings:** `sentence-transformers`, `langchain`, `langchain-community`
- **Vector DB:** `faiss-cpu` (local index)
- **PDF handling:** `pypdf`, `fpdf`
- **Environment:** `python-dotenv` for config
- **Other:** `euriai`, `langchain-text-splitters`

Dependencies are listed in `requirements.txt`.

## Project Overview

MediChat Pro ingests PDF documents, splits and embeds text, stores embeddings in a FAISS vectorstore, and provides a conversational interface for querying the content.

Key components (in `app/`):

- `chat_utils.py`: Chat flow helpers and prompt handling.
- `vectorstore_utils.py`: Build and query the FAISS vectorstore.
- `pdf_utils.py`: PDF parsing and preprocessing helpers.
- `config.py`: Configuration and environment loading.
- `ui.py`: Streamlit-based UI (optional) to run an interactive chat.

Other files:

- `main.py`: Project entry point (example runner).
- `requirements.txt`: Python dependencies.
- `sample_data/`: Example PDFs and test data.

## How It Works

1. PDFs are loaded and text is extracted via `app/pdf_utils.py`.
2. Text is split into chunks and converted to embeddings using a sentence-transformer model.
3. Embeddings are stored in a FAISS index managed by `app/vectorstore_utils.py`.
4. Chat queries are answered by retrieving nearest neighbors from the vectorstore and composing a response via LangChain tools in `app/chat_utils.py`.

## Running Locally (Windows)

1. Create and activate a virtual environment:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

Or using cmd:

```cmd
python -m venv .venv
.\.venv\Scripts\activate
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Copy example PDFs into `sample_data/` (or point the app to your documents).

4. Run the app (command-line runner or Streamlit UI):

- To run the basic entrypoint:

```bash
python main.py
```

- To launch the Streamlit UI (if `app/ui.py` is implemented):

```bash
streamlit run app/ui.py
```

## Configuration

- Create a `.env` file (if needed) and set API keys or config values used by `app/config.py`.

## Notes

- This project uses a local FAISS index; for larger datasets consider a remote vectorstore.
- If you change embedding models or chunking settings, rebuild the vectorstore.

## Contributing

Contributions welcome — open an issue or submit a PR with improvements.

## License

Add a license file if you plan to publish this project.
