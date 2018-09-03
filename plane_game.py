import pygame
from plane_sprites import *


class PlaneGame(object):

    def __init__(self):
        # 初始化游戏
        pygame.init()

        # 创建游戏窗口
        self.screen = pygame.display.set_mode(SCREEN_RECT.size)
        # 创建游戏时钟
        self.clock = pygame.time.Clock()
        # 调用私有方法，创建精灵和精灵组
        self.__create_sprites()

        # 设置定时器事件，创建敌机
        pygame.time.set_timer(CREATE_ENEMY_EVENT, 1000)
        # 设置定时器事件，创建子弹
        pygame.time.set_timer(CREATE_BULLETS_EVENT, 500)

    def __create_sprites(self):

        # 创建背景精灵和精灵组
        bg1 = Background()
        bg2 = Background(True)
        self.bg_group = pygame.sprite.Group(bg1, bg2)

        # 创建敌机精灵组
        self.enemy_group = pygame.sprite.Group()

        # 创建子弹精灵组
        self.bullet_group = pygame.sprite.Group()

        # 创建英雄精灵和精灵组
        self.hero = Hero()
        self.hero_group = pygame.sprite.Group(self.hero)

    def start_game(self):
        print('游戏开始...')

        while True:
            self.clock.tick(FRAME_PER_SEC)
            self.__event_handler()
            self.__check_collide()
            self.__update_sprites()
            pygame.display.flip()

    def __event_handler(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                PlaneGame.__quit_game()
            elif event.type == CREATE_ENEMY_EVENT:
                # 创建敌机精灵
                enemy = Enemy()
                # 将敌机精灵加入精灵组
                self.enemy_group.add(enemy)
            elif event.type == CREATE_BULLETS_EVENT:
                # 创建子弹精灵
                bullets = Bullet()
                # 将子弹精灵加入精灵组
                self.bullet_group.add(bullets)

        #捕获按键
        keys_pressed = pygame.key.get_pressed()
        if keys_pressed[pygame.K_RIGHT]:
                self.hero.speed = 2
        elif keys_pressed[pygame.K_LEFT]:
                self.hero.speed = -2
        else:
            self.hero.speed = 0

    def __check_collide(self):
        pass

    def __update_sprites(self):

        self.bg_group.update()
        self.bg_group.draw(self.screen)

        self.enemy_group.update()
        self.enemy_group.draw(self.screen)

        self.bullet_group.update()
        self.bullet_group.draw(self.screen)

        self.hero_group.update()
        self.hero_group.draw(self.screen)

    @staticmethod
    def __quit_game():
        # 退出游戏
        print('游戏结束')

        pygame.quit()
        exit()


if __name__ == '__main__':

    plane_game = PlaneGame()
    plane_game.start_game()
