# import requests
# from app.config import OLLAMA_BASE_URL, LLM_MODEL

# # Mocked LLM to avoid HTTP 404 errors
# def llm_review(tone: str, text: str, score: float) -> str:
#     """
#     Mock LLM evaluation:
#     - Verdict: Pass if score > 0.5 else Fail
#     - Explanation + optional rewrite
#     """
#     verdict = "Pass" if score > 0.5 else "Fail"
#     explanation = f"Mocked LLM: Content scored {score:.2f} against tone '{tone}'"
#     rewrite = text if score > 0.5 else f"[Rewrite to match tone: {tone}] {text}"
    
#     return f"Verdict: {verdict}\nExplanation: {explanation}\nRewrite: {rewrite}"


import requests
from app.config import OLLAMA_BASE_URL, LLM_MODEL

PASS_THRESHOLD = 0.6   # this is your brand strictness

def llm_review(tone: str, text: str, score: float):
    """
    Uses Ollama to decide:
    - If tone matches -> explain why, do NOT rewrite
    - If not -> suggest improvements + rewrite
    """

    if score >= PASS_THRESHOLD:
        prompt = f"""
You are a brand tone evaluator.

Brand tone: {tone}
Text: "{text}"

The text already matches the brand tone.

Explain briefly WHY it matches the tone.
Do NOT rewrite it.
Return in this format:

Verdict: PASS
Explanation: ...
"""

    else:
        prompt = f"""
You are a brand copy editor.

Brand tone: {tone}
Text: "{text}"

The text does NOT match the brand tone.

1. Identify what tone elements are missing
2. Suggest words or phrases that should be added
3. Rewrite the content to match the tone

Return in this format:

Verdict: FAIL
Missing: ...
Suggestions: ...
Rewrite: ...
"""

    r = requests.post(
        f"{OLLAMA_BASE_URL}/api/generate",
        json={
            "model": LLM_MODEL,
            "prompt": prompt,
            "stream": False
        },
        timeout=60
    )

    r.raise_for_status()
    return r.json()["response"]
