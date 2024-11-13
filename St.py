import pygame
import sys

def main():
    pygame.init()
    pygame.display.set_caption("시작 페이지")
    screen = pygame.display.set_mode((1200,700))

    img_bg = pygame.image.load("img/BG_PG.png") #바탕이미지 1200x700크기
    img_st_btn = pygame.image.load("img/st_btn.png")#게임시작 버튼 100x50크기
    img_ct_btn = pygame.image.load("img/control_btn.png")#조작키 설명 버튼 100x50크기
    img_ct_des = pygame.image.load("img/control_des.png")#조작키 설명서 이미지 800x500크기

    # 버튼 위치 정의
    st_btn_plc = pygame.Rect(1000, 530, 100, 50)  # 게임 시작 버튼
    ct_btn_plc= pygame.Rect(1000, 600, 100, 50)  # 조작 설명 버튼

    ct_des_vis = False #조작 설명 화면에 표시 여부

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            #마우스
            if event.type == pygame.MOUSEBUTTONDOWN:
                # 마우스 클릭 시 위치 얻음
                mouse_x, mouse_y = pygame.mouse.get_pos()

                # 조작키 설명 버튼 클릭
                if ct_btn_plc.collidepoint(mouse_x, mouse_y):
                    ct_des_vis = not ct_des_vis

                # 게임 시작 버튼 클릭 (튜토리얼로 이동)
                if st_btn_plc.collidepoint(mouse_x, mouse_y):
                    import tutorial
                    tutorial.main()

        screen.blit(img_bg, [0, 0])#바탕이미지 위치
        screen.blit(img_st_btn, [1000, 530])#게임시작버튼 위치
        screen.blit(img_ct_btn, [1000, 600])#조작키설명버튼 위치

        if ct_des_vis:
            screen.blit(img_ct_des, [200, 100])  # 조작 설명서 표시 (위치)

        pygame.display.update()


if __name__ == '__main__':
    main()