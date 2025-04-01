import pygame
# Random: Help With Random Ghost Movement
import random

# Initialize pygame: Game Initialization
pygame.init()

# Constant Variables Section
WIDTH, HEIGHT = 600, 600  # The dimensions of the game window
GRID_SIZE = 30  # Each cell in the grid is 30x30 pixels
ROWS, COLS = HEIGHT // GRID_SIZE, WIDTH // GRID_SIZE  # Number of rows and columns in the grid
WHITE = (255, 255, 255)  # Color for empty paths and pellets
BLACK = (0, 0, 0)  # Background color
YELLOW = (255, 255, 0)  # Color for Pac-Man
RED = (255, 0, 0)  # Color for ghosts
BLUE = (0, 0, 255)  # Color for walls

# Maze grid (1 = Wall, 0 = Empty path, 2 = Pellet, 3 = Ghost, 4 = Pac-Man)
maze = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 1],
    [1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1],
    [1, 0, 1, 3, 1, 0, 1, 3, 0, 0, 0, 0, 1, 3, 1, 0, 1, 3, 0, 1],
    [1, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]

# Store pellet positions separately
pellet_positions = [(row_idx, col_idx) for row_idx, row in enumerate(maze) for col_idx, cell in enumerate(row) if cell == 2]


# Game Render Section: Function iterates through the maze grid and draws the appropriate elements on the screen
def draw_maze(screen):
    for row_idx, row in enumerate(maze):
        for col_idx, cell in enumerate(row):
            x, y = col_idx * GRID_SIZE, row_idx * GRID_SIZE
            if cell == 1:
                pygame.draw.rect(screen, BLUE, (x, y, GRID_SIZE, GRID_SIZE))
            elif cell == 2:
                pygame.draw.circle(screen, WHITE, (x + GRID_SIZE // 2, y + GRID_SIZE // 2), 5)
            elif cell == 3:
                pygame.draw.circle(screen, RED, (x + GRID_SIZE // 2, y + GRID_SIZE // 2), 12)
            elif cell == 4:
                pygame.draw.circle(screen, YELLOW, (x + GRID_SIZE // 2, y + GRID_SIZE // 2), 12)


# Locate Pac-Man & Ghosts Within The Maze: Function scans the grid and returns their positions,
# which will be used for movement and collision detection
def get_positions():
    pacman_pos = None
    ghost_positions = []
    for row_idx, row in enumerate(maze):
        for col_idx, cell in enumerate(row):
            if cell == 4:
                pacman_pos = [row_idx, col_idx]
            elif cell == 3:
                ghost_positions.append([row_idx, col_idx])
    return pacman_pos, ghost_positions

pacman_pos, ghost_positions = get_positions()
score = 0
lives = 3

# Control Pacman's Movement Function Based On Player Input
def move_pacman(direction, screen):
    global pacman_pos, score
    row, col = pacman_pos
    new_row, new_col = row, col

    if direction == "UP":
        new_row -= 1
    elif direction == "DOWN":
        new_row += 1
    elif direction == "LEFT":
        new_col -= 1
    elif direction == "RIGHT":
        new_col += 1

    # Check if the new position is not a wall
    if maze[new_row][new_col] != 1:
        # Check if Pac-Man eats a pellet
        if (new_row, new_col) in pellet_positions:
            # Remove the pellet
            pellet_positions.remove((new_row, new_col))
            # Increase the score
            score += 10

        # Clear old position
        maze[row][col] = 0
        # Move Pac-Man
        maze[new_row][new_col] = 4
        # Update Pac-Man’s position
        pacman_pos = [new_row, new_col]

    # Check if Pac-Man collides with a ghost
    check_collision(screen)



# Moving The Ghosts Function
def move_ghosts(screen):
    # Right, Left, Down, Up
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    for ghost in ghost_positions:
        row, col = ghost
        # Randomize movement direction
        random.shuffle(directions)

        for dr, dc in directions:
            new_row, new_col = row + dr, col + dc

            # Check if new position is an empty path or pellet
            if maze[new_row][new_col] in [0, 2]:
                # Restore empty path
                maze[row][col] = 0
                if (row, col) in pellet_positions:
                    # Restore pellet if ghost was on one
                    maze[row][col] = 2

                # Update ghost position
                ghost[0], ghost[1] = new_row, new_col
                # Move ghost
                maze[new_row][new_col] = 3
                break

    # Check if a ghost has collided with Pac-Man
    check_collision(screen)


# Detects Collisions Between Pac-Man And Ghosts Function
def check_collision(screen):
    global lives, pacman_pos
    for ghost in ghost_positions:
        # Check if Pac-Man and a ghost occupy the same position
        if pacman_pos == ghost:
            # Decrease lives count
            lives -= 1

            if lives > 0:
                # Show a message if lives remain
                display_message(screen, "You lost a life!", RED)
            if lives == 0:
                # Show game over message
                display_message(screen, "Game Over!", RED)
                pygame.quit()
                exit()

            # Reset Pac-Man position and update the maze immediately
            old_row, old_col = pacman_pos
            # Clear old position
            maze[old_row][old_col] = 0
            # Reset Pac-Man to the starting position
            pacman_pos = [1, 1]
            # Place Pac-Man back on the grid
            maze[1][1] = 4



# Display Messages On the Screen Function
def display_message(screen, message, color=WHITE):
    # Set the font size to 50
    font = pygame.font.Font(None, 50)
    # Render the message text
    text = font.render(message, True, color)
    # Center the text on the screen
    text_rect = text.get_rect(center=(WIDTH // 2, HEIGHT // 2))

    # Draw the message on the screen
    screen.blit(text, text_rect)
    # Update the display to show the message
    pygame.display.flip()
    # Pause for 2 seconds before continuing
    pygame.time.delay(2000)



# Main Game Loop Function
def main():
    # Create the game window
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    # Set window title
    pygame.display.set_caption("Pac-Man Game")
    # Initialize game clock
    clock = pygame.time.Clock()

    while True:
        # Clear screen to black before drawing
        screen.fill(BLACK)
        # Render the maze and all game elements
        draw_maze(screen)

        # Display score and lives
        font = pygame.font.Font(None, 36)
        score_text = font.render(f"Score: {score}", True, WHITE)
        lives_text = font.render(f"Lives: {lives}", True, WHITE)
        screen.blit(score_text, (10, 10))
        screen.blit(lives_text, (WIDTH - 100, 10))

        # Update ghost positions
        move_ghosts(screen)
        # Update the display with new frame
        pygame.display.flip()

        # Handle user inputs
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    move_pacman("UP", screen)
                elif event.key == pygame.K_DOWN:
                    move_pacman("DOWN", screen)
                elif event.key == pygame.K_LEFT:
                    move_pacman("LEFT", screen)
                elif event.key == pygame.K_RIGHT:
                    move_pacman("RIGHT", screen)

        clock.tick(5)  # Control game speed


if __name__ == "__main__":
    main()
