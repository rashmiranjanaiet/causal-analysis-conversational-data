from src.data_loader import load_transcripts
from src.transcript_filter import filter_by_intent
from src.context_manager import ContextManager
from src.causal_analyzer import identify_causal_factors

DATA_PATH = "data/Conversational_Transcript_Dataset.json"

def run():
    context = ContextManager()
    transcripts = load_transcripts(DATA_PATH)

    cases = filter_by_intent(transcripts, "Delivery Investigation")
    followups = []

    for case in cases:
        if not context.is_used(case["transcript_id"]):
            followups.append({
                "transcript_id": case["transcript_id"],
                "causal_factors": identify_causal_factors(case)
            })
            context.update(case["transcript_id"], case["intent"])

    return followups

if __name__ == "__main__":
    output = run()
    for item in output:
        print(item)
