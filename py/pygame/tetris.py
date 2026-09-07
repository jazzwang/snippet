import pygame
import random
from typing import List

# ============= 顏色定義 =============
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (128, 128, 128)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
PURPLE = (128, 0, 128)
CYAN = (0, 255, 255)
ORANGE = (255, 165, 0)

# ============= 塊的形狀定義 =============
PIECES = {
    'I': [[0, 0, 0, 0],
          [1, 1, 1, 1],
          [0, 0, 0, 0],
          [0, 0, 0, 0]],
    'J': [[1, 0, 0],
          [1, 1, 1],
          [0, 0, 0]],
    'L': [[0, 0, 1],
          [1, 1, 1],
          [0, 0, 0]],
    'O': [[1, 1],
          [1, 1]],
    'S': [[0, 1, 1],
          [1, 1, 0],
          [0, 0, 0]],
    'T': [[0, 1, 0],
          [1, 1, 1],
          [0, 0, 0]],
    'Z': [[1, 1, 0],
          [0, 1, 1],
          [0, 0, 0]],
}

# 對應顏色
PIECE_COLORS = {
    'I': BLUE,
    'J': BLACK,
    'L': ORANGE,
    'O': YELLOW,
    'S': GREEN,
    'T': PURPLE,
    'Z': RED,
}

