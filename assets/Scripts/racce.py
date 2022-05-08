##-Импорт библиотек-##
import os, sys, platform, pygame, random, subprocess
import db_control as dc


##-------------------------------Подключение к данным-------------------------------##

##-Подключение к БД-##
dc.conect_db('DB')

##-Переменные-##
project_path = os.getcwd()
score = 0
score_chek = 10
speed_player = 6
player_lives = 100
player_petrol = 100
tanks_list = ['player_tank']

if platform.system() == 'Windows': divider = '\\'
elif platform.system() == 'Linux': divider = '/'


##-Подключение к JSON-##
if dc.select('INFO.nf', 'name') == False:
    if platform.system() == 'Windows': os.system('start menu.py')
    elif platform.system() == 'Linux': subprocess.call(f'{project_path}{divider}menu.py')
    sys.exit()

player_nickname = dc.select('INFO.nf', 'name')
player_skin = dc.select('INFO.nf', 'active_skin')

##-Настройка цветов-##
BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (255,0,0)
GREEN = (0,255,0)

##-Настройки окружения-##
WIDTH = 705
HEIGHT = 480
FPS = 60

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock_fps = pygame.time.Clock()


##-------------------------------Отрисовка текста-------------------------------##

font_name = pygame.font.match_font('None')

##-Дефолтный текст-##
def draw_text(surf, text, size, x, y):

    font = pygame.font.Font(font_name,size)
    text_surface = font.render(text, True, WHITE)

    text_rect = text_surface.get_rect()
    text_rect.midtop = (x, y)

    surf.blit(text_surface, text_rect)

##-Текст "Конец игра"-##
def draw_game_over_text(surf, text, size, x, y):

    font = pygame.font.Font(font_name,size)
    text_surface = font.render(text, True, RED)

    text_rect = text_surface.get_rect()
    text_rect.midtop = (x, y)

    surf.blit(text_surface, text_rect)


#-------------------------------Создание объектов-------------------------------#

##-спавн противника на 2 левых полосах-##
def mob_up_spawn():
    mob = Mob_up()

    mob_up_chek.add(mob)
    all_sprites.add(mob)

##-спавн противника на 2 правых полосах-##
def mob_down_spawn():
    mob = Mob_down()

    mob_down_chek.add(mob)
    all_sprites.add(mob)

##-Создание полосы здоровья-##
def live_strip_update():
    live = Live()

    livs.add(live)
    all_sprites.add(live)

##-Создание полосы бензина-##
def petrol_strip_update():
    global player_petrol
    if player_petrol > 100: player_petrol = 100

    petrol_strip = Petrol_Strip()

    petrol_strip_chek.add(petrol_strip)
    all_sprites.add(petrol_strip)

##-Создание монетки-##
def coin_spawn():
    coin = Coin()

    coins.add(coin)
    all_sprites.add(coin)

##-Создание канистры бензина-##
def petrol_spawn():
    petrol_bak = Petrol_Bak()

    petrols.add(petrol_bak)
    all_sprites.add(petrol_bak)

##-Создание ремонт комплекта-##
def repair_kit_spawn():
    global player_lives
    if player_lives > 100: player_lives = 100

    repair_kit = Repair_Kit()

    repair_kits.add(repair_kit)
    all_sprites.add(repair_kit)

##-Отрисовка стен-##
def walls():
    lin_r = Line_Right()
    lin_l = Line_Left()

    line_left.add(lin_r)
    line_right.add(lin_l)
    all_sprites.add(lin_r)
    all_sprites.add(lin_l)


#-------------------------------Класы-------------------------------#

##-Боковые линии-##
class Line_Right(pygame.sprite.Sprite):

    def __init__(self):

        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.transform.scale(line_right_skin, (10,480))
        self.image.set_colorkey(BLACK)

        self.rect = self.image.get_rect()
        self.rect.center =  (WIDTH - 474, HEIGHT / 2)

class Line_Left(pygame.sprite.Sprite):

    def __init__(self):

        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.transform.scale(line_left_skin, (10,480))
        self.image.set_colorkey(BLACK)

        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH - 150, HEIGHT / 2)

##-Ремонт комплект-##
class Repair_Kit(pygame.sprite.Sprite):

    def __init__(self):

        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.transform.scale(repair_kit_skin, (45,55))
        self.image.set_colorkey(BLACK)

        self.rect = self.image.get_rect()

        random_r_c = random.randint(1,4)
        if random_r_c == 4: self.rect.center = (WIDTH - 350,HEIGHT - 480)
        elif random_r_c == 3: self.rect.center = (WIDTH - 440, HEIGHT - 480)
        elif random_r_c == 2: self.rect.center = (WIDTH - 190,HEIGHT - 480)
        elif random_r_c == 1: self.rect.center = (WIDTH - 270, HEIGHT - 480)

        self.speedx = 4

    def update(self):
        self.rect.y += self.speedx
        if self.rect.top > HEIGHT: self.kill()

