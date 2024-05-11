from pygame import *


'''Важные переменные'''
back = (0, 97, 135)
win_width = 800
win_height = 700
window = display.set_mode((win_width, win_height))
window.fill(back)

point1 = 0
point2 = 0
leftrocket = 'left_rocket.png'
rightrocket = 'right_rocket.png'
game = True
finish = False

clock = time.Clock()
FPS = 30

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
        if keys[K_s] and self.rect.y < win_height:
            self.rect.y += self.speed
 #метод "выстрел" (используем место игрока, чтобы создать там пулю)
    def update_r(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
           self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < win_height:
            self.rect.y += self.speed

left_rocket = Player(leftrocket, 30, 300, 100, 150, 9)
right_rocket = Player(rightrocket, 670, 300, 100, 150, 9)
ball = GameSprite('ball.png', 300, 300, 50, 50, 19)

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
        window.fill(back)
        left_rocket.update_l()
        right_rocket.update_r()
        ball.rect.x += speed_x
        ball.rect.y += speed_y

        points1 = font.render('POINTS: '+ str(point1),  True, (0, 255, 0))
        window.blit(points1, (200, 10))

        points2 = font.render('POINTS: '+ str(point2),  True, (0, 255, 0))
        window.blit(points2, (500, 10))

        if sprite.collide_rect(left_rocket, ball):
            speed_x *= -1
            speed_y *= 1
            point1 +=1

        if sprite.collide_rect(right_rocket, ball):
            speed_x *= -1
            speed_y *= 1
            point2 +=1

        if ball.rect.y > win_height-50 or ball.rect.y < 0:
            speed_y *= -1

        if ball.rect.x < 0:
            finish = True
            window.blit(lose1, (300, 325))

        if ball.rect.x > 700:
            finish = True
            window.blit(lose2, (300, 325))

    left_rocket.reset()
    right_rocket.reset()
    ball.reset()
    
    
    display.update()
    clock.tick(FPS)
