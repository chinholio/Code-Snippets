# PyGame Tutorial from Youtube: Clear Code channel https://www.youtube.com/watch?v=AY9MnQ4x3zk&t=6960s

# import required modules. 
import pygame
from sys import exit
from random import randint, choice

# Class of player sprite
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        player_walk_1 = pygame.image.load('Python/PyGame Runner/graphics/player/player_walk_1.png').convert_alpha()
        player_walk_2 = pygame.image.load('Python/PyGame Runner/graphics/player/player_walk_2.png').convert_alpha()
        self.player_walk = [player_walk_1,player_walk_2]
        self.player_index = 0
        self.player_jump = pygame.image.load('Python/PyGame Runner/graphics/player/jump.png').convert_alpha()

        self.image = self.player_walk[self.player_index]
        self.rect = self.image.get_rect(midbottom = (80,300))
        self.gravity = 0

        self.jump_sound = pygame.mixer.Sound('Python/PyGame Runner/audio/jump.mp3')
        self.jump_sound.set_volume(0.3)
    
    def player_input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE] and self.rect.bottom == 300:
            self.gravity = -20
            self.jump_sound.play()
    
    def apply_gravity(self):
        self.gravity += 1
        self.rect.y += self.gravity
        if self.rect.bottom >= 300:
            self.rect.bottom = 300

    def animation_states(self):
        if self.rect.bottom  < 300:
            self.image = self.player_jump
        else:
            self.player_index += 0.1
            if self.player_index >= len(self.player_walk):self.player_index = 0
            self.player_surf = self.player_walk[int(self.player_index)]

    def update(self):
        self.player_input()
        self.apply_gravity()
        self.animation_states()

# Class of in game obstacles
class Obstacles(pygame.sprite.Sprite):
    def __init__(self,type):
        super().__init__()
        if type == 'snail':
            snail_frame_1 = pygame.image.load('Python/PyGame Runner/graphics/snail/snail1.png').convert_alpha()
            snail_frame_2 = pygame.image.load('Python/PyGame Runner/graphics/snail/snail2.png').convert_alpha()
            self.frames = [snail_frame_1,snail_frame_2]
            y_pos = 300
        else:
            fly_frame_1 = pygame.image.load('Python/PyGame Runner/graphics/Fly/Fly1.png').convert_alpha()
            fly_frame_2 = pygame.image.load('Python/PyGame Runner/graphics/Fly/Fly2.png').convert_alpha()
            self.frames = [fly_frame_1,fly_frame_2]
            y_pos = 210

        self.animation_index = 0
        self.image = self.frames[self.animation_index]
        self.rect = self.image.get_rect(midbottom = (randint(900,1100),y_pos))

    def animation_state(self):
        self.animation_index += 0.1
        if self.animation_index >= len(self.frames): self.animation_index = 0
        self.image = self.frames[int(self.animation_index)]

    def update(self):
        self.animation_state()
        self.rect.x -= 6
        self.destroy()

    def destroy(self):
        if self.rect.x <= -100:
            self.kill()

# Function to display score
def display_score():
    current_time = int((pygame.time.get_ticks() - start_time) / 1000)
    score_surf = test_font.render(f'Score: {current_time}', False, (64,64,64))
    score_rect = score_surf.get_rect(center = (400,50))
    screen.blit(score_surf,score_rect)
    return current_time

# Collision function
def collision_sprite():
    if pygame.sprite.spritecollide(player.sprite,obstacles,False):
        obstacles.empty()
        return False
    else:
        return True

# starts pygame
pygame.init()

# Sets initial details
screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption('Runner')
clock = pygame.time.Clock()
test_font = pygame.font.Font('Python/PyGame Runner/font/Pixeltype.ttf', 50)
game_active = False
start_time = 0
score = 0
background_sound = pygame.mixer.Sound('Python/PyGame Runner/audio/music.wav')
background_sound.set_volume(0.4)
background_sound.play(loops = -1)


# Groups
player = pygame.sprite.GroupSingle()
player.add(Player())

obstacles = pygame.sprite.Group()
obstacles.add(Obstacles(type))

sky_surface = pygame.image.load('Python/PyGame Runner/graphics/Sky.png').convert()
ground_surface = pygame.image.load('Python/PyGame Runner/graphics/ground.png').convert()

obstacle_rect_list = []

# Intro screen player
player_stand = pygame.image.load('Python/PyGame Runner/graphics/player/player_stand.png').convert_alpha()
player_stand = pygame.transform.rotozoom(player_stand,0,2)
player_stand_rect = player_stand.get_rect(center = (400,200))

# Intro Screen Text
title_surf = test_font.render(f'Pixel Runner', False, (111,196,169))
title_rect = title_surf.get_rect(center = (400,80))

game_message = test_font.render(f'Press Space to Run.', False, (111,196,169))
game_message_rect = game_message.get_rect(center = (400,340))


# Timers
obstacle_timer = pygame.USEREVENT + 1
pygame.time.set_timer(obstacle_timer,1500)

snail_animation_timer = pygame.USEREVENT + 2
pygame.time.set_timer(snail_animation_timer,500)

fly_animation_timer = pygame.USEREVENT + 2
pygame.time.set_timer(fly_animation_timer,200)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        
        if game_active:
            if event.type == obstacle_timer:
                obstacles.add(Obstacles(choice(['snail','snail','snail','fly'])))
        else:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                game_active = True
                start_time = pygame.time.get_ticks()


    if game_active:
        screen.blit(sky_surface,(0,0))
        screen.blit(ground_surface,(0,300))
        score = display_score()

        player.draw(screen)
        player.update()

        obstacles.draw(screen)
        obstacles.update()

        game_active = collision_sprite()

    else:
        screen.fill((94,129,162))
        screen.blit(player_stand,player_stand_rect)
        obstacle_rect_list.clear()
        player_stand_rect.midbottom = (400, 300)
        player_gravity = 0

        score_message = test_font.render(f'Your score: {score}', False, (111,196,169))
        score_message_rect = score_message.get_rect(center = (400,330))
        screen.blit(title_surf,title_rect)

        if score == 0:
            screen.blit(game_message,game_message_rect)
        else:
            screen.blit(score_message,score_message_rect)

    # draw all elements
    # update everything
    pygame.display.update()

    # Sets maximum frame rate
    clock.tick(60)