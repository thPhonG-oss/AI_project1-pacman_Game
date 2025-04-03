import pygame
import sys

class Menu:
    def __init__(self, screen):
        self.screen = screen
        self.font = pygame.font.SysFont('Arial', 30)
        self.button_color = (0, 0, 255)  # Màu nút bình thường
        self.hover_color = (0, 255, 0)  # Màu nút khi hover
        self.text_color = (255, 255, 255)  # Màu chữ
        self.buttons = {
            'Level 1 - BFS': (0, 0),
            'Level 2 - DFS': (0, 0),
            'Level 3 - UCS': (0, 0),
            'Level 4 - A*': (0, 0),
            'Level 5 - Parallel Execution': (0, 0),
            'Level 6 - User-Controlled Pac-Man': (0, 0),
            'Exit': (0, 0)
        }
        self.button_rects = {}  # Lưu vị trí của các button để xử lý hiệu ứng hover
        self.button_width = 600
        self.button_height = 50
        self.vertical_spacing = 20  # Khoảng cách giữa các button
        self.center_x = self.screen.get_width() // 2  # Trung tâm theo chiều ngang
        self.start_y = (self.screen.get_height() - (len(self.buttons) * (self.button_height + self.vertical_spacing))) // 2  # Trung tâm theo chiều dọc

    def draw(self):
        self.screen.fill((0, 0, 0))  # Màu nền đen

        # Vẽ tất cả các button
        for i, (button_text, _) in enumerate(self.buttons.items()):
            button_rect = pygame.Rect(self.center_x - self.button_width // 2, self.start_y + i * (self.button_height + self.vertical_spacing), self.button_width, self.button_height)
            self.button_rects[button_text] = button_rect

            # Kiểm tra xem chuột có đang hover lên button không
            if button_rect.collidepoint(pygame.mouse.get_pos()):
                button_color = self.hover_color
            else:
                button_color = self.button_color

            # Vẽ button với màu nền và viền
            pygame.draw.rect(self.screen, button_color, button_rect)
            pygame.draw.rect(self.screen, (0, 0, 0), button_rect, 3)  # Viền màu đen

            # Vẽ chữ trong button
            button_surface = self.font.render(button_text, True, self.text_color)
            self.screen.blit(button_surface, (button_rect.centerx - button_surface.get_width() // 2, button_rect.centery - button_surface.get_height() // 2))

        pygame.display.update()

    def handle_click(self, pos):
        for button_text, button_rect in self.button_rects.items():
            if button_rect.collidepoint(pos):
                if button_text == 'Exit':
                    pygame.quit()
                    sys.exit()
                return button_text
        return None
