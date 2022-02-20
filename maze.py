from pygame import *

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (65,65))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
class Player(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (65,65))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
    def update(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_w] and self.rect.y > 50:
            self.rect.y -= self.speed
        if keys_pressed[K_s] and self.rect.y < 370:
            self.rect.y += self.speed
        if keys_pressed[K_a] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys_pressed[K_d] and self.rect.x < 640:
            self.rect.x += self.speed 
class Enemy(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed, direction):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (65,65))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
        self.direction = direction
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
    def update(self):
        
        if self.direction == 'left' and self.rect.x > 470:
            self.rect.x -= self.speed
            
        if self.rect.x == 470 or self.rect.x < 470:
            self.direction = 'right'
        if self.direction == 'right':
            self.rect.x += self.speed
            
        if self.rect.x == 650:
            self.direction = 'left'
        
        
class Wall(sprite.Sprite):
    def __init__(self, color_1, color_2, color_3, wall_x, wall_y,wall_width, wall_height):
        super().__init__()
        self.color_1 = color_1
        self.color_2 = color_2
        self.color_3 = color_3
        self.wall_width = wall_width
        self.wall_height = wall_height
        self.image = Surface((self.wall_width, self.wall_height))
        self.image.fill((color_1, color_2, color_3))
        self.rect = self.image.get_rect()
        self.rect.x = wall_x
        self.rect.y = wall_y
    def draw_wall(self):
        window.blit(self.image, (self.rect.x, self.rect.y))    
        
#создай окно игры
window = display.set_mode((700, 500))
display.set_caption("Maze")
clock = time.Clock()
FPS = 60
background = transform.scale(image.load("background.jpg"), (700, 500))
treasure = GameSprite('treasure.png', 500, 370,1)
player = Player('hero.png', 5, 420, 4)
enemy = Enemy('cyborg.png', 620 , 280, 2,'left')
wall1 = Wall(94, 164, 0, 10, 50,650,5)
wall2 = Wall(94, 164, 0, 10, 50,5,320)
wall3 = Wall(94, 164, 0, 150, 305,5,330)
wall4 = Wall(94, 164, 0, 125, 210,250,5)
wall5 = Wall(94, 164, 0, 300, 140,5,190)
wall6 = Wall(94, 164, 0, 125, 300,250,5)
wall7 = Wall(94, 164, 0, 300, 160,125,5)
wall8 = Wall(94, 164, 0, 400, 160,5,125)
wall9 = Wall(94, 164, 0, 320, 265,125,5)
wall10 = Wall(94, 164, 0, 425, 250,5,140)
font.init()
font = font.SysFont('Arial',70)
win = font.render('YOU WIN', True, (255, 215, 0))
mixer.init()
kick = mixer.Sound('kick.ogg')
money = mixer.Sound('money.ogg')
#mixer.music.load('jungles.ogg')
#mixer.music.play()
game = True
finish = False
while game:
    
    for e in event.get():
        if e.type == QUIT:
            game = False

    
    if finish != True:
        window.blit(background, (0,0))
        player.reset()
        enemy.reset()
        treasure.reset()
        wall1.draw_wall()
        wall2.draw_wall()
        wall3.draw_wall()
        wall4.draw_wall()
        wall5.draw_wall()
        wall6.draw_wall()
        wall7.draw_wall()
        wall8.draw_wall()
        wall9.draw_wall()
        wall10.draw_wall()
        player.update()
        enemy.update()
        if sprite.collide_rect(player, treasure):
            finish = True
            money.play()
            print('Player is collide ')
            win = font.render('YOU WIN', True, (255, 215, 0))
            window.blit(win, (250,200))
            
        if sprite.collide_rect(player, enemy) or sprite.collide_rect(player, wall1) or sprite.collide_rect(player, wall2) or sprite.collide_rect(player, wall3) or sprite.collide_rect(player, wall4) or sprite.collide_rect(player, wall5) or sprite.collide_rect(player, wall6) or sprite.collide_rect(player, wall7) or sprite.collide_rect(player, wall8) or sprite.collide_rect(player, wall9) or sprite.collide_rect(player, wall10):
            finish = True
            kick.play()
            lose = font.render('YOU LOSE', True, (255,0,0))
            window.blit(lose, (250,200))
           
    display.update()
    clock.tick(FPS)