##-Канистра бензина-## 
class Petrol_Bak(pygame.sprite.Sprite):

    def __init__(self):

        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.transform.scale(petrol_bak, (45,55))
        self.image.set_colorkey(BLACK)

        self.rect = self.image.get_rect()

        random_petrol = random.randint(1,4)
        if random_petrol == 4: self.rect.center = (WIDTH - 350,HEIGHT - 480)
        elif random_petrol == 3: self.rect.center = (WIDTH - 440, HEIGHT - 480)
        elif random_petrol == 2: self.rect.center = (WIDTH - 190,HEIGHT - 480)
        elif random_petrol == 1: self.rect.center = (WIDTH - 270, HEIGHT - 480)

        self.speedx = 4

    def update(self):

        self.rect.y += self.speedx
        if self.rect.top > HEIGHT: self.kill()

##-Монетка-##
class Coin(pygame.sprite.Sprite):

    def __init__(self):

        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.transform.scale(coin_skin, (50,50))
        self.image.set_colorkey(BLACK)

        self.rect = self.image.get_rect()

        random_r_c = random.randint(1,4)

        if random_r_c == 4: self.rect.center = (WIDTH - 350,HEIGHT - 480)
        elif random_r_c == 3: self.rect.center = (WIDTH - 440, HEIGHT - 480)
        elif random_r_c == 2: self.rect.center = (WIDTH - 190,HEIGHT - 480)
        elif random_r_c == 1: self.rect.center = (WIDTH - 270, HEIGHT - 480)

        self.speedx = 4

    def update(self):

        self.rect.y += self.speedx
        if self.rect.top > HEIGHT: self.kill()

##-Показатель бензина-##
class Petrol_Strip(pygame.sprite.Sprite):

    def __init__(self):

        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.Surface((20, 1)) if player_petrol <= 0 else pygame.Surface((20, player_petrol))
        self.image.fill(RED)

        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH - 95,HEIGHT - 75) 

    def update(self): self.kill(), petrol_strip_update()

##-Показатель hp-##
class Live(pygame.sprite.Sprite):

    def __init__(self):

        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.Surface((20, 1)) if player_lives <= 10 else pygame.Surface((20, player_lives))
        self.image.fill(GREEN)

        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH - 40,HEIGHT - 75) 

    def update(self):
        global live_update

        if live_update == True: live_update = False, self.kill(), live_strip_update()

##-Противники на 2 левых дорогах-##
class Mob_down(pygame.sprite.Sprite):

    def __init__(self):

        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.transform.scale(mob_skin_down, (45, 55))
        self.image.set_colorkey(BLACK)

        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH - 350,HEIGHT - 480) if random.randint(1,2) == 1 else (WIDTH - 440, HEIGHT - 480)

        speed_mob2 = speed_player + 4
        self.speedy = speed_mob2

    def update(self):
        global score, speed_mob2, score_chek, speed_player

        if self.rect.top > HEIGHT:

            speed_player += 0.1
            self.kill()

            score += 10

            mob_down_spawn()
        self.rect.y += self.speedy

        if game_over == True: self.kill()

##-Противники на 2 правых дорогах-##
class Mob_up(pygame.sprite.Sprite):

    def __init__(self):

        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.transform.scale(mob_skin_up, (45, 55))
        self.image.set_colorkey(BLACK)

        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH - 190,HEIGHT - 480) if random.randint(1,2) == 1 else (WIDTH - 270, HEIGHT - 480)

        self.speedy = speed_player

    def update(self):
        global score, speed_player, score_chek

        if self.rect.top > HEIGHT:

            speed_player += 0.1
            self.kill()

            score += 10

            mob_up_spawn()
        self.rect.y += self.speedy

        if game_over == True: self.kill()

##-Машинка-##
class Car(pygame.sprite.Sprite):

    def __init__(self):

        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.transform.scale(photo_player, (73, 154)) if player_skin in tanks_list else pygame.transform.scale(photo_player, (45,55))
        self.image.set_colorkey(BLACK)

        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH / 2,HEIGHT - 90) if player_skin in tanks_list else (WIDTH / 2,HEIGHT - 60)
        
        self.speedx = 0
        self.shoot_delay = 250
        self.last_shot = pygame.time.get_ticks()

    def update(self):
        global running, player_lives, live_update

        self.speedx = 0

        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_c]:
            player_lives = 100
            live_update = True

        if keystate[pygame.K_RIGHT] or keystate[pygame.K_d]:
            self.speedx = 10
            self.image = pygame.transform.scale(player_right, (73, 154)) if player_skin in tanks_list else pygame.transform.scale(player_right, (45,55))
        else:
            self.image = pygame.transform.scale(photo_player, (73, 154)) if player_skin in tanks_list else pygame.transform.scale(photo_player, (45,55))
        
        if keystate[pygame.K_LEFT] or keystate[pygame.K_a]:
            self.speedx = -10
            self.image = pygame.transform.scale(player_left, (73, 154)) if player_skin in tanks_list else pygame.transform.scale(player_left, (45,55))
        self.image.set_colorkey(BLACK)

        if keystate[pygame.K_SPACE]: 
            if player_skin in tanks_list: self.shoot()
        
        if self.rect.right > WIDTH - 160: self.rect.right = WIDTH - 160

        if self.rect.left < WIDTH - 467: self.rect.left = WIDTH - 467

        self.rect.x += self.speedx

    def shoot(self):
        now = pygame.time.get_ticks()

        if now - self.last_shot > self.shoot_delay:
            self.last_shot = now
            
            bullet = Bullet(self.rect.centerx, self.rect.top)

            bullets.add(bullet)
            all_sprites.add(bullet)

##-Пуля-##
class Bullet(pygame.sprite.Sprite):

    def __init__(self, x, y):

        pygame.sprite.Sprite.__init__(self)

        self.image = bullet_skin
        self.image.set_colorkey(BLACK)

        self.rect = self.image.get_rect()
        self.rect.bottom = y
        self.rect.centerx = x

        self.speedy = -10

    def update(self):

        self.rect.y += self.speedy
        if self.rect.bottom < 0: self.kill()


#-------------------------------Изображения-------------------------------#

##Все пути к фоткам разного типа##
img = f"{dc.select('PH.nf', 'path')}{divider}assets{divider}img"
img_players = f"{dc.select('PH.nf', 'path')}{divider}assets{divider}img{divider}player"
img_items = f"{dc.select('PH.nf', 'path')}{divider}assets{divider}img{divider}items"

##Изображение линий##
line_left_skin = pygame.image.load(os.path.join(img, 'line1.png')).convert()
line_right_skin = pygame.image.load(os.path.join(img, 'line2.png')).convert()

##Изображение противников##
mob_skin_up = pygame.image.load(os.path.join(img_players, 'mob_up.png')).convert()
mob_skin_down = pygame.image.load(os.path.join(img_players, 'mob_down.png')).convert()

##Изображение вещей##
petrol_bak = pygame.image.load(os.path.join(img_items, 'petrol.png')).convert()
coin_skin = pygame.image.load(os.path.join(img_items, 'coin.png')).convert()
repair_kit_skin = pygame.image.load(os.path.join(img_items, 'r_c.png')).convert()
bullet_skin = pygame.image.load(os.path.join(img_items, 'bullet.png')).convert()

##CABOOOOM##
boom_skin = pygame.image.load(os.path.join(img_items, 'cabom.png')).convert()

background = pygame.image.load(os.path.join(img, 'bg2.png')).convert() if player_skin in tanks_list else pygame.image.load(os.path.join(img, 'bg.png')).convert()
background_rect = background.get_rect()

##Отображение скинов машинки##
photo_player = pygame.image.load(os.path.join(img_players, f'{player_skin}.png')).convert()
player_left = pygame.image.load(os.path.join(img_players, f'{player_skin}_left.png')).convert()
player_right = pygame.image.load(os.path.join(img_players, f'{player_skin}_right.png')).convert()


#-------------------------------Музыка и звуки-------------------------------#

##-Настройка фоновой музыки в игре-##
playlist = ''
playlist = f"{dc.select('PH.nf', 'path')}{divider}assets{divider}music{divider}game_song2" if player_skin in tanks_list else f"{dc.select('PH.nf', 'path')}{divider}assets{divider}music{divider}game_song1.wav"

pygame.mixer.music.load(playlist)

pygame.mixer.music.play(-1)
pygame.mixer.music.set_volume(0.1)


#-------------------------------Групировка-------------------------------#

all_sprites = pygame.sprite.Group()

##Пуля##
bullets = pygame.sprite.Group()

##Противники##
mob_up_chek = pygame.sprite.Group()
mob_down_chek = pygame.sprite.Group()
mob_up_spawn()
mob_down_spawn()

##Показатель hp##
livs = pygame.sprite.Group()
live_strip_update()

##Боковые полосы##
line_left = pygame.sprite.Group()
line_right = pygame.sprite.Group()
walls()

