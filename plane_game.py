import pygame
from plane_sprites import *


class PlaneGame(object):

    def __init__(self):
        # 初始化游戏
        pygame.init()

        self.screen = pygame.display.set_mode(SCREEN_RECT.size)
        self.clock = pygame.time.Clock()
        self.__create_sprites()

    def __create_sprites(self):

        bg1 = Background()
        bg2 = Background(True)

        self.bg_group = pygame.sprite.Group(bg1, bg2)

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

    def __check_collide(self):
        pass

    def __update_sprites(self):

        self.bg_group.update()
        self.bg_group.draw(self.screen)

    @staticmethod
    def __quit_game():
        # 退出游戏
        print('游戏结束')

        pygame.quit()
        exit()


if __name__ == '__main__':

    plane_game = PlaneGame()
    plane_game.start_game()
