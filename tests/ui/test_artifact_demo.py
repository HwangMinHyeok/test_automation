import pytest


@pytest.mark.skip(reason="Artifact capture demo intentionally clicks a missing selector.")
def test_artifact_capture_demo(home_page):
    home_page.locator("#id_for_test_failure").click(timeout=1000)
