from test_result import TestResult


class TestSuite(object):
    def __init__(self):
        self.methods = []

    def add(self, method):
        self.methods.append(method)

    def run(self, result):
        for method in self.methods:
            method.run(result)
