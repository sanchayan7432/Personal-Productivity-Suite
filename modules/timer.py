"""Timer and stopwatch functionality."""
from .utils import safe_input
import time


def run():
    MENU = '''\nTIMER & STOPWATCH:\n1. Start Timer (countdown)\n2. Start Stopwatch\n3. Back to Main Menu\n'''
    while True:
        print(MENU)
        c = safe_input('Choice: ').strip()
        if c == '1':
            secs = safe_input('Enter seconds for countdown: ').strip()
            if not secs.isdigit():
                print('Please enter a positive integer.')
                continue
            secs = int(secs)
            try:
                while secs > 0:
                    print(f'Time left: {secs} sec', end='\r')
                    time.sleep(1)
                    secs -= 1
                print('\nTime is up!')
            except KeyboardInterrupt:
                print('\nCancelled.')
        elif c == '2':
            print('Stopwatch started. Press Enter to stop.')
            start = time.time()
            try:
                safe_input('')
            except Exception:
                pass
            elapsed = time.time() - start
            print(f'Elapsed: {elapsed:.2f} seconds')
        elif c == '3' or c == '':
            break
        else:
            print('Invalid choice')