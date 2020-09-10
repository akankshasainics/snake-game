import os
import curses
import random
from curses import wrapper

def draw_menu(stdscr):
    k = 0
    cursor_x = 0
    cursor_y = 0
    x = 0
    y = 0
    inc_x = 1
    inc_y = 0
    statusbarstr = "        quit with q" + "             Created by Akanksha"
    height, width = stdscr.getmaxyx()
    target_x = random.randint(1, width - 1)
    target_y = random.randint(1, height - 1)
    curses.start_color()
    curses.init_pair(1, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_WHITE, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_BLACK, curses.COLOR_CYAN)
    stdscr.clear()
    stdscr.refresh()
    
    
    while k != ord('q'):
        stdscr.clear()
        if k == curses.KEY_LEFT:
            x -= 1
        elif k == curses.KEY_RIGHT:
            x += 1
        elif k == curses.KEY_UP:
            y -= 1
        elif k == curses.KEY_DOWN:
            y += 1

        x = max(0, x)
        x = min(width-1, x)

        y = max(0, y)
        y = min(height-1, y)

        if target_x == x +3 and target_y == y:
            stdscr.addstr(1, 1, "you won", 1)
            break
        
        stdscr.addstr(target_y, target_x, "o", curses.color_pair(2))
        stdscr.addstr(y, x, "=", curses.color_pair(2))
        stdscr.addstr(y+inc_y, x+inc_x, "=", curses.color_pair(2))
        stdscr.addstr(y+(inc_y)*2, x+(inc_x)*2, "=", curses.color_pair(2))
        stdscr.addstr(y+(inc_y)*3, x+(inc_x)*3, ">", curses.color_pair(2))

        stdscr.attron(curses.color_pair(3))
        stdscr.addstr(height-1, 0, statusbarstr)
        stdscr.addstr(height-1, len(statusbarstr), " " * (width - len(statusbarstr) - 1))
        stdscr.attroff(curses.color_pair(3))

        stdscr.refresh()
        k = stdscr.getch()


def main():
    wrapper(draw_menu)

if __name__ == "__main__":
    main()