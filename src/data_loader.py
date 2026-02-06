import json

def load_transcripts(file_path):
    """
    Load conversational transcript dataset from JSON file.
    """
    with open(file_path, "r", encoding="utf-8") as f:
        return json.load(f)
