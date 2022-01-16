from pickle import TRUE
import pygame
import os
import random
from lib import fish
from lib import kb

WIDTH, HEIGHT = 1280, 720
WIN = pygame.display.set_mode((WIDTH, HEIGHT)) #set window size
pygame.display.set_caption("Klee Fishing Mania!") #set window name

FPS = 60 #fps variable
KLEE_MOVE_SPEED = 4 #move speed pixle/s
BOMB_SPEED = 5 #move speed of bomb
MAX_BOMBS = 3 #max number of bombs
MIN_FISH_SPEED = 3 #starting fish speed
FISH_SPEED = [MIN_FISH_SPEED]
BORDER_KLEE = pygame.Rect(0, HEIGHT//2 - 5, WIDTH, 10) #movement border
MAX_FISH = 3 #Max no of fish at one time
TIMELIMIT = 120000 #time limit in ticks, 1s = 1000tick

FISH_HIT = pygame.USEREVENT + 1 #user events
RESTART_GAME = pygame.USEREVENT + 1

pygame.font.init()
font1 = pygame.font.Font(os.path.join('assets', 'fonts', 'zh-cn.ttf'), 50) #load font
font2 = pygame.font.Font(os.path.join('assets', 'fonts', 'zh-cn.ttf'), 20)

KLEE_IMAGE = pygame.image.load(os.path.join('assets', 'klee2.png')) #Import & resize Images
KLEE = pygame.transform.scale(KLEE_IMAGE, (100, 100))
BOMBREFIL_IMAGE = pygame.image.load(os.path.join('assets', 'bomb.png'))
BOMBREFIL = pygame.transform.scale(BOMBREFIL_IMAGE, (50, 50))
FISH_IMAGE = pygame.image.load(os.path.join('assets', 'fish.png'))
FISH = pygame.transform.scale(FISH_IMAGE, (50,50))
FISH2_IMAGE = pygame.image.load(os.path.join('assets', 'fish2.png'))
FISH2 = pygame.transform.scale(FISH2_IMAGE, (50,50))
SMALLBOMB_IMAGE = pygame.image.load(os.path.join('assets', 'small bomb.png'))
SMALLBOMB = pygame.transform.scale(SMALLBOMB_IMAGE, (20, 20))
BACKGROUND_BEACH = pygame.image.load(os.path.join('assets', 'bg.png'))
STARTSCREEN_IMAGE = pygame.image.load(os.path.join('assets', 'title.png'))
STARTSCREEN = pygame.transform.scale(STARTSCREEN_IMAGE, (WIDTH, HEIGHT))
BOMBBAR_EMPTY_IMAGE = pygame.image.load(os.path.join('assets', 'bombbar empty.png'))
BOMBBAR_EMPTY = pygame.transform.scale(BOMBBAR_EMPTY_IMAGE, (100, 100))
BOMBBAR_IMAGE = pygame.image.load(os.path.join('assets', 'bomb bar.png'))
BOMBBAR = pygame.transform.scale(BOMBBAR_IMAGE, (100, 100))
EXPLOSION_IMAGE = pygame.image.load(os.path.join('assets', 'explosion.png'))
EXPLOSION = pygame.transform.scale(EXPLOSION_IMAGE, (70, 70))
FISHSTACK_IMAGE = pygame.image.load(os.path.join('assets', 'fish stack.png'))
FISHSTACK = pygame.transform.scale(FISHSTACK_IMAGE, (250, 250))
STARTBUTTON_IMAGE = pygame.image.load(os.path.join('assets', 'buttons', 'start_button.png'))
STARTBUTTON = pygame.transform.scale(STARTBUTTON_IMAGE, (213, 101))
QUITBUTTON_IMAGE = pygame.image.load(os.path.join('assets', 'buttons', 'quit_button.png'))
QUITBUTTON = pygame.transform.scale(QUITBUTTON_IMAGE, (213, 101))
AGAINBUTTON_IMAGE = pygame.image.load(os.path.join('assets', 'buttons', 'again_button.png'))
AGAINBUTTON = pygame.transform.scale(AGAINBUTTON_IMAGE, (213, 101))
CONTROLS_IMAGE = pygame.image.load(os.path.join('assets', 'controls.png'))
CONTROLS = pygame.transform.scale(CONTROLS_IMAGE, (WIDTH, HEIGHT))
CLOCK1_IMAGE = pygame.image.load(os.path.join('assets', 'clock', 'clock1.png'))
CLOCK1 = pygame.transform.scale(CLOCK1_IMAGE, (100, 122))
CLOCK2_IMAGE = pygame.image.load(os.path.join('assets', 'clock', 'clock2.png'))
CLOCK2 = pygame.transform.scale(CLOCK2_IMAGE, (100, 122))
CLOCK3_IMAGE = pygame.image.load(os.path.join('assets', 'clock', 'clock3.png'))
CLOCK3 = pygame.transform.scale(CLOCK3_IMAGE, (100, 122))
CLOCK4_IMAGE = pygame.image.load(os.path.join('assets', 'clock', 'clock4.png'))
CLOCK4 = pygame.transform.scale(CLOCK4_IMAGE, (100, 122))
CLOCK5_IMAGE = pygame.image.load(os.path.join('assets', 'clock', 'clock5.png'))
CLOCK5 = pygame.transform.scale(CLOCK5_IMAGE, (100, 122))
CLOCK6_IMAGE = pygame.image.load(os.path.join('assets', 'clock', 'clock6.png'))
CLOCK6 = pygame.transform.scale(CLOCK6_IMAGE, (100, 122))
BACKGROUND_END_IMAGE = pygame.image.load(os.path.join('assets', 'bg end.png'))
BACKGROUND_END = pygame.transform.scale(BACKGROUND_END_IMAGE, (WIDTH, HEIGHT))

class button(): #class for buttons
    def __init__(self, x, y, image):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.clicked = False

    def draw(self): #draw and click detection mouse
        action = False
        pos = pygame.mouse.get_pos() 
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                action = True

        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False

        WIN.blit(self.image, (self.rect.x, self.rect.y))
        return action

start_button = button(377, 540, STARTBUTTON) #button instances
quit_button = button(690, 540, QUITBUTTON)
again_button = button(177, 600, AGAINBUTTON)
quit_button2 = button(490, 600, QUITBUTTON)

def start_screen():
    sub = font2.render("Game By Rein", False, (255, 150, 150))
    starting = True
    started = False
    clock = pygame.time.Clock()
    pygame.display.update()
    while starting:
        WIN.blit(STARTSCREEN, (0,0)) #display Start screen text & buttons
        WIN.blit(sub, (570, 690))
        if start_button.draw():
            starting = False
            started = True
        if quit_button.draw():
            pygame.quit()
        clock.tick(60)
        return started #returns started to start game

def draw_window_game(klee_pos, bombs, fishes1, bomb_fill, fish_caught, BOMBS_LEFT, explosion, explosion_pos, fishes2, show_controls, time_started): #draw images in window
    WIN.fill((255,255,255))
    WIN.blit(BACKGROUND_BEACH, (0, 0)) #disp background and fish stack
    if fish_caught[0] > 10:
        WIN.blit(FISHSTACK, (-50, 500))
    if fish_caught[0] > 20:
        WIN.blit(FISHSTACK, (0, 500))
    if fish_caught[0] > 30:
        WIN.blit(FISHSTACK, (50, 500))
    if fish_caught[0] > 40:
        WIN.blit(FISHSTACK, (100, 500))
    if fish_caught[0] > 50:
        WIN.blit(FISHSTACK, (150, 500))
    if fish_caught[0] > 60:
        WIN.blit(FISHSTACK, (200, 500))
    if fish_caught[0] > 70:
        WIN.blit(FISHSTACK, (250, 500))
    if fish_caught[0] > 80:
        WIN.blit(FISHSTACK, (300, 500))
    for bomb in bombs: #disp bomb & fishes
        WIN.blit(SMALLBOMB, (bomb.x, bomb.y))
    for fish in fishes1: #display fish going left
        WIN.blit(FISH, (fish.x, fish.y))
    for fish2 in fishes2: #display fish going right
        WIN.blit(FISH2, (fish2.x, fish2.y))
    for bomb_fill_pos in bomb_fill:
        WIN.blit(BOMBREFIL, (bomb_fill_pos.x, bomb_fill_pos.y))
    WIN.blit(KLEE, (klee_pos.x, klee_pos.y)) #disp klee
    WIN.blit(BOMBBAR_EMPTY, (1180,5)) #disp empty bomb bar
    WIN.blit(BOMBBAR_EMPTY, (1100,5))
    WIN.blit(BOMBBAR_EMPTY, (1020,5))
    if explosion[0] > 0: #explosion
        explosion[0] -= 1
        exploc = explosion_pos[0]
        WIN.blit(EXPLOSION, (exploc.x - 35, exploc.y - 35))
    if BOMBS_LEFT[0] == 3: #bomb counter
        WIN.blit(BOMBBAR, (1180,5))
        WIN.blit(BOMBBAR, (1100,5))
        WIN.blit(BOMBBAR, (1020,5))
    elif BOMBS_LEFT[0] == 2:
        WIN.blit(BOMBBAR, (1100,5))
        WIN.blit(BOMBBAR, (1020,5))
    elif BOMBS_LEFT[0] == 1:
        WIN.blit(BOMBBAR, (1020,5))
    if (pygame.time.get_ticks() - time_started) < ((TIMELIMIT//6)): #draw time
        WIN.blit(CLOCK1, (10, 10))
    elif (pygame.time.get_ticks() - time_started) < ((TIMELIMIT//6)*2):
        WIN.blit(CLOCK2, (10, 10))
    elif (pygame.time.get_ticks() - time_started) < ((TIMELIMIT//6)*3):
        WIN.blit(CLOCK3, (10, 10))
    elif (pygame.time.get_ticks() - time_started) < ((TIMELIMIT//6)*4):
        WIN.blit(CLOCK4, (10, 10))
    elif (pygame.time.get_ticks() - time_started) < ((TIMELIMIT//6)*5):
        WIN.blit(CLOCK5, (10, 10))
    elif (pygame.time.get_ticks() - time_started) < TIMELIMIT:
        WIN.blit(CLOCK6, (10, 10))
    if show_controls == True:
        WIN.blit(CONTROLS, (0, 0))
    pygame.display.update()


def endscreen(fish_caught):
    sub = font2.render("Game By Rein", False, (255, 150, 150))
    clock = pygame.time.Clock()
    fishc = "Fishes Caught: " + str(fish_caught[0])
    caught = font1.render(fishc, False, (76, 58, 38))
    ended = True
    pygame.display.update()
    while ended:
        WIN.blit(BACKGROUND_END, (0,0))
        WIN.blit(caught, (150, 360))
        WIN.blit(sub, (570, 690))
        if again_button.draw():
            main()
        if quit_button2.draw():
            pygame.quit()
        clock.tick(60)
        return ended
    

def main():
    klee_pos = pygame.Rect(640, 540, 100, 100) #klee position starting
    klee_pos1 = pygame.Rect(640, 540, 100, 100)

    bombs = []
    bomb_fill = []
    BOMBS_LEFT = [MAX_BOMBS]
    fishes1 = []
    fishes2 = []
    fish_caught = [0]
    explosion = [0]
    explosion_pos = [0]
    fish_last = [0]
    FISH_SPEED = [MIN_FISH_SPEED]
    time_started = 0
    clock = pygame.time.Clock()
    run = True
    started1 = False
    started2 = False
    controls = False
    show_controls = True
    
    pygame.mixer.init()
    pygame.mixer.music.load(os.path.join('assets', 'music', 'bgm1.mp3'))
    pygame.mixer.music.play(loops=100)

    while run: #Loop to check if user quit
        if started1 == False:
            if start_screen():
                started1 = True
                started2 = True
        if started2 == False and started1 == True:
            endscreen(fish_caught)
        clock.tick(FPS) #set max fps
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN and controls == True:
                if event.key == pygame.K_SPACE and len(bombs) < MAX_BOMBS and int(BOMBS_LEFT[0]) > 0: #detect key press & check if max bombs
                    bomb = pygame.Rect(klee_pos.x + klee_pos.width - 50, klee_pos.y + klee_pos.height//2 - 5, 20, 20)
                    bombs.append(bomb)
                    BOMBS_LEFT[0] -= 1 
                    controls = True     

        if controls == False: #show controls screen
            if klee_pos != klee_pos1:
                show_controls = False
                controls = True
                time_started = pygame.time.get_ticks()

        if started2 == True:
            if controls == True: #fixed bug where staying in controls screen long enough crashes game
                if (pygame.time.get_ticks() - time_started) > TIMELIMIT:
                    started2 = False

            keys_pressed = pygame.key.get_pressed() #detect key press

            kb.klee_movement(keys_pressed, klee_pos, KLEE_MOVE_SPEED, BORDER_KLEE, WIDTH, HEIGHT) #klee movement
            kb.bombs_movement(bombs, klee_pos, fishes1, fish_caught, explosion, explosion_pos, fishes2, BOMB_SPEED) #bomb movement and interaction with fish
            kb.refil_bombs(BOMBS_LEFT, klee_pos, bomb_fill, bombs, BOMB_SPEED, MAX_BOMBS) #bomb refil
            kb.bomb_fill_spawn(bomb_fill, bombs, BOMBS_LEFT, klee_pos) #bomb refil spawn
            fish.fish_spawn(fishes1, fishes2, MAX_FISH) #spawns fish
            fish.fish_swim_left(fishes1, FISH_SPEED) #make fish swim
            fish.fish_swim_right(fishes2, FISH_SPEED)
            fish.fish_dissapear_prevention(fishes1) #fixed bug where fish were disappearing
            fish.fish_dissapear_prevention2(fishes2)
            fish.fish_collison_prevention(fishes1, fishes2)#fix bug where collision of fish crashes game
            fish.fish_speed_up(fish_caught, FISH_SPEED, fish_last) #increasing difficulty

            draw_window_game(klee_pos, bombs, fishes1, bomb_fill, fish_caught, BOMBS_LEFT, explosion, explosion_pos, fishes2, show_controls, time_started)

    pygame.quit()



if __name__ == "__main__": #only run when file is run, dont run when import
    main()
            