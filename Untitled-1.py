from pygame import *


'''Важные переменные'''
back = (0, 97, 135)
win_width = 800
win_height = 700
window = display.set_mode((win_width, win_height))
window.fill(back)

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
        if keys[K_w] and self.rect.y > 5:
           self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < win_height:
            self.rect.y += self.speed

left_rocket = Player(leftrocket, 30, 200, 100, 250, 4)
right_rocket = Player(rightrocket, 30, 200, 100, 250, 4)
ball = GameSprite('ball.png', 200, 200, 100, 100, 4)

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

    left_rocket.reset()
    right_rocket.reset()
    ball.reset()


    display.update()
    clock.tick(FPS)
