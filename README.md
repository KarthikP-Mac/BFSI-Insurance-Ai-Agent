# Banking AI Copilot (CRAG)

A Banking AI Copilot utilizing the Corrective Retrieval Augmented Generation (CRAG) pattern for high-accuracy retail banking queries. Built with LangChain, FastAPI, and Streamlit.

## Features
- **Self-Reflective RAG (CRAG)**: Retrieves from FAISS, grades chunks for relevance, and rewrites queries if retrievals are sub-optimal (up to 2 iterations).
- **Web Search Fallback**: Automatically falls back to DuckDuckGo search for out-of-corpus queries, labelling the answer as "Low Confidence".
- **Structured Lookups**: Reads CSV files directly for Interest Rates and Loan Eligibility to avoid approximate matching hallucination.
- **Compliance Guardrails**: Uses LLM-based guardrails to block financial advice, loan approvals, and rate guarantees. Automatically injects regulatory disclaimers into every response.
- **Multi-LLM Support**: Supports both OpenAI and Anthropic through environment variables.
- **Trace Observability**: Full pipeline steps visible in the Streamlit UI.

## Setup Instructions

1. Clone the repository.
2. Ensure you have the raw datasets in `data/raw/` (PDFs and CSVs).
3. Copy `.env.example` to `.env` and fill in your API keys (OpenAI or Anthropic).

### Running Locally (Python)
1. Create a virtual environment: `python -m venv .venv`
2. Activate the environment: `.\.venv\Scripts\activate` (Windows) or `source .venv/bin/activate` (Mac/Linux)
3. Install dependencies: `pip install -r requirements.txt`
4. Run the data ingestion script to build the FAISS index:
   ```bash
   python backend/data/ingest.py
   ```
5. Start the backend API:
   ```bash
   uvicorn backend.api.main:app --reload --port 8000
   ```
6. Start the frontend UI in a new terminal:
   ```bash
   streamlit run ui/app.py
   ```

### Running via Docker
1. Ensure Docker Desktop is running.
2. Build and run the containers:
   ```bash
   docker-compose up --build
   ```
3. The API will be available at `http://localhost:8000` and the UI at `http://localhost:8501`.

## Project Structure
- `backend/`: FastAPI backend, LangChain CRAG orchestration, Guardrails, Data Ingestion
- `ui/`: Streamlit frontend application
- `data/`: Raw PDFs/CSVs and processed FAISS vectorstore
- `Dockerfile` / `docker-compose.yml`: Containerization
