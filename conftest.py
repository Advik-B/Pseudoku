import pytest

def pytest_sessionfinish(session, exitstatus):
    if exitstatus == pytest.ExitCode.NO_TESTS_COLLECTED:
        # Modify the exit status to 0 if no tests were run
        return pytest.ExitCode.OK
