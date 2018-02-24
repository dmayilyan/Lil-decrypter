#!/usr/bin/env python
# -*- coding: utf-8 -*-

import curses
import traceback
import time
from itertools import cycle
from subprocess import call


def decr():
    text = input("\033[1mՏեղադրեք տեքստը այստեղ.\nEnter the text to inverse:\033[0;0m \n")

    print("\033[1mՎերծանված տեքստը.\nInversed text. Yay we can read what she has written!\033[0;0m\n", text[::-1])


def main(stdscr):
    # Defining colors
    curses.init_pair(1, curses.COLOR_RED, curses.COLOR_BLACK)

    # Setting background color
    stdscr.bkgd(curses.color_pair(1))
    stdscr.refresh()

    # Getting the height and width of the window for window creation
    height, width = stdscr.getmaxyx()

    # Creating the window
    win = curses.newwin(height, width, 0, 0)
    # Coloring
    win.bkgd(curses.color_pair(1))
    # Borders
    win.box()

    # Making text fancy (bold and colored)
    c = curses.A_BOLD
    c |= curses.color_pair(1)

    # Printing the text
    # win.erase()
    text = "+ Lil decrypter v1.0 +"
    win.addstr(height // 2, (width - len(text)) // 2, text, c)
    win.refresh()
    time.sleep(1)

    win.refresh()

    return width


def splash_screen(width):
    text = "Lil decrypter v1.0"
    # First line of symbols
    for i in range(width):
        print("-", end="")

    spaces = (width - len(text)) // 2
    for i in range(spaces):
        print(" ", end="")

    print("\033[91m" + text + "\033[0;0m")

    # Second line of symbols
    for i in range(width):
        print("-", end="")


if __name__ == '__main__':
    try:
        # Initialize curses
        stdscr = curses.initscr()
        # Turn off echoing of keys, and enter cbreak mode,
        # where no buffering is performed on keyboard input
        curses.noecho()
        curses.cbreak()
        curses.curs_set(0)  # Make cursor invisible
        curses.start_color()

        # In keypad mode, escape sequences for special keys
        # (like the cursor keys) will be interpreted and
        # a special value like curses.KEY_LEFT will be returned
        stdscr.keypad(1)

        # Enter the main loop and get the width of the window
        width = main(stdscr)
        # Set everything back to normal
        stdscr.keypad(0)
        curses.echo()
        curses.nocbreak()
        curses.endwin()                 # Terminate curses

        call(["clear"])  # Cleaning the window

        # Starting the splash screen
        splash_screen(width)
        # Starting decryppt part
        decr()
    except:
        # In event of error, restore terminal to sane state.
        stdscr.keypad(0)
        curses.echo()
        curses.nocbreak()
        curses.endwin()
        traceback.print_exc()           # Print the exception

        curses.curs_set(1)  # Getting back the cursor
