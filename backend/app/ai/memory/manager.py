class MemoryManager:

    @staticmethod
    def build_messages(history, current_message: str):

        messages = [
            {
                "role": "system",
                "content": (
                    "You are Enterprise AI Assistant. "
                    "Be professional, concise and helpful."
                ),
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
