import random
from PIL import Image, ImageDraw

# Cores
COLORS = ["#006400", "#000080", "#ff0000", "#1e90ff"]
BACKGROUND = "#ebedf0"

WIDTH = 52
HEIGHT = 7
BLOCK_SIZE = 20
FRAMES = 200

def draw_frame(grid):
    img = Image.new("RGB", (WIDTH * BLOCK_SIZE, HEIGHT * BLOCK_SIZE), BACKGROUND)
    draw = ImageDraw.Draw(img)
    for y in range(HEIGHT):
        for x in range(WIDTH):
            color = grid[y][x]
            if color != BACKGROUND:
                draw.rectangle(
                    [x * BLOCK_SIZE, y * BLOCK_SIZE,
                     (x + 1) * BLOCK_SIZE - 1, (y + 1) * BLOCK_SIZE - 1],
                    fill=color,
                    outline=color
                )
    return img

def tetris_animation():
    grid = [[BACKGROUND for _ in range(WIDTH)] for _ in range(HEIGHT)]
    frames = []
    for _ in range(FRAMES):
        x = random.randint(0, WIDTH - 1)
        y = 0
        color = random.choice(COLORS)
        while y < HEIGHT - 1 and grid[y + 1][x] == BACKGROUND:
            y += 1
        grid[y][x] = color
        frames.append(draw_frame(grid))
    return frames

if __name__ == "__main__":
    frames = tetris_animation()
    frames[0].save(
        "tetris.gif",
        save_all=True,
        append_images=frames[1:],
        duration=100,
        loop=0
    )
