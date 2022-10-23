import pygame,sys
# https://www.bilibili.com/video/BV1X44y1N7gk

bg_color1 = (0,128,128)
bg_color2 = (60,60,60)
bg_color3 = (255,0,0)

pygame.init()
screen_image = pygame.display.set_mode((800,600))
screen_rect = screen_image.get_rect()
pygame.display.set_caption("pygame游戏")


ship_image = pygame.image.load('intro_ball.gif')
ship_rect = ship_image.get_rect()

ship_rect.center = screen_rect.center

# 子弹
bullet_rect = pygame.Rect(0,0,20,50)
bullet_rect.midbottom = ship_rect.midtop
# 文字
txt_font = pygame.font.SysFont(None, 48)
txt_image = txt_font.render('Abc1234', True, bg_color2, bg_color3)
txt_rect = txt_image.get_rect()

pygame.display.flip()
while True:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      sys.exit()
    elif event.type == pygame.KEYDOWN:
      if event.key == pygame.K_LEFT:
        print("left")
        ship_rect.x -= 10
      if event.key == pygame.K_RIGHT:
        ship_rect.x += 10
      if event.key == pygame.K_UP:
        ship_rect.y -= 10
      if event.key == pygame.K_DOWN:
        ship_rect.y += 10 
  # 绘制图像
  screen_image.fill(bg_color1)
  screen_image.blit(ship_image, ship_rect)
  pygame.draw.rect(screen_image,bg_color2,bullet_rect)
  screen_image.blit(txt_image,txt_rect)
  pygame.display.flip()


