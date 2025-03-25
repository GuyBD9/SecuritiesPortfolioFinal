import asyncio
from ai.ollama_model import OllamaModel

class AIController:
    def __init__(self):
        self.ai_model = OllamaModel()

    async def consult_ai(self, question: str) -> str:
        """Handles AI queries asynchronously to prevent blocking."""
        loop = asyncio.get_event_loop()
        try:
            response = await loop.run_in_executor(None, self.ai_model.query, question)
            return response
        except Exception as e:
            return f" AI Error: {str(e)}"
