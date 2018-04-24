import pygame

class Ship():

    def __init__(self, screen):
        """初始化飞船并设置其初始位置"""
        self.screen = screen

        # 加载飞船图像并获取其外接矩形
        self.image = pygame.image.load("images\ship.bmp")
        # 获取飞船图像的外接矩形
        self.rect = self.image.get_rect()
        # 获取屏幕的外接矩形
        self.screen_rect = screen.get_rect()

        # 将每艘新飞船放在屏幕底部中央
        # 飞船的外接矩形中心点坐标 = 屏幕的外接矩形中心点坐标
        self.rect.centerx = self.screen_rect.centerx
        # 飞船的外接矩形下边缘 = 屏幕的外接矩形下边缘
        self.rect.bottom = self.screen_rect.bottom

    def blitme(self):
        """在指定位置绘制飞船"""
        self.screen.blit(self.image, self.rect)