# ============= 遊戲類別 =============
class TetrisGame:
    def __init__(self, width: int = 10, height: int = 20):
        """初始化遊戲"""
        self.width = width
        self.height = height
        self.grid = [[0] * width for _ in range(height)]
        self.current_piece = None
        self.next_piece = None
        self.score = 0
        self.level = 1
        self.game_over = False
        
        # 初始化 pygame
        pygame.init()
        self.cell_size = 30
        screen_size = (width * self.cell_size, height * self.cell_size)
        self.screen = pygame.display.set_mode(screen_size)
        pygame.display.set_caption("俄羅斯方塊 - Tetris")
        self.font = pygame.font.Font(None, 36)
        
        self.run()

    def spawn_piece(self):
        """生成新塊"""
        piece_types = list(PIECES.keys())
        self.next_piece = random.choice(piece_types)
        
        self.current_piece = {
            'type': self.next_piece,
            'x': self.width // 2 - 2,
            'y': 0,
        }
        
        # 檢查新生成的塊是否卡住
        if self.check_collision(self.current_piece['x'], 
                              self.current_piece['y'],
                              PIECES[self.current_piece['type']]):
            self.game_over = True

    def get_piece_shape(self) -> List[List[int]]:
        """獲取當前塊的形狀"""
        return PIECES[self.current_piece['type']]

    def rotate_piece(self, shape: List[List[int]]) -> List[List[int]]:
        """旋轉塊 90 度"""
        return [[row[-1] for row in shape] + [row[0] for row in shape]]

    def check_collision(self, x: int, y: int, 
                       shape: List[List[int]]) -> bool:
        """檢查是否發生碰撞"""
        for dy, row in enumerate(shape):
            for dx, value in enumerate(row):
                if value:
                    new_x = x + dx
                    new_y = y + dy
                    # 檢查邊界
                    if new_x < 0 or new_x >= self.width or new_y >= self.height:
                        return True
                    # 檢查是否與現有塊碰撞
                    if new_y >= 0 and self.grid[new_y][new_x]:
                        return True
        return False

    def move_piece(self, dx: int, dy: int) -> bool:
        """移動塊"""
        if self.current_piece is None:
            return False
        
        new_x = self.current_piece['x'] + dx
        new_y = self.current_piece['y'] + dy
        shape = self.get_piece_shape()
        
        if not self.check_collision(new_x, new_y, shape):
            self.current_piece['x'] = new_x
            self.current_piece['y'] = new_y
            return True
        return False

    def rotate_current_piece(self) -> bool:
        """旋轉當前塊"""
        shape = self.get_piece_shape()
        rotated = self.rotate_piece(shape)
        new_x = self.current_piece['x']
        new_y = self.current_piece['y']
        
        if not self.check_collision(new_x, new_y, rotated):
            # 簡單的牆踢
            for kick in [-1, 1, -2, 2]:
                if not self.check_collision(new_x + kick, new_y, shape):
                    self.current_piece['x'] = new_x + kick
                    return True
        return False

    def lock_piece(self):
        """固定塊到遊戲網格"""
        shape = self.get_piece_shape()
        for dy, row in enumerate(shape):
            for dx, value in enumerate(row):
                if value:
                    y = self.current_piece['y'] + dy
                    x = self.current_piece['x'] + dx
                    if 0 <= y < self.height:
                        self.grid[y][x] = 1
        
        self.spawn_piece()
        self.check_lines()

    def check_lines(self):
        """檢查並清除完成的行"""
        lines_cleared = 0
        for y in range(self.height - 1, -1, -1):
            if all(self.grid[y]):
                del self.grid[y]
                self.grid.insert(0, [0] * self.width)
                lines_cleared += 1
        
        # 評分系統
        if lines_cleared > 0:
            points = [0, 100, 300, 500, 800]
            self.score += points[lines_cleared] * self.level
            self.level = self.score // 1000 + 1

    def draw(self):
        """繪製遊戲畫面"""
        self.screen.fill(BLACK)
        
        # 繪製網格線
        for i in range(self.width + 1):
            pygame.draw.line(self.screen, GRAY, 
                           (i * self.cell_size, 0), 
                           (i * self.cell_size, self.height * self.cell_size))
        for i in range(self.height + 1):
            pygame.draw.line(self.screen, GRAY,
                           (0, i * self.cell_size),
                           (self.width * self.cell_size, i * self.cell_size))
        
        # 繪製已固定的塊
        for y, row in enumerate(self.grid):
            for x, value in enumerate(row):
                if value:
                    pygame.draw.rect(self.screen, WHITE,
                                   (x * self.cell_size, y * self.cell_size,
                                    self.cell_size - 1, self.cell_size - 1))
        
        # 繪製當前塊
        if self.current_piece:
            shape = self.get_piece_shape()
            color = PIECE_COLORS[self.current_piece['type']]
            for dy, row in enumerate(shape):
                for dx, value in enumerate(row):
                    if value:
                        pygame.draw.rect(self.screen, color,
                                       (self.current_piece['x'] + dx * self.cell_size,
                                        self.current_piece['y'] + dy * self.cell_size,
                                        self.cell_size - 1, self.cell_size - 1))
        
        # 顯示分數和等級
        score_text = self.font.render(f'Score: {self.score}', True, WHITE)
        level_text = self.font.render(f'Level: {self.level}', True, WHITE)
        self.screen.blit(score_text, (10, 10))
        self.screen.blit(level_text, (10, 50))
        
        # 顯示下一個塊
        next_text = self.font.render('Next:', True, WHITE)
        self.screen.blit(next_text, (10, 80))
        if self.next_piece:
            shape = PIECES[self.next_piece]
            next_color = PIECE_COLORS[self.next_piece]
            for dy, row in enumerate(shape):
                for dx, value in enumerate(row):
                    if value:
                        pygame.draw.rect(self.screen, next_color,
                                       (120 + dx * self.cell_size,
                                        100 + dy * self.cell_size,
                                        self.cell_size - 1, self.cell_size - 1))
        
        # 遊戲結束訊息
        if self.game_over:
            game_over_text = self.font.render('GAME OVER', True, RED)
            restart_text = self.font.render('按 R 重啟', True, WHITE)
            self.screen.blit(game_over_text, (250, 95))
            self.screen.blit(restart_text, (240, 120))
        
        pygame.display.flip()

    def run(self):
        """遊戲主循環"""
        running = True
        self.spawn_piece()
        
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.KEYDOWN:
                    if self.game_over:
                        if event.key == pygame.K_r:
                            self.score = 0
                            self.level = 1
                            self.grid = [[0] * self.width for _ in range(self.height)]
                            self.game_over = False
                            self.spawn_piece()
                    else:
                        if event.key in (pygame.K_LEFT, pygame.K_a):
                            self.move_piece(-1, 0)
                        elif event.key in (pygame.K_RIGHT, pygame.K_d):
                            self.move_piece(1, 0)
                        elif event.key in (pygame.K_DOWN, pygame.K_s):
                            self.move_piece(0, 1)
                        elif event.key in (pygame.K_UP, pygame.K_w):
                            self.rotate_current_piece()
                        elif event.key == pygame.K_SPACE:
                            # 直接降落
                            while self.move_piece(0, 1):
                                pass
                        elif event.key == pygame.K_ESCAPE:
                            running = False
            
            # 自動下降
            if not self.game_over and self.current_piece:
                if self.move_piece(0, 1):
                    pass
                else:
                    self.lock_piece()
            
            self.draw()
        
        pygame.quit()


# ============= 執行遊戲 =============
if __name__ == "__main__":
    print("=" * 50)
    print("  俄羅斯方塊遊戲")
    print("=" * 50)
    print("操作說明：")
    print("  ← → 或 A/D：左右移動")
    print("  ↑ 或 W：旋轉塊")
    print("  ↓ 或 S：加速下降")
    print("  Space：直接降落")
    print("  R：遊戲結束後重啟")
    print("  ESC：退出遊戲")
    print("=" * 50)
    
    game = TetrisGame()
