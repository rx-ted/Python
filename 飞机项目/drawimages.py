import pygame
pygame.init()

# 创建游戏的窗口  480*700
screen = pygame.display.set_mode((480, 700))

# draw background
# 1> 加载图像

# 2> 绘制图像
screen.blit(pygame.image.load("./images/background.png"), (0, 0))
# 3> 刷新屏幕
pygame.display.update()

while True:
    pass
pygame.quit()
