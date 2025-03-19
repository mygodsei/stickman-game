import pygame
import sys
import random
import time
import os

# Initialize pygame
pygame.init()

# Set up the display
backWIDTH, backHEIGHT = 1536, 800
WIDTH, HEIGHT = 150, 90
gunWIDTH, gunHEIGHT = 100, 70
hpWIDTH, hpHEIGHT = 310, 130
screen = pygame.display.set_mode((backWIDTH, backHEIGHT))
image = pygame.image.load("OOF_picture.ico")
pygame.display.set_caption("火柴人拿槍槍天下")
pygame.display.set_icon(image)
current_dir = os.getcwd()

# Set path
resource_folder = os.path.join(current_dir, "resources")
music_folder = os.path.join(current_dir, "mus")

# Load images
lobby_img = pygame.image.load(os.path.join(resource_folder, "lobby.png"))
map_img = pygame.image.load(os.path.join(resource_folder, "map.png"))
manex_U_img = pygame.image.load(os.path.join(resource_folder, "manexU.png"))
manex_D_img = pygame.image.load(os.path.join(resource_folder, "manexD.png"))
manex_L_img = pygame.image.load(os.path.join(resource_folder, "manL.png"))
manex_R_img = pygame.image.load(os.path.join(resource_folder, "manR.png"))
gun_U_img = pygame.image.load(os.path.join(resource_folder, "gunU.png"))
gun_D_img = pygame.image.load(os.path.join(resource_folder, "gunD.png"))
gun_L_img = pygame.image.load(os.path.join(resource_folder, "gunL.png"))
gun_R_img = pygame.image.load(os.path.join(resource_folder, "gunR.png"))
bullet_U_img = pygame.image.load(os.path.join(resource_folder, "bulletU.png"))
bullet_D_img = pygame.image.load(os.path.join(resource_folder, "bulletD.png"))
bullet_L_img = pygame.image.load(os.path.join(resource_folder, "bulletL.png"))
bullet_R_img = pygame.image.load(os.path.join(resource_folder, "bulletR.png"))
sausage_U_img = pygame.image.load(os.path.join(resource_folder, "sausageU.png"))
sausage_D_img = pygame.image.load(os.path.join(resource_folder, "sausageD.png"))
sausage_L_img = pygame.image.load(os.path.join(resource_folder, "sausageL.png"))
sausage_R_img = pygame.image.load(os.path.join(resource_folder, "sausageR.png"))
croco_U_img = pygame.image.load(os.path.join(resource_folder, "crocoU.png"))
croco_D_img = pygame.image.load(os.path.join(resource_folder, "crocoD.png"))
croco_L_img = pygame.image.load(os.path.join(resource_folder, "crocoL.png"))
croco_R_img = pygame.image.load(os.path.join(resource_folder, "crocoR.png"))
hp_20_img = pygame.image.load(os.path.join(resource_folder, "hp20.png"))
hp_40_img = pygame.image.load(os.path.join(resource_folder, "hp40.png"))
hp_60_img = pygame.image.load(os.path.join(resource_folder, "hp60.png"))
hp_80_img = pygame.image.load(os.path.join(resource_folder, "hp80.png"))
hp_100_img = pygame.image.load(os.path.join(resource_folder, "hp100.png"))
hp_ex_img = pygame.image.load(os.path.join(resource_folder, "hpex.png"))

# Transform (scale) images
lobby_img = pygame.transform.scale(lobby_img, (backWIDTH, backHEIGHT))
map_img = pygame.transform.scale(map_img, (backWIDTH, backHEIGHT))
gun_U_img = pygame.transform.scale(gun_U_img, (gunWIDTH, gunHEIGHT))
gun_D_img = pygame.transform.scale(gun_D_img, (gunWIDTH, gunHEIGHT))
gun_L_img = pygame.transform.scale(gun_L_img, (gunWIDTH, gunHEIGHT))
gun_R_img = pygame.transform.scale(gun_R_img, (gunWIDTH, gunHEIGHT))
hp_100_img = pygame.transform.scale(hp_100_img, (hpWIDTH, hpHEIGHT))

