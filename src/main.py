import pygame
import sys
from menu import Menu

# Khởi tạo Pygame
pygame.init()
screen = pygame.display.set_mode((1000, 800))
pygame.display.set_caption("Pac-Man AI - Main Menu")

# Khởi tạo Menu
menu = Menu(screen)

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            # Xử lý click chuột
            level = menu.handle_click(event.pos)
            if level:
                print(f"User selected: {level}")
                # Thực hiện chuyển đến level tương ứng
                running = False

    menu.draw()
