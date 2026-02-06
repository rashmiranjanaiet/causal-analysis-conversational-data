def extract_evidence(transcript):
    """
    Extract dialogue turns as evidence.
    """
    evidence = []

    for turn in transcript.get("conversation", []):
        text = turn.get("text", "").lower()
        if any(word in text for word in ["not received", "fraud", "failed", "error", "investigation"]):
            evidence.append({
                "speaker": turn.get("speaker"),
                "text": turn.get("text")
            })

    return evidence
