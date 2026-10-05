from arlab.evaluation import Case, evaluate


def test_evaluation_is_reproducible() -> None:
    report = evaluate(
        [Case("1", "a", "A"), Case("2", "b", "B")],
        lambda value: value.upper(),
    )
    assert report.total == 2
    assert report.passed == 2
    assert report.accuracy == 1.0
