class ContextManager:
    """
    Manages multi-turn interaction context.
    """
    def __init__(self):
        self.previous_transcripts = set()
        self.previous_intent = None

    def update(self, transcript_id, intent):
        self.previous_transcripts.add(transcript_id)
        self.previous_intent = intent

    def is_used(self, transcript_id):
        return transcript_id in self.previous_transcripts
