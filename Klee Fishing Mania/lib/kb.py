import pygame
import random

def klee_movement(keys_pressed, klee_pos, KLEE_MOVE_SPEED, BORDER_KLEE, WIDTH, HEIGHT): #klee movment
    if keys_pressed[pygame.K_a] and klee_pos.x - KLEE_MOVE_SPEED > 0: #move left
        klee_pos.x -= KLEE_MOVE_SPEED
    if keys_pressed[pygame.K_d] and klee_pos.x + KLEE_MOVE_SPEED + klee_pos.width < WIDTH: #move right
        klee_pos.x += KLEE_MOVE_SPEED
    if keys_pressed[pygame.K_w] and klee_pos.y - KLEE_MOVE_SPEED > BORDER_KLEE.y: #move up
        klee_pos.y -= KLEE_MOVE_SPEED
    if keys_pressed[pygame.K_s] and klee_pos.y + KLEE_MOVE_SPEED + klee_pos.height < HEIGHT: #move down
        klee_pos.y += KLEE_MOVE_SPEED

def bombs_movement(bombs, klee_pos, fishes1, fish_caught, explosion, explosion_pos, fishes2, BOMB_SPEED): #bomb movenet and interactions
    for bomb in bombs:
        bomb.y -= BOMB_SPEED                     
        for fish in fishes1:
            if fish.colliderect(bomb):
                explosion_pos[0] = bomb
                fishes1.remove(fish)
                fish_caught[0] += 1
                bombs.remove(bomb)
                explosion[0] = 60
        for fish2 in fishes2:
            if fish2.colliderect(bomb):
                explosion_pos[0] = bomb
                fishes2.remove(fish2)
                fish_caught[0] += 1
                for bomb2 in bombs:
                    if bomb2 == bomb:
                        bombs.remove(bomb)
                explosion[0] = 60

                
        if bomb.y < 0:
            bombs.remove(bomb)

def refil_bombs(BOMBS_LEFT, klee_pos, bomb_fill, bombs, BOMB_SPEED, MAX_BOMBS):
    for bomb_fill_pos in bomb_fill:
        if klee_pos.colliderect(bomb_fill_pos):
            BOMBS_LEFT[0] = MAX_BOMBS
            bomb_fill.remove(bomb_fill_pos)
            bombs.clear()
            
def bomb_fill_spawn(bomb_fill, bombs, BOMBS_LEFT, klee_pos):
    if len(bomb_fill) == 0 and (len(bombs) == 0 and BOMBS_LEFT[0] == 0): #spawn bomb refills
                bomb_fill_pos = pygame.Rect(random.randint(50, 1230), random.randint(410, 670), 50, 50)
                while bomb_fill_pos.colliderect(klee_pos): #make sure players dont get free reload
                    bomb_fill_pos = pygame.Rect(random.randint(50, 1230), random.randint(410, 670), 50, 50)
                bomb_fill.append(bomb_fill_pos)
