import random

class NumberGuessingGame:
    """数字猜谜游戏类"""
    
    def __init__(self, min_number=1, max_number=100, max_attempts=10):
        self.min_number = min_number
        self.max_number = max_number
        self.max_attempts = max_attempts
        self.score = 0
        self.high_score = 0
        
    def generate_number(self):
        """生成随机数字"""
        return random.randint(self.min_number, self.max_number)
    
    def get_user_input(self, prompt):
        """获取用户输入"""
        while True:
            try:
                return int(input(prompt))
            except ValueError:
                print("❌ 请输入一个有效的数字!")
    
    def start(self):
        """开始游戏"""
        while True:
            print(f"\n🎯 我已经想好了一个 {self.min_number} 到 {self.max_number} 之间的数字!")
            print(f"你有 {self.max_attempts} 次机会来猜中它!")
            
            target_number = self.generate_number()
            attempts = 0
            won = False
            
            while attempts < self.max_attempts:
                guess = self.get_user_input(f"请输入你的猜测 ({attempts + 1}/{self.max_attempts}): ")
                
                if guess < target_number:
                    print("📈 太低了! 再试一次!")
                elif guess > target_number:
                    print("📉 太高了! 再试一次!")
                else:
                    print(f"🎉 恭喜! 你猜对了! 数字就是 {target_number}!")
                    self.score += 1
                    won = True
                    break
                    
                attempts += 1
            
            if not won:
                print(f"😅 游戏结束! 正确的数字是 {target_number}")
                self.score = 0
            
            # 更新最高分
            if self.score > self.high_score:
                self.high_score = self.score
            
            # 显示分数
            print(f"\n⭐ 当前连胜: {self.score}")
            print(f"🏆 最高连胜: {self.high_score}")
            
            # 询问是否继续游戏
            play_again = input("\n还想再玩一次吗? (y/n): ").lower()
            if play_again != 'y':
                print("👋 感谢游玩! 再见!")
                break