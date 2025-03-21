import asyncio
import pygame

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Bouncing Ball Game')
clock = pygame.time.Clock()

# Ball properties
ball_color = (0, 0, 255)
ball_radius = 20
ball_x, ball_y = 400, 300
ball_speed_x, ball_speed_y = 5, 5

async def main():
    global ball_x, ball_y, ball_speed_x, ball_speed_y
    color_toggle = False  # Used to test if the screen is updating

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

        ball_x += ball_speed_x
        ball_y += ball_speed_y

        if ball_x - ball_radius <= 0 or ball_x + ball_radius >= 800:
            ball_speed_x *= -1
        if ball_y - ball_radius <= 0 or ball_y + ball_radius >= 600:
            ball_speed_y *= -1

        # Toggle background color to test updates
        if color_toggle:
            screen.fill((255, 0, 0))  # Red background
        else:
            screen.fill((0, 255, 0))  # Green background
        color_toggle = not color_toggle

        pygame.draw.circle(screen, ball_color, (ball_x, ball_y), ball_radius)
        pygame.display.update()

        await asyncio.sleep(0)
        clock.tick(60)

asyncio.run(main())
