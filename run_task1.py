import json
from jsonschema import validate
from jsonschema.exceptions import ValidationError

from src.data_loader import load_transcripts
from src.transcript_filter import filter_by_intent
from src.causal_analyzer import identify_causal_factors
from src.evidence_extractor import extract_evidence

DATA_PATH = "data/Conversational_Transcript_Dataset.json"
SCHEMA_PATH = "data/schema.json"


def validate_dataset():
    with open(DATA_PATH, "r", encoding="utf-8") as f:
        data = json.load(f)

    with open(SCHEMA_PATH, "r", encoding="utf-8") as s:
        schema = json.load(s)

    try:
        validate(instance=data, schema=schema)
        print("Dataset schema validated successfully ✅")
    except ValidationError as e:
        print("Schema validation failed ❌")
        print(e)
        exit(1)


def run():
    # ✅ Validate BEFORE processing
    validate_dataset()

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
