from arlab.calibration import evaluate_calibration


def test_calibration_report() -> None:
    report = evaluate_calibration([1.0, 0.0], [True, False])
    assert report.observed_accuracy == 0.5
    assert report.mean_absolute_gap == 0.0
