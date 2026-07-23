def build_rag_prompt(context, question):
    return f"""
Context:
{'\n'.join(context)}

Question:
{question}

Instructions:
- Answer ONLY the user's question.
- Do not include unrelated bus information.
- If the user asks for stops, return only the stops.
- If the user asks for fare, return only fare details.
- If the user asks for schedules, return only schedules.
- Do not combine different answer types.
- If the answer is not present in the context, say:
  "The requested information is not available in the current travel database."

Answer:
"""