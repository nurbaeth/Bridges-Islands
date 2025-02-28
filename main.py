import pygame
import random

# Constants
WIDTH, HEIGHT = 600, 600
GRID_SIZE = 6
CELL_SIZE = WIDTH // GRID_SIZE
WHITE, BLACK, BLUE, GRAY = (255, 255, 255), (0, 0, 0), (50, 150, 255), (200, 200, 200)

# Generate islands with random numbers
def generate_islands(grid_size):
    islands = []
    for _ in range(grid_size):
        x, y = random.randint(0, grid_size - 1), random.randint(0, grid_size - 1)
        if (x, y) not in islands:
            islands.append((x, y, random.randint(1, 4)))  # Number of required bridges
    return islands

# Initialize game
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Bridges & Islands")
clock = pygame.time.Clock()

def draw_grid():
    for x in range(0, WIDTH, CELL_SIZE):
        pygame.draw.line(screen, GRAY, (x, 0), (x, HEIGHT))
    for y in range(0, HEIGHT, CELL_SIZE):
        pygame.draw.line(screen, GRAY, (0, y), (WIDTH, y))

def draw_islands(islands):
    for x, y, number in islands:
        pygame.draw.circle(screen, BLUE, (x * CELL_SIZE + CELL_SIZE // 2, y * CELL_SIZE + CELL_SIZE // 2), 20)
        font = pygame.font.Font(None, 36)
        text = font.render(str(number), True, WHITE)
        screen.blit(text, (x * CELL_SIZE + CELL_SIZE // 2 - 10, y * CELL_SIZE + CELL_SIZE // 2 - 10))

islands = generate_islands(GRID_SIZE)
running = True
while running:
    screen.fill(WHITE)
    draw_grid()
    draw_islands(islands)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    pygame.display.flip()
    clock.tick(30)

pygame.quit()
