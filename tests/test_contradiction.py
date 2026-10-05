from arlab.contradiction import find_lexical_contradictions


def test_detects_simple_negation_conflict() -> None:
    result = find_lexical_contradictions([
        "the system is reliable",
        "the system is not reliable",
    ])
    assert len(result) == 1
