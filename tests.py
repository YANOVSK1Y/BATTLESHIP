import unittest
import Battleship

class TestButtleship(unittest.TestCase):
    def setUp(self):
        self.battleship = Battleship()

    def test_shoot(self):
        return True
        #self.battleship.worker()


if __name__ == '__main__':
    unittest.main()
