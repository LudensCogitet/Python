import pygame
from random import randint

class Ball(pygame.sprite.Sprite):
        def __init__(self,x,y):
                pygame.sprite.Sprite.__init__(self)

                self.image = pygame.image.load("./ball.png")
                self.rect = self.image.get_rect()
                self.rect.left = x
                self.rect.top = y

class InvisiWall(pygame.sprite.Sprite):
        def __init__(self,x,y,surface):
                pygame.sprite.Sprite.__init__(self)

                self.rect = surface.get_rect()
                self.rect.left = x
                self.rect.top = y
                self.mask = pygame.mask.from_surface(surface)
                
pygame.init()
screen = pygame.display.set_mode((640,480))
print("SCREEN ALPHA: " + str(screen.get_alpha()))
done = False
game_clock = pygame.time.Clock()

ball = Ball(20,20)

background = pygame.image.load("./scene0.png")

wall_group = pygame.sprite.Group()

collisions = 0

lines = []
drawLine = False
i = 0

while not done:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        done = True
                elif event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_ESCAPE:
                                done = True
                        if event.key == pygame.K_RETURN:
                                
                                for line in lines:
                                        surface_x = min([line[0][0],line[1][0]])
                                        surface_y = min([line[0][1],line[1][1]])
                                        print(surface_x)
                                        print(surface_y)

                                        width = abs(abs(line[0][0]) - abs(line[1][0]))
                                        height = abs(abs(line[0][1]) - abs(line[1][1]))
                                        if height < 5:
                                                height = 5
                                        if width < 5:
                                                width = 5
                                        print(width)
                                        print(height)

                                        
                                        temp = pygame.Surface((width, height), pygame.SRCALPHA, 32)
                                        temp.convert_alpha()
                                        
                                        pygame.draw.line(temp,(255,0,0),(line[0][0]-surface_x,line[0][1]-surface_y),(line[1][0]-surface_x,line[1][1]-surface_y),2)
                                        pygame.image.save(temp,"line"+str(i)+".png")
                                        wall_group.add(InvisiWall(surface_x,surface_y,temp))
                                        lines.remove(line)
                                        
                                        i = i + 1
                                        
                elif event.type == pygame.MOUSEBUTTONDOWN:
                        mouseCoords = pygame.mouse.get_pos()
                        if drawLine == False:
                                drawLine = True
                                lineCoords = [[mouseCoords[0],mouseCoords[1]],[0,0]]
                                lines.append(lineCoords)
                        elif drawLine == True:
                                drawLine = False
                                

        if drawLine == True:
                for line in lines:
                        mouseCoords = pygame.mouse.get_pos()
                        lines[len(lines)-1][1][0], lines[len(lines)-1][1][1] = mouseCoords[0],mouseCoords[1]

        x_move = 0
        y_move = 0
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RIGHT]:
                x_move = 2
        if keys[pygame.K_LEFT]:
                x_move = -2
        if keys[pygame.K_DOWN]:
                y_move = 2
        if keys[pygame.K_UP]:
                y_move = -2
                   

        ball.rect = ball.rect.move(x_move,y_move)

        if pygame.sprite.spritecollideany(ball,wall_group,pygame.sprite.collide_mask):
                ball.rect = ball.rect.move(-x_move,-y_move)
                
        screen.fill((0,0,0))
        screen.blit(background,background.get_rect())
        screen.blit(ball.image,ball.rect)
        for line in lines:
                pygame.draw.aaline(screen,(255,0,0),line[0],line[1],5)
        #ball_group.draw(screen)
        pygame.display.flip()
        game_clock.tick(60)
	

pygame.quit()
