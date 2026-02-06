def identify_causal_factors(transcript):
    """
    Identify causal factors based on dialogue patterns.
    """
    factors = []
    reason = transcript.get("reason_for_call", "")

    if "not received" in reason.lower():
        factors.append("Customer reported item marked delivered but not received")

    if "fraud" in reason.lower():
        factors.append("Unauthorized transaction triggered fraud investigation")

    if "failed" in reason.lower():
        factors.append("Repeated service failure caused escalation")

    if not factors:
        factors.append("Causal factors inferred from conversation context")

    return factors

