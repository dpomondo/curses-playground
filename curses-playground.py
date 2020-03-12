# playing around with python curses

import curses

def main_loop(stdscr):

   # clear the screen
   stdscr.clear()
   stdscr.refresh()

   # initialize the variables
   k = 0      
   cursor_x = 0
   cursor_y = 0

   # start color
   curses.start_color()
   curses.init_pair(1, curses.COLOR_CYAN, curses.COLOR_BLACK)
   curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)
   curses.init_pair(3, curses.COLOR_BLACK, curses.COLOR_WHITE)

   # start the loop
   while (k != ord('q')):

       stdscr.clear()
       height, width = stdscr.getmaxyx()

       screen_print = "Last Key Pressed: {}".format(k)

       cursor_x = int((width - len(screen_print)) / 2)
       cursor_y = int((height - 1) / 2)

       # write to the screen
       stdscr.attron(curses.color_pair(1))
       stdscr.addstr(cursor_y, cursor_x, screen_print)

       # refresh
       stdscr.refresh()

       # get input
       k = stdscr.getch()

def main():
   curses.wrapper(main_loop)

if __name__ == "__main__":
   main()

