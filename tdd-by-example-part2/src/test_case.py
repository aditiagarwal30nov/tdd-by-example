from test_result import TestResult


class TestCase:
    def __init__(self, name):
        self.name = name

    def run(self, result):
        result.testStarted()
        self.setUp()
        try:
            method = getattr(self, self.name)
            method()
        except Exception:
            result.testFailed()
        finally:
            self.tearDown()

    def setUp(self):
        pass

    def tearDown(self):
        pass
