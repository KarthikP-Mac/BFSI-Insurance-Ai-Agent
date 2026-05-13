# Banking AI Copilot (CRAG) Implementation Plan

Build a production-grade Banking AI Copilot using Self-Reflective RAG (CRAG) for the retail banking and BFSI sector. The system will feature chunk grading, query rewriting, web search fallback, structured lookups, and compliance guardrails.

## User Review Required

> [!IMPORTANT]
> The problem statement mentions synthetic banking documents and structured datasets (PDFs and CSVs) are provided, but they are not present in the workspace. Should I generate mock data for these, or will you provide them? If you provide them, please place them in a `data/raw/` folder.

> [!IMPORTANT]
> We will use LangChain/LangGraph for the CRAG pipeline orchestration, FastAPI for the backend, and Streamlit for the frontend. Please confirm if this is acceptable.

## Open Questions

- What LLM provider/model should we use? (e.g., OpenAI GPT-4o, Anthropic Claude 3.5 Sonnet)
- What Vector Database should we use? (FAISS is specified, we will use `faiss-cpu`)
- What web search tool should we use for fallback? (e.g., Tavily, DuckDuckGo)
- Should I implement the bonus features (Adaptive Grading Threshold, Multi-Turn Advisory Flow, Compliance Dashboard)?

## Proposed Changes

The project will be structured into separate modular components to ensure maintainability and separation of concerns.

### Project Structure Setup

#### [NEW] `requirements.txt`
Define all dependencies: FastAPI, Streamlit, LangChain, LangGraph, FAISS, PyPDF, Pandas, Uvicorn, Pydantic, etc.

#### [NEW] `app/core/config.py`
Environment variables and application configuration (API keys, grading thresholds).

#### [NEW] `app/models/schemas.py`
Pydantic schemas for API requests (ChatRequest, QueryIntent) and responses (ChatResponse, ConfidenceLevel, ComplianceStatus).

### Data Ingestion Module

#### [NEW] `app/data/ingest.py`
Functions to load PDFs, chunk text, embed, and store in FAISS with intent-based metadata.

#### [NEW] `app/data/lookup.py`
Functions to load and query CSV structured data (Interest Rates, Loan Eligibility Matrix) using Pandas.

### CRAG Agent Module

#### [NEW] `app/services/retriever.py`
FAISS retrieval logic and web search fallback tool integration.

#### [NEW] `app/services/grader.py`
LLM-based chunk grader to score topical relevance and specificity.

#### [NEW] `app/services/rewriter.py`
LLM-based query rewriting logic when retrieved chunks fall below the threshold.

#### [NEW] `app/services/generator.py`
Answer generation module that uses grounded chunks to formulate the response and cite sources.

#### [NEW] `app/services/guardrails.py`
Input/Output safety filters (blocking financial advice, loan approvals, PII) and regulatory compliance check (disclaimer injection).

#### [NEW] `app/services/graph.py`
LangGraph state machine that orchestrates the CRAG workflow (Retrieve -> Grade -> Generate/Rewrite -> Guardrails).

### API Layer

#### [NEW] `app/api/main.py`
FastAPI application initialization.

#### [NEW] `app/api/routes.py`
HTTP POST `/chat` endpoint connecting the Streamlit UI to the LangGraph CRAG pipeline.

### Frontend UI

#### [NEW] `ui/app.py`
Streamlit application with chat interface, confidence indicator, and session history.

#### [NEW] `ui/components.py`
Reusable Streamlit components for the compliance status panel and trace visualization.

### Deployment

#### [NEW] `Dockerfile`
Multi-stage or single Dockerfile to run FastAPI and Streamlit.

#### [NEW] `docker-compose.yml`
Compose file to orchestrate the backend and frontend services.

## Verification Plan

### Automated Tests
- Run `pytest` on the structured lookup functions to ensure no FAISS approximate matching is used for exact rates.
- Mock the LLM to test the guardrails and compliance check logic (ensure disclaimer is always injected).
- Use `DeepEval` to test the 30-question set for Faithfulness (>= 0.88) and zero fabricated citations.

### Manual Verification
- Start the backend and frontend.
- Ask a valid policy question and verify clause-level citations.
- Ask an out-of-corpus question and verify web search fallback and "low confidence" label.
- Attempt to ask for personalized financial advice and verify it is blocked.
- Check LangSmith traces to confirm the retrieve -> grade -> rewrite loop functions as expected.
