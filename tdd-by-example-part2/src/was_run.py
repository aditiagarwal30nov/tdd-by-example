from test_case import TestCase


class WasRun(TestCase):
    def __init__(self, name):
        TestCase.__init__(self, name)

    def testMethod(self):
        self.wasRun = 1
        self.log = self.log + "testMethod "

    def setUp(self):
        self.wasSetUp = 1
        self.log = "setUp "
        self.wasRun = None

    def tearDown(self):
        self.log = self.log + "tearDown"

    def testBrokenMethod(self):
        raise Exception
