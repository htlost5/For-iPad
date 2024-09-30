import os
os.environ['SDL_AUDIODRIVER'] = 'dummy'
import pygame
pygame.init()

# ウィンドウサイズの設定
width, height = 640, 480
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Simple Pygame Example")

# 色の定義
black = (0, 0, 0)
white = (255, 255, 255)

# ボールの設定
ball_pos = [width // 2, height // 2]
ball_radius = 20
ball_speed = [2, 2]

# メインループ
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # ボールの位置を更新
    ball_pos[0] += ball_speed[0]
    ball_pos[1] += ball_speed[1]

    # 壁で跳ね返る処理
    if ball_pos[0] - ball_radius < 0 or ball_pos[0] + ball_radius > width:
        ball_speed[0] = -ball_speed[0]
    if ball_pos[1] - ball_radius < 0 or ball_pos[1] + ball_radius > height:
        ball_speed[1] = -ball_speed[1]

    # 画面を黒でクリア
    screen.fill(black)

    # ボールを描画
    pygame.draw.circle(screen, white, ball_pos, ball_radius)

    # 画面を更新
    pygame.display.flip()

    # フレームレートの設定
    pygame.time.Clock().tick(60)

# Pygameの終了処理
pygame.quit()
sys.exit()