import curses
import random

# 初始化curses模式
stdscr = curses.initscr()
curses.curs_set(0)
sh, sw = stdscr.getmaxyx()
w = curses.newwin(sh, sw, 0, 0)
w.keypad(1)
w.timeout(100)

# 初始化贪吃蛇和食物的位置
snake_x = sw//4
snake_y = sh//2
snake = [
    (snake_y, snake_x),
    (snake_y, snake_x-1),
    (snake_y, snake_x-2)
]

food = (sh//2, sw//2)
w.addch(food[0], food[1], curses.ACS_PI)

# 游戏主循环
key = curses.KEY_RIGHT

while True:
    w.border(0)
    w.addstr(0, 2, 'Score : ' + str(len(snake)-3))
    w.timeout(150 - (len(snake) - 3) * 5)

    prev_key = key
    event = w.getch()
    if event != curses.ERR:
        key = event

    # 获取蛇头的下一个位置
    snake_head = snake[0]
    if key == curses.KEY_DOWN:
        new_head = (snake_head[0] + 1, snake_head[1])
    elif key == curses.KEY_UP:
        new_head = (snake_head[0] - 1, snake_head[1])
    elif key == curses.KEY_LEFT:
        new_head = (snake_head[0], snake_head[1] - 1)
    elif key == curses.KEY_RIGHT:
        new_head = (snake_head[0], snake_head[1] + 1)
    else:
        new_head = snake_head

    # 检查是否吃到食物
    if new_head == food:
        food = None
        while food is None:
            nf = (random.randint(1, sh-2), random.randint(1, sw-2))
            if nf not in snake:
                food = nf
        w.addch(food[0], food[1], curses.ACS_PI)
    else:
        # 如果没有吃到食物，移动蛇身
        tail = snake.pop()
        w.addch(tail[0], tail[1], ' ')

    # 检查是否撞墙或咬到自己
    if (new_head[0] in [0, sh-1]) or (new_head[1] in [0, sw-1]) or new_head in snake:
        break

    # 移动蛇头
    snake.insert(0, new_head)

# 游戏结束
curses.endwin()
print("Game over! Your score is:", len(snake)-3)

