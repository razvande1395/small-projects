import pygame
import random
import time


pygame.init()

x_end = 1000
y_end = 600

x = x_end / 2
y = y_end / 2

block_size = 10

screen = pygame.display.set_mode((x_end, y_end))
screen.fill((125, 205, 255))
pygame.display.set_caption("Snakes, why'd it have to be snakes")
pygame.display.update()

snake_color = "red"
food_color = "purple"

font_style = pygame.font.SysFont("gothic sans ms", 25)

pygame.draw.rect(screen, snake_color, (x, y, block_size, block_size))
pygame.display.update()

speed = pygame.time.Clock()

def display_snake(block_size, body_list): #function used to display the snake on the screen, called by the game_function
    for x in body_list:
        pygame.draw.rect(screen, snake_color, (int(x[0]), int(x[1]), block_size, block_size))


def message(msg, color):
    mesg = font_style.render(msg, True, color)
    screen.blit(mesg, [x_end / 3, y_end / 2])


def game_function(): #the function containing the game loop

    body_list = []
    snake_length = 1
    
    direction = ""

    game_over = False
    game_end = False
    
    x_end = 1000
    y_end = 600
    
    x = x_end / 2  #current coordinates for the head's position, snake starts in the middle
    y = y_end / 2

    x_move = 0
    y_move = 0

    x_food = round(random.randrange(0, x_end - 1))
    y_food = round(random.randrange(0, y_end - 1))

    
    while not game_over:  #game loop, shuts down the game if the snake goes over the edge or bites itself
       

        while game_end == True:
            
            screen.fill((125, 205, 255))
            message("You lost! Press Y - Play Again or N - Quit", "red")
            pygame.display.update()
            
            for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_n:
                            game_over = True
                            game_end = False
                        if event.key == pygame.K_y:
                            game_function()
                    
        for event in pygame.event.get(): #quit the window by pressing the X button
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:   #movement branches
                if event.key == pygame.K_LEFT and direction != "right":
                    x_move = -block_size
                    y_move = 0
                    direction = "left"
                elif event.key == pygame.K_RIGHT and direction != "left":
                    x_move = block_size
                    y_move = 0
                    direction = "right"
                elif event.key == pygame.K_UP and direction != "down":
                    y_move = -block_size
                    x_move = 0
                    direction = "up"
                elif event.key == pygame.K_DOWN and direction != "up":
                    y_move = block_size
                    x_move = 0
                    direction = "down"

        if x >= x_end or x < 0 or y >= y_end or y < 0:
            game_end = True
        
        x += x_move
        y += y_move
        
        screen.fill((125, 205, 255))
        pygame.draw.rect(screen, food_color, (x_food, y_food, block_size, block_size))       

        display_snake(block_size, body_list)
    
        pygame.display.update()
        
        #workaround for eating the food; the exact coordinates (x-y for head, food) were nearly impossible to match otherwise
        if (x in range(x_food, x_food + block_size) or x + block_size in range(x_food, x_food + block_size)) and (y in range(y_food, y_food + block_size) or y + block_size in range(y_food, y_food + block_size)): 
            snake_length += 1
            x_food = round(random.randrange(0, x_end - block_size))
            y_food = round(random.randrange(0, y_end - block_size))

        snake_head = []
        snake_head.append(x)
        snake_head.append(y)
        body_list.append(snake_head)  

        if len(body_list) > 2:
            for i in body_list[:-1]:
                if i == snake_head:
                    game_end = True      

        if len(body_list) > snake_length:
            del body_list[0]

        speed.tick(15)
                    
    pygame.quit()
    quit()


game_function()
