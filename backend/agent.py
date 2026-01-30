import os
from typing import List, Dict

from openai import OpenAI

client = OpenAI()

def run_agent(message: str, memory: List[Dict[str, str]]) -> str:
    """
    memory format:
      [{"role": "user"/"assistant", "content": "..."}]
    """

    model = os.getenv("OPENAI_MODEL", "gpt-4.1-mini")

    # Convert your memory into a single input string (simple + reliable for demos)
    # Later, you can send structured messages or add tools.
    convo = []
    for m in memory[-12:]:  # keep it small to control token usage
        convo.append(f"{m['role'].upper()}: {m['content']}")
    convo.append(f"USER: {message}")
    input_text = "\n".join(convo)

    response = client.responses.create(
        model=model,
        input=input_text
    )

    return response.output_text
