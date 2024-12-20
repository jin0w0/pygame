import pygame
import sys
import os

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

def main():
    pygame.init()
    screen_width = 1200
    screen_height = 700
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("HEART OF TRUTH")
    # 배경이미지 관리
    background_image = pygame.image.load("start.png")
    background_image = pygame.transform.scale(background_image, (screen_width, screen_height))
    # 버튼 위치 및 크기 정의 (앞의 두개의 값은 각각 X좌표 Y좌표 뒤의 두개의 값은 사각형의 가로 세로값)
    font = pygame.font.Font(None, 36)
    start_button = pygame.Rect(320, 620, 230, 60)
    exit_button = pygame.Rect(625, 620, 230, 60)
    start_text = font.render("",True, WHITE)
    exit_text = font.render("",True, WHITE)

    # 메인 동작
    running = True
    while running:
        # 배경출력
        screen.blit(background_image, (0, 0))
        # 버튼출력
        screen.blit(start_text, (start_button.x + 70, start_button.y + 10))
        screen.blit(exit_text, (exit_button.x + 80, exit_button.y + 10))
        pygame.display.flip()
        # 이벤트 처리 start버튼 클릭시 story1.py 실행, exit버튼 클릭시 종료
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if start_button.collidepoint(event.pos):
                    os.system("python story1.py")
                elif exit_button.collidepoint(event.pos):
                    running = False

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
