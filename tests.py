import unittest
import task


class TestCase(unittest.TestCase):

    def test1(self):
        expected = "success"
        self.assertEqual(expected, task.firstrun())

    def test2(self):
        expected = "failure"
        self.assertNotEqual(expected, task.firstrun())

    def testradius(self):
        expected = 3.14
        self.assertEqual(expected, task.radius(1))

    def testlist(self):
        expected = 1, 2
        list = [1, 2]
        self.assertEqual(expected, task.list(list))

    def testdate(self):
        expected = 10
        self.assertEqual(expected, task.dates(311, 321))


if __name__ == '__main__':
    unittest.main()
