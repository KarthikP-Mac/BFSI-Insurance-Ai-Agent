import asyncio
import os
from backend.services.crag import run_crag_pipeline, grade_chunk, rewrite_query
from backend.services.guardrails import check_compliance_and_guardrails
from backend.services.llm_factory import get_llm
from backend.data.lookup import StructuredLookup

async def run_tests():
    print("Testing imports... OK")
    
    # We will only do partial testing if API keys are not set, otherwise we'll test actual models
    api_key = os.getenv("OPENAI_API_KEY") or os.getenv("ANTHROPIC_API_KEY")
    if not api_key:
        print("API keys not set. Skipping actual LLM calls.")
        return
        
    print("\n--- Testing Guardrails ---")
    bad_query = "What is the specific interest rate for a 50k home loan?"
    bad_answer = "You are approved for a home loan at exactly 8.5% interest."
    res = check_compliance_and_guardrails(bad_query, bad_answer)
    print("Guardrails flagged bad answer:", not res["is_compliant"])
    
    good_query = "What is a home loan?"
    good_answer = "A home loan is a loan taken to purchase a house."
    res = check_compliance_and_guardrails(good_query, good_answer)
    print("Guardrails passed good answer:", res["is_compliant"])
    print("Disclaimer injected:", res["disclaimer_injected"] if "disclaimer_injected" in res else ("This information is for guidance only" in res.get("final_answer", "")))
    
    print("\n--- Testing Structured Lookup ---")
    lookup = StructuredLookup()
    rate = lookup.lookup_interest_rate("Home Loan")
    print("Rate lookup output prefix:", rate[:40])
    
    print("\n--- Testing Full CRAG Pipeline ---")
    # This will trigger the web search fallback if vectorstore isn't populated or query is obscure
    res = await run_crag_pipeline("What are the latest NASA updates 2024?", "test_session_123")
    print("CRAG Fallback confidence level:", res["confidence_level"])
    
    print("\nAll tests ran successfully!")

if __name__ == "__main__":
    asyncio.run(run_tests())
