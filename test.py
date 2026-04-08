import unittest
from main import to_upper

class MyTestCase(unittest.TestCase):
    def test_to_upper(self):
        name="Aditya"
        up=to_upper(name)
        # Change "Aditya" to "ADITYA"
        self.assertEqual(up, "ADITYA") 

if __name__=='__main__':
    unittest.main()