##Монетка##
coins = pygame.sprite.Group()
coin_spawn()

##Игрок##
player = pygame.sprite.Group()
player = Car()
all_sprites.add(player)

##Показатель бензина##
petrol_strip_chek = pygame.sprite.Group()
petrol_strip_update()

##Бак бензина##
petrols = pygame.sprite.Group()
petrol_spawn()

##Ремонт комплект##
repair_kits = pygame.sprite.Group()
repair_kit_spawn()


#-------------------------------Переменные и цикл-------------------------------#

live_update = False
game_over = False
running = True

while running:

    clock_fps.tick(FPS)

    ##Проверка на кнопки выхода(хрестик и кнопка Esc)##
    for event in pygame.event.get():
        if event.type == pygame.QUIT: running = False

    keystate = pygame.key.get_pressed()
    if keystate[pygame.K_ESCAPE]: running = False
    
    ##Обновление спрайтов##
    all_sprites.update()

    
    #-------------------------------столкновения спрайтов-------------------------------#

    hits = pygame.sprite.spritecollide(player,mob_up_chek,True)
    for hit in hits:
        live_update = True

        player_lives -= 10 if player_skin in tanks_list else 50
        
        if speed_player > 6.5: speed_player -= 0.1

        mob_up_spawn()

    hits = pygame.sprite.spritecollide(player,mob_down_chek,True)
    for hit in hits:
        live_update = True

        player_lives -= 10 if player_skin in tanks_list else 50
        
        if speed_player > 6.5: speed_player -= 0.1

        mob_down_spawn()

    g = pygame.sprite.spritecollide(player, line_left, False)
    for j in g:
        live_update = True

        player_lives -= 0 if player_skin in tanks_list else 1

        live_strip_update()
            
    g = pygame.sprite.spritecollide(player, line_right, False)
    for j in g:
        live_update = True

        player_lives -= 0 if player_skin in tanks_list else 1

        live_strip_update()

    g = pygame.sprite.spritecollide(player, petrols, True)
    for j in g:
        player_petrol += 50

        petrol_strip_update()

    g = pygame.sprite.spritecollide(player, repair_kits, True)
    for j in g:

        player_lives += 50

        repair_kit_spawn()

    g = pygame.sprite.spritecollide(player, coins, True)
    for j in g:

        dc.update(f'{player_nickname}.nf', 'coin', dc.select(f'{player_nickname}.nf', 'coin') + 1)

        coin_spawn()

    #-------------------------------Проверки-------------------------------#

    ##Проверки(да-да, они очень тупые, но хоть что-то)##
    if player_lives <= 0: game_over = True
    if player_petrol <= 0: game_over = True

    if score >= score_chek:

        score_chek += 10

        player_petrol -= 0.2 if player_skin in tanks_list else 2
        
        petrol_strip_update()

    if player_petrol <= 50:

       pet_chek = True
       #petrol_spawn()

    if player_lives <= 50: repair_kit_spawn()

    #-------------------------------Отрисовка екрана и данных на нем-------------------------------#

    ##Отрисовка екрана##
    screen.fill(BLACK)
    screen.blit(background, background_rect)
    all_sprites.draw(screen)

    ##Текст на екране##
    draw_text(screen, str(player_lives), 18, WIDTH - 42, 335)

    print_petrol = "%.1f" % player_petrol
    draw_text(screen, str(print_petrol), 18, WIDTH - 100, 335)

    draw_text(screen, str(score), 22, WIDTH - 20, 196)

    print_speed = "%.1f" % speed_player
    draw_text(screen, str(print_speed), 20, WIDTH - 85, 280)

    draw_text(screen, str(clock_fps.tick(FPS)), 22, WIDTH - 20, 7)

    draw_text(screen, player_nickname, 22, WIDTH - 65, 93)
    
    draw_text(screen, f'{dc.select(f"{player_nickname}.nf", "coin")}', 22, WIDTH - 65, 137)

    ##Проверка на конец игры##
    if game_over == True:
        draw_game_over_text(screen, 'GAME OVER', 100, WIDTH/2, HEIGHT/2)

        if score == 0: dc.remove_table(f'{player_nickname}.nf')

        else: 
            if dc.select(f'{player_nickname}.nf', 'score') < score: pass

            else: dc.update(f'{player_nickname}.nf', 'score', score)

        running = False

    pygame.display.flip()
    
pygame.quit()
os.remove(f"{project_path}{divider}INFO.nf")
if platform.system() == 'Windows': os.system('start menu.py')
elif platform.system() == 'Linux': subprocess.call(f'{project_path}{divider}menu.py')
