import unittest
import sys
import os

# 添加src目录到路径
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src'))

from game import NumberGuessingGame

class TestGame(unittest.TestCase):
    """游戏测试类"""
    
    def test_number_generation(self):
        """测试数字生成范围"""
        game = NumberGuessingGame(1, 10)
        number = game.generate_number()
        self.assertTrue(1 <= number <= 10)
    
    def test_game_initialization(self):
        """测试游戏初始化"""
        game = NumberGuessingGame(1, 50, 5)
        self.assertEqual(game.min_number, 1)
        self.assertEqual(game.max_number, 50)
        self.assertEqual(game.max_attempts, 5)

if __name__ == '__main__':
    unittest.main()