def filter_by_intent(transcripts, intent_name):
    """
    Filter transcripts by intent.
    """
    return [
        t for t in transcripts
        if t.get("intent", "").lower() == intent_name.lower()
    ]
