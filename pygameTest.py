import pygame
from random import randint

class Ball(pygame.sprite.Sprite):
        def __init__(self,x,y):
                pygame.sprite.Sprite.__init__(self)

                self.image = pygame.image.load("./ball.png")
                self.rect = self.image.get_rect()
                self.rect.left = x
                self.rect.top = y

        

pygame.init()
screen = pygame.display.set_mode((640,480))
done = False
game_clock = pygame.time.Clock()

ball = Ball(20,20)

ball_group = pygame.sprite.Group()

collisions = 0

for i in range(10):
        new_ball = Ball(randint(0,620),randint(0,460))
        ball_group.add(new_ball)

while not done:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        done = True

        keys = pygame.key.get_pressed()
        if keys[pygame.K_RIGHT]:
           ball.rect = ball.rect.move(1,0)
        if keys[pygame.K_LEFT]:
           ball.rect = ball.rect.move(-1,0)
        if keys[pygame.K_DOWN]:
           ball.rect = ball.rect.move(0,1)
        if keys[pygame.K_UP]:
           ball.rect = ball.rect.move(0,-1)

        if pygame.sprite.spritecollideany(ball,ball_group,pygame.sprite.collide_mask):
                collisions = collisions +1
                print(collisions)
                
        screen.fill((0,0,0))
        screen.blit(ball.image,ball.rect)
        ball_group.draw(screen)
        pygame.display.flip()
        game_clock.tick(60)
	

pygame.quit()
