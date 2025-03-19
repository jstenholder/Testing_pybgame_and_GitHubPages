import asyncio
import pygame

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Test Game')
clock = pygame.time.Clock()

async def main():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
        screen.fill((255, 255, 255))
        pygame.display.update()
        await asyncio.sleep(0)
        clock.tick(60)

asyncio.run(main())        