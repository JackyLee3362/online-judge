import pygame
screen = weight, height = 1920//2, 1080//2
bg_color1 = (0,128,128)
bg_color2 = (60,60,60)
bg_color3 = (255,0,0)
pygame.init()
pygame.key.set_repeat(10, 15)
screen_image = pygame.display.set_mode(screen)
screen_rect = screen_image.get_rect()

person_image = pygame.image.load("firesheep.png")
person_rect = person_image.get_rect()
person_rect.center = screen_rect.center
person_size = person_image.get_size()

while True:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      pygame.quit()
    if event.type == pygame.KEYDOWN:
      if event.key == pygame.K_LEFT or event.key == pygame.K_a:
        if person_rect.x > 0: 
          person_rect.x -= 10
      elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:
        if person_rect.x < weight-person_size[0]: 
          person_rect.x += 10
      elif event.key == pygame.K_UP or event.key == pygame.K_w:
        if person_rect.y > 0: 
          person_rect.y -= 10
      elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
        if person_rect.y < height-person_size[1]: 
          person_rect.y += 10
  screen_image.fill(bg_color1)
  screen_image.blit(person_image,person_rect)
  pygame.display.update()
  