"""
ollama_client.py
Thin wrapper around the local Ollama API. Uses format="json" so the
model is constrained to valid JSON output — much more reliable than
asking nicely in the prompt and hoping.
"""

import json

import requests


def call_ollama_json(host: str, model: str, system_prompt: str, user_prompt: str,
                      timeout: int = 300) -> dict:
    resp = requests.post(
        f"{host}/api/chat",
        json={
            "model": model,
            "messages": [
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt},
            ],
            "format": "json",
            "stream": False,
            "options": {"temperature": 0.2},
        },
        timeout=timeout,
    )
    resp.raise_for_status()
    content = resp.json()["message"]["content"]

    try:
        return json.loads(content)
    except json.JSONDecodeError as e:
        raise RuntimeError(
            f"Model '{model}' returned invalid JSON. Raw output:\n{content}"
        ) from e


def call_ollama_embed(host: str, model: str, text: str, timeout: int = 60) -> list[float]:
    resp = requests.post(
        f"{host}/api/embeddings",
        json={"model": model, "prompt": text},
        timeout=timeout,
    )
    resp.raise_for_status()
    return resp.json()["embedding"]
