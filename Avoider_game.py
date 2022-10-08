from ursina import*
from tkinter import messagebox
import random
app = Ursina()
enemy_y_pos = 8
score = 0
stop = 0
enemy = Entity(model = "quad", position = (0, enemy_y_pos), color = color.red, collider = "box")
enemy2 = Entity(model = "quad", position = (random.randint(-5, 3), enemy_y_pos), color = color.red, collider = "box")
enemy3 = Entity(model = "quad", position = (random.randint(-5, 3), enemy_y_pos), color = color.red, collider = "box")
enemy4 = Entity(model = "quad", position = (random.randint(-5, 3), enemy_y_pos), color = color.red, collider = "box")
player = Entity(model = "circle", position = (0, -2), collider = "box", color = color.green)
score_text = Text(f'Score:{score}', origin = (4,5, -5), scale = 2)
def update():
  global stop
  if stop == 0:
    enemy.y -= enemy_y_pos * time.dt / 3
    enemy2.y -= enemy_y_pos * time.dt / 3
    enemy3.y -= enemy_y_pos * time.dt / 3
    enemy4.y -= enemy_y_pos * time.dt / 3
    if enemy.y <= -5:
        global score, score_text
        score += 1
        score_text.y = 1
        score_text = Text(f'Score:{score}', origin = (4,5, -5), scale = 2)
        enemy.y = enemy_y_pos
        enemy.x = random.randint(-5, 5)
        enemy2.y = 6
        enemy2.x = random.randint(-5, 5)
        enemy3.y = 6
        enemy.x = random.randint(-5, 5)
        enemy4.y = 6
        enemy.x = random.randint(-5, 5)
    if player.intersects(enemy).hit:
        enemy.color = color.lime
        destroy(player, delay = 0.1)
        messagebox.showerror("Game", "You lost")
        stop += 1
    elif player.intersects(enemy2).hit:
        enemy2.color = color.lime
        destroy(player, delay = 0.1)
        messagebox.showerror("Game", "You lost")
        stop += 1
    elif player.intersects(enemy3).hit:
        enemy3.color = color.lime
        destroy(player, delay = 0.1)
        messagebox.showerror("Game", "You lost")
        stop += 1
    elif player.intersects(enemy4).hit:
        enemy4.color = color.lime
        destroy(player, delay = 0.1)
        messagebox.showerror("Game", "You lost")
        stop += 1
    else:
        enemy.color = color.red
        enemy2.color = color.red
        enemy3.color = color.red
        enemy4.color = color.red
    if held_keys["a"]:
        player.x -= 2 * time.dt
    if held_keys["d"]:
        player.x += 2 * time.dt
app.run()
