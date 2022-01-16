import random
import pygame

def fish_swim_left(fishes1, FISH_SPEED): #fish swim left
    for fish in fishes1:
        fish.x -= FISH_SPEED[0]
        if fish.x == 0:
            fish.x = 1280

def fish_swim_right(fishes2, FISH_SPEED): #fish swim right
    for fish in fishes2:
        fish.x += FISH_SPEED[0]
        if fish.x == 1280:
            fish.x = 0

def fish_dissapear_prevention(fishes1):
    for fish in fishes1:
        if fish.x < 0:
            fishes1.remove(fish)

def fish_dissapear_prevention2(fishes2):
    for fish2 in fishes2:
        if fish2.x > 1280:
            fishes2.remove(fish2)

def fish_collison_prevention(fishes1, fishes2):#fix bug where collision of fish crashes game
    for fish1 in fishes1:
        for fish2 in fishes2:
            if fish1.colliderect(fish2):
                roll = random.randint(1,2)
                if roll == 1:
                    fishes1.remove(fish1)
                else:
                    fishes2.remove(fish2)

def fish_speed_up(fish_caught, FISH_SPEED, fish_last):
    if (fish_caught[0] - fish_last[0]) == 10:
        FISH_SPEED[0] += 1
        fish_last[0] = fish_caught[0]

def fish_spawn(fishes1, fishes2, MAX_FISH):
    if len(fishes1) < MAX_FISH:
        fish_posi = pygame.Rect(random.randint(961, 1229), random.randint(50, 310), 50, 50) #fish starting position
        for collide in fishes1:
            if collide.colliderect(fish_posi): #fixed bug where when 2 fished killed at once game crashed
                fishes1.remove(collide)
        fishes1.append(fish_posi)
    if len(fishes2) < MAX_FISH:
        fish_posi2 = pygame.Rect(random.randint(51, 319), random.randint(50, 310), 50, 50) #fish starting position
        for collide in fishes2:
            if collide.colliderect(fish_posi2): #fixed bug where when 2 fished killed at once game crashed
                fishes2.remove(collide)
        fishes2.append(fish_posi2)
