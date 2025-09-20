import os
try:
    import openai
except Exception:
    openai = None

class LLMClient:
    def __init__(self):
        self.provider = os.getenv('LLM_PROVIDER', 'openai')
        self.api_key = os.getenv('OPENAI_API_KEY', '')
        if openai and self.api_key:
            openai.api_key = self.api_key

    def get_response(self, text, intent=None):
        # If OpenAI is available and API key is set, call it.
        if openai and self.api_key and self.provider == 'openai':
            try:
                prompt = self._build_prompt(text, intent)
                resp = openai.ChatCompletion.create(
                    model=os.getenv('OPENAI_MODEL','gpt-4o-mini'),
                    messages=[{'role':'system','content':'You are a concise empathetic mental health assistant.'},
                              {'role':'user','content':prompt}],
                    max_tokens=200,
                    temperature=0.7
                )
                choice = resp['choices'][0]['message']['content'].strip()
                return choice
            except Exception as e:
                # fallback to mock reply on error
                return f"(LLM error fallback) I hear you. Would you like a coping exercise or resources? [{e}]"
        # Mock fallback
        if intent == 'mood_check':
            return "I'm sorry you're feeling this way. Would you like a short grounding exercise or a mood quiz?"
        if 'hello' in text.lower() or 'hi' in text.lower():
            return 'Hi — I am Health Hackers. How are you feeling today?'
        return "I hear you. Would you like a coping exercise or resources?"

    def _build_prompt(self, text, intent):
        # Keep prompts short and safe: instruct LLM to avoid diagnosis and to escalate if suicidal ideation.
        system = (
            "You are an empathetic mental health support assistant. Do NOT provide medical diagnosis or prescriptions."
            "If the user expresses self-harm or suicidal intent, respond with a crisis escalation message and include helpline suggestions."
        )
        user = f"User said: {text}\nIntent: {intent}\nRespond empathetically and offer a short next-step (exercise, mood check or helpline)."
        return user
