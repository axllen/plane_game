import random
import pygame


SCREEN_RECT = pygame.Rect(0, 0, 480, 700)
FRAME_PER_SEC = 60
CREATE_ENEMY_EVENT = pygame.USEREVENT
CREATE_BULLETS_EVENT = pygame.USEREVENT


class GameSprite(pygame.sprite.Sprite):

    def __init__(self, image_name, speed=1):

        super().__init__()

        self.image = pygame.image.load(image_name)
        self.rect = self.image.get_rect()
        self.speed = speed

    def update(self):

        self.rect.y += self.speed


class Background(GameSprite):

    def __init__(self, is_alt=False):

        super().__init__('images/background.png')

        if is_alt:
            self.rect.y = -self.rect.height

    def update(self):

        super().update()

        if self.rect.y >= SCREEN_RECT.height:
            self.rect.y = -self.rect.height


class Enemy(GameSprite):

    # 调用父类方法，初始化敌机
    def __init__(self):

        super().__init__('images/enemy1.png')

        # 随机速度
        self.speed = random.randint(1, 3)
        # 从屏幕外飞进来
        self.rect.bottom = 0
        # 随机水平位置
        self.rect.x = random.randint(0, SCREEN_RECT.width - self.rect.width)

    # 更新敌机位置
    def update(self):

        super().update()

        # 飞出屏幕自动销毁
        if self.rect.y >= SCREEN_RECT.height:
            self.kill()


class Hero(GameSprite):

    def __init__(self):

        super().__init__('images/me1.png', speed=0)

        # 英雄初始位置
        self.rect.centerx = SCREEN_RECT.centerx
        self.rect.bottom = SCREEN_RECT.height - 50

    def update(self):

        # 水平移动
        self.rect.x += self.speed

        # 不飞出屏幕
        if self.rect.x < 0:
            self.rect.x = 0
        elif self.rect.right > SCREEN_RECT.right:
            self.rect.right = SCREEN_RECT.right

    def fire(self):

        pass


class Bullet(GameSprite):

    def __init__(self):

        super().__init__('images/bullet1.png', speed=-1)

    def update(self):

        super().update()

        if self.rect.bottom <= 0:
            self.kill()
