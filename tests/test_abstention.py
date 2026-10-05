from arlab.abstention import AbstentionPolicy


def test_abstention_requires_minimum_support() -> None:
    policy = AbstentionPolicy(min_confidence=0.7, min_evidence=2)
    assert policy.should_abstain(confidence=0.6, evidence_count=5)
    assert policy.should_abstain(confidence=0.9, evidence_count=1)
    assert not policy.should_abstain(confidence=0.9, evidence_count=2)
