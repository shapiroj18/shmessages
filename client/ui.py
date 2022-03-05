import curses
import time

class UI:
    def __init__(self):
        self.stdscr = curses.initscr()
    
    def logic(self, messages: list):
        curses.noecho()
        curses.cbreak()
        self.stdscr.keypad(True)
        
        self.stdscr.clear()
        pad = curses.newpad(100, 100)
        
        for index, message in enumerate(messages):
            txt = ''
            for i in message:
                txt+=str(i)
            pad.addstr(index,0, ''.join(txt))
        
        pad.refresh( 0,0, 5,5, 20,75)
        
        time.sleep(20)
        curses.endwin()
        
    def main(self, messages: list):
        return curses.wrapper(self.logic(messages=messages))