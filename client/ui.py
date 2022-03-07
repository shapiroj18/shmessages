import curses
import time
import re

class UI:
    def __init__(self):
        self.stdscr = curses.initscr()
    
    def logic(self, messages: list):
        
        stdscr = self.stdscr
        
        name = ''
        name_done = False
        while True:
            
            input = 'What is your name?'
            stdscr.addstr(0, 0, input)
            stdscr.clrtoeol()
            stdscr.addstr(' ')
            stdscr.addstr(name)
            if name_done:
                stdscr.addstr(1, 0, f'Hi {name}!')
            
            char = stdscr.get_wch()
            if name_done:
                return 0
            
            if isinstance(char, str) and char.isprintable() and char != '\b':
                name += char
            elif char in ['\x7f']:
                name = name[:-1]
            elif char in ['\n']:
                name_done = True
            else:
                raise AssertionError(repr(char))
        
        # curses.noecho()
        # curses.cbreak()
        # self.stdscr.keypad(True)
        
        # self.stdscr.clear()
        # pad = curses.newpad(100, 100)
        
        # for index, message in enumerate(messages):
        #     txt = ''
        #     for i in message:
        #         txt+=str(i)
        #     pad.addstr(index,0, ''.join(txt))
        
        # pad.refresh( 0,0, 5,5, 20,75)
        
        # time.sleep(5)
        # curses.endwin()
        
    def main(self, messages: list):
        return curses.wrapper(self.logic(messages=messages))