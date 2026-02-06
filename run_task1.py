from src.data_loader import load_transcripts
from src.transcript_filter import filter_by_intent
from src.causal_analyzer import identify_causal_factors
from src.evidence_extractor import extract_evidence

DATA_PATH = "data/Conversational_Transcript_Dataset.json"

def run():
    transcripts = load_transcripts(DATA_PATH)
    cases = filter_by_intent(transcripts, "Delivery Investigation")

    results = []
    for case in cases:
        result = {
            "transcript_id": case.get("transcript_id"),
            "causal_factors": identify_causal_factors(case),
            "evidence": extract_evidence(case)
        }
        results.append(result)

    return results

if __name__ == "__main__":
    output = run()
    for item in output:
        print(item)
