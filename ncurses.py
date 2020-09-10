import os
import curses
from curses import wrapper

def draw_menu(stdscr):
    k = 0
    cursor_x = 0
    cursor_y = 0
    x = 0
    y = 0
    title = "Created by Akanksha"
    height, width = stdscr.getmaxyx()
    
    while k != ord('q'):
        if k == curses.KEY_LEFT:
            cursor_x -= 1
            x -= 1
        elif k == curses.KEY_RIGHT:
            cursor_x += 1
            x += 1
        elif k == curses.KEY_UP:
            cursor_y += 1
            y += 1
        elif k == curses.KEY_DOWN:
            cursor_y -= 1
            y -= 1


        x = max(0, x)
        x = min(width-1, x)

        y = max(0, y)
        y = min(height-1, y)

        k = stdscr.getch()


def main():
    wrapper(draw_menu)

if __name__ == "__main__":
    main()