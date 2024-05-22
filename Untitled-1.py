from pygame import *


'''Важные переменные'''
mixer.init()
back = 'Pixilart - Sky.jpg'
win_width = 800
win_height = 700
window = display.set_mode((win_width, win_height))
background = transform.scale(image.load(back), (800, 700))

point1 = 0
point2 = 0
leftrocket = 'racket.png'
rightrocket = 'racket.png'
scoreline = 'scoreline.png'
bounce_sound = mixer.Sound('bounce.ogg')
lose_sound = mixer.Sound('lose.ogg')
right_will_get_point = False
left_will_get_point = False
game = True
finish = False

clock = time.Clock()
FPS = 120

'''Важные классы'''

#класс-родитель для других спрайтов
class GameSprite(sprite.Sprite):
    #конструктор класса
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
        #вызываем конструктор класса (Sprite):
        sprite.Sprite.__init__(self)


        #каждый спрайт должен хранить свойство image - изображение
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.speed = player_speed


    #каждый спрайт должен хранить свойство rect - прямоугольник, в который он вписан
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y


#метод, отрисовывающий героя на окне
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
        
class Player(GameSprite):    
#метод для управления спрайтом стрелками клавиатуры
    def update_l(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
           self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < win_height - 150:
            self.rect.y += self.speed
 #метод "выстрел" (используем место игрока, чтобы создать там пулю)
    def update_r(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
           self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < win_height- 150:
            self.rect.y += self.speed

class Scoreline(GameSprite):
    def update_move(self):
        self.rect.x += self.speed
        if self.rect.x < win_width - 250:
            self.speed *= -1
        if self.rect.x > win_width - 750:
            self.speed *= -1


left_rocket = Player(leftrocket, 50, 300, 90, 200, 9)
right_rocket = Player(rightrocket, 670, 300, 90, 200, 9)
ball = GameSprite('pixel tennis ball.png', 300, 300, 70, 70, 19)
scoreline_obj = Scoreline(scoreline, 300, 25, 200, 35, 3)


font.init()
font = font.Font(None, 35)
lose1 = font.render('PLAYER 1 LOSE!', True, (180, 0, 0))
lose2 = font.render('PLAYER 2 LOSE!', True, (180, 0, 0))
speed_x = 3
speed_y = 3

'''Игровой цикл'''

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
        
    if finish != True:
        window.blit(background, (0, 0))
        left_rocket.update_l()
        right_rocket.update_r()
        scoreline_obj.update_move()
        ball.rect.x += speed_x
        ball.rect.y += speed_y

        points1 = font.render('POINTS: '+ str(point1),  True, (255, 255, 255))
        window.blit(points1, (50, 650))

        points2 = font.render('POINTS: '+ str(point2),  True, (255, 255, 255))
        window.blit(points2, (600, 650))

        if sprite.collide_rect(left_rocket, ball):
            speed_x *= -1
            speed_y *= 1
            bounce_sound.play()
            left_will_get_point == True

        if sprite.collide_rect(right_rocket, ball):
            speed_x *= -1
            speed_y *= 1
            bounce_sound.play()
            right_will_get_point == True

        if sprite.collide_rect(scoreline_obj, ball) and right_will_get_point == True:
            speed_x *= -1 
            point2 += 1
        else:
            right_will_get_point == False

        if sprite.collide_rect(scoreline_obj, ball) and left_will_get_point == True:
            speed_x *= -1
            point1 += 1
        else:
            left_will_get_point == False

        if ball.rect.y > win_height-50 or ball.rect.y < 0:
            speed_y *= -1

        if ball.rect.x < 0:
            finish = True
            window.blit(lose1, (300, 325))
            lose_sound.play()

        if ball.rect.x > 725:
            finish = True
            window.blit(lose2, (300, 325))
            lose_sound.play()

    left_rocket.reset()
    right_rocket.reset()
    ball.reset()
    scoreline_obj.reset()
    
    
    display.update()
    clock.tick(FPS)
