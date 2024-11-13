import pygame
import sys

# 맵[y][x] 12x7
map = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],  
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
]

# 이미지
img_wall = pygame.image.load("img/wall.png")  # 벽1
img_p = pygame.image.load("img/p_d.png")  # 플레이어
img_e = pygame.image.load("img/end.png")  # end
img_move = pygame.image.load("img/move.png")  # 움직이는 블럭

# 플레이어 시작 위치
pl_x = 1
pl_y = 5
# 움직이는 블럭의 위치 추적
move_x = 3
move_y = 3  

# 플레이어 움직임
def player_move(event):
    global pl_x, pl_y, move_x, move_y
    if event.type == pygame.KEYDOWN:
        # 'r' 키를 눌러서 플레이어 위치 초기화
        if event.key == pygame.K_r:
            pl_x = 1
            pl_y = 5
            move_x = 3
            move_y = 3 
        # 플레이어가 이동하려는 방향으로 블럭이 있는지 확인
        if event.key == pygame.K_UP:
            if map[pl_y - 1][pl_x] != 1:
                pl_y -= 1
                # 블럭 밀기
                if pl_y == move_y and pl_x == move_x:
                    if map[move_y - 1][move_x] != 1:  # 밀려날 자리가 벽이 아니라면
                        move_y -= 1
                    else:
                        pl_y += 1
        elif event.key == pygame.K_DOWN:
            if map[pl_y + 1][pl_x] != 1:
                pl_y += 1
                # 블럭 밀기
                if pl_y == move_y and pl_x == move_x:
                    if map[move_y + 1][move_x] != 1:
                        move_y += 1
                    else:
                        pl_y -= 1
        elif event.key == pygame.K_LEFT:
            if map[pl_y][pl_x - 1] != 1:
                pl_x -= 1
                # 블럭 밀기
                if pl_x == move_x and pl_y == move_y:
                    if map[move_y][move_x - 1] != 1:
                        move_x -= 1
                    else:
                        pl_x += 1
        elif event.key == pygame.K_RIGHT:
            if map[pl_y][pl_x + 1] != 1:
                pl_x += 1
                # 블럭 밀기
                if pl_x == move_x and pl_y == move_y:
                    if map[move_y][move_x + 1] != 1:
                        move_x += 1
                    else:
                        pl_x -= 1

def main():
    global pl_x, pl_y, move_x, move_y
    pygame.init()
    pygame.display.set_caption("튜토리얼")
    screen = pygame.display.set_mode((1200, 700))
    clock = pygame.time.Clock()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            player_move(event)

        # 화면
        screen.fill((255, 255, 255))  # 화면 초기화

        # 벽
        for y in range(7):
            for x in range(12):
                if map[y][x] == 1:
                    screen.blit(img_wall, [x * 100, y * 100])

        # 엔드 위치
        screen.blit(img_e, [1000, 100])

        # 플레이어
        screen.blit(img_p, [pl_x * 100, pl_y * 100])

        # 움직이는 블럭
        screen.blit(img_move, [move_x * 100, move_y * 100])

        # 플레이어가 end에 도달하면 종료
        if pl_x == 10 and pl_y == 1:
            pass

        pygame.display.update()
        clock.tick(10)

if __name__ == '__main__':
    main()