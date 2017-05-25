import unittest
from HTMLTestRunner import HTMLTestRunner

from TestEvent import TestEvent
from TestFriend import TestFriend
from TestPost import TestPost
from TestProfile import TestProfile

if __name__ == '__main__':
    # get all tests from SearchText and HomePageTest class
    tests_event = unittest.TestLoader().loadTestsFromTestCase(TestEvent)
    tests_friends = unittest.TestLoader().loadTestsFromTestCase(TestFriend)
    tests_post = unittest.TestLoader().loadTestsFromTestCase(TestPost)
    tests_profile = unittest.TestLoader().loadTestsFromTestCase(TestProfile)

    # create a test suite
    test_suite = unittest.TestSuite()
    test_suite.addTests(tests_event)
    test_suite.addTests(tests_post)
    test_suite.addTests(tests_profile)
    test_suite.addTests(tests_friends)

    with open('Report.html', 'w') as f:
        runner = HTMLTestRunner(stream=f,
                                title='Socify Test Report',
                                description='generated by HTMLTestRunner.'
                                )
        runner.run(test_suite)
