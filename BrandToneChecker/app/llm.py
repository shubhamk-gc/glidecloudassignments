import requests
from app.config import OLLAMA_BASE_URL, LLM_MODEL

# Mocked LLM to avoid HTTP 404 errors
def llm_review(tone: str, text: str, score: float) -> str:
    """
    Mock LLM evaluation:
    - Verdict: Pass if score > 0.5 else Fail
    - Explanation + optional rewrite
    """
    verdict = "Pass" if score > 0.5 else "Fail"
    explanation = f"Mocked LLM: Content scored {score:.2f} against tone '{tone}'"
    rewrite = text if score > 0.5 else f"[Rewrite to match tone: {tone}] {text}"
    
    return f"Verdict: {verdict}\nExplanation: {explanation}\nRewrite: {rewrite}"
