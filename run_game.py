#!/usr/bin/env python3
"""
主游戏运行文件
"""

from src.game import NumberGuessingGame

def main():
    """主函数"""
    print("🎮 欢迎来到数字猜谜游戏!")
    game = NumberGuessingGame()
    game.start()

if __name__ == "__main__":
    main()