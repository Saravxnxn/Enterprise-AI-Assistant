from app.ai.prompts.manager import PromptManager


class MemoryManager:

    @staticmethod
    def build_messages(history, current_message: str):

        system_prompt = PromptManager.load("enterprise_assistant")

        messages = [
            {
                "role": "system",
                "content": system_prompt,
            }
        ]

        for msg in history:
            messages.append(
                {
                    "role": msg.role,
                    "content": msg.content,
                }
            )

        # Do NOT append current_message here.
        # It has already been saved to the database,
        # so load_history() already includes it.

        return messages
