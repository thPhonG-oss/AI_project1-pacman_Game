import pygame
import sys  

def main():
    pygame.init()
    screen = pygame.display.set_mode((448, 535))
    pygame.display.set_caption("PacMan-HCMUS")

    # Tải hình ảnh nền
    try:
        background_img = pygame.image.load("assets/maze/background.png").convert()
    except pygame.error as e:
        print(f"Không thể tải hình ảnh nền: {e}")
        pygame.quit()
        sys.exit()

    # Vẽ nền lên cửa sổ
    screen.fill((0, 0, 0))  # Màu nền đen
    screen.blit(background_img, (0, 0))
    pygame.display.flip()


    # Vòng lặp sự kiện chính
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # Đóng cửa sổ khi nhấn nút X
                running = False

    pygame.quit()

if __name__ == "__main__":
    main()