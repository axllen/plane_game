import pygame
from settings import *


class PlaneGame():

    def __init__(self):
        # 初始化游戏
        pygame.init()

        self.screen = pygame.display.set_mode((PLANE_WIDTH, PLANE_HEIGHT))
        self.clock = pygame.time.Clock()
        self.__create_sprites()

    def __create_sprites(self):
        pass

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
        pass

    @staticmethod
    def __quit_game(self):
        # 退出游戏
        pygame.quit()
        exit()

if __name__ == '__main__':
    plane_game = PlaneGame()
    plane_game.start_game()