# Game variables
manex_speed = 3
bullet_speed = 5
manex_rect = manex_U_img.get_rect()
gun_rect = gun_U_img.get_rect()
bullet_rect = bullet_U_img.get_rect()
manex_rect.center = (backWIDTH // 2, backHEIGHT // 2)
gun_rect.center = manex_rect.center
bullets = []
music_intro = os.path.join(music_folder, "mus_school.ogg")
music_map1 = os.path.join(music_folder, "KEYGEN.ogg")
music_map2 = os.path.join(music_folder, "queen_boss.ogg")
music_map3 = os.path.join(music_folder, "berdly_chase.ogg")
music_map4 = os.path.join(music_folder, "joker.ogg")
music_gover = os.path.join(music_folder, "AUDIO_DEFEAT.ogg")

# 隨機排序音樂清單
music_list = [music_map1, music_map2, music_map3, music_map4]
random.shuffle(music_list)

# Game state
is_in_lobby = True  # True if in the lobby, False if in the map
direction = 'D'  # 'U' for up, 'D' for down, 'L' for left, 'R' for right
manex_img = manex_D_img
gun_img = gun_D_img
bullet_img = bullet_D_img

# Timer variables
shoot_delay = 2000  # Delay in milliseconds (2 seconds)
last_shoot_time = pygame.time.get_ticks()

# Play music
pygame.mixer.music.load(music_intro)
pygame.mixer.music.play(-1)

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.mixer.music.stop()
            pygame.quit()
            sys.exit()

    # Get the state of all keyboard keys
    keys = pygame.key.get_pressed()

    if is_in_lobby and event.type == pygame.MOUSEBUTTONDOWN:
        if event.button == 1:  # 檢測滑鼠左鍵按下
            is_in_lobby = False
        pygame.mixer.music.stop()  # 停止播放開場音樂
        pygame.mixer.music.load(music_list[0])
        pygame.mixer.music.play(-1)  # 開始播放地圖音樂
        music_list.append(music_list.pop(0))  # 將已播放的音樂移到清單末尾
    elif not is_in_lobby and event.type == pygame.MOUSEBUTTONDOWN:
        if event.button == 1:  # 檢測滑鼠左鍵按下
            pass  # 不執行任何操作，以防止切換回大廳

    if not is_in_lobby:
        if keys[pygame.K_w]:
            # Move manex and gun up
            if manex_rect.y - manex_speed >= 0:
                manex_rect.y -= manex_speed
                gun_rect.y -= manex_speed
            direction = 'U'
        if keys[pygame.K_s]:
            # Move manex and gun down
            if manex_rect.y + manex_speed + manex_rect.height <= backHEIGHT:
                manex_rect.y += manex_speed
                gun_rect.y += manex_speed
            direction = 'D'
        if keys[pygame.K_a]:
            # Move manex and gun left
            if manex_rect.x - manex_speed >= 0:
                manex_rect.x -= manex_speed
                gun_rect.x -= manex_speed
            direction = 'L'
        if keys[pygame.K_d]:
            # Move manex and gun right
            if manex_rect.x + manex_speed + manex_rect.width <= backWIDTH:
                manex_rect.x += manex_speed
                gun_rect.x += manex_speed
            direction = 'R'

    # Clear the screen
    screen.fill((0, 0, 0))

    # Draw the lobby or map
    if is_in_lobby:
        screen.blit(lobby_img, (0, 0))
    else:
        screen.blit(map_img, (0, 0))

    # Draw manex and gun
    if not is_in_lobby:
        if direction == 'U':
            manex_img = manex_U_img
            gun_img = gun_U_img
        elif direction == 'D':
            manex_img = manex_D_img
            gun_img = gun_D_img
        elif direction == 'L':
            manex_img = manex_L_img
            gun_img = gun_L_img
        elif direction == 'R':
            manex_img = manex_R_img
            gun_img = gun_R_img

        screen.blit(manex_img, manex_rect)
        screen.blit(gun_img, gun_rect)
        # Draw health bar
        if not is_in_lobby:
            screen.blit(hp_100_img, (10, 10))  # Draw health bar at the top left corner

    # Update the display
    pygame.display.flip()

# Quit the game
pygame.quit()
sys.exit()
