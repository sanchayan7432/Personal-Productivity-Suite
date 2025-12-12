"""Entry point for the Personal Productivity Suite."""
import sys
from modules import calculator, notes_manager, timer, file_organizer, unit_converter, backup, utils


MENU = '''
==========================================
PERSONAL PRODUCTIVITY SUITE
==========================================


MAIN MENU:
1. Calculator Tool
2. Notes Manager
3. Timer & Stopwatch
4. File Organizer
5. Unit Converter
6. Backup & Restore
7. Exit
'''




def main():
    utils.ensure_data_dirs()
    while True:
        print(MENU)
        try:
            choice = input('Enter your choice (1-7): ').strip()
        except (EOFError, KeyboardInterrupt):
            print('\nExiting...')
            sys.exit(0)
        if choice == '1':
            calculator.run()
        elif choice == '2':
            notes_manager.run()
        elif choice == '3':
            timer.run()
        elif choice == '4':
            file_organizer.run()
        elif choice == '5':
            unit_converter.run()
        elif choice == '6':
            backup.run()
        elif choice == '7':
            print('Goodbye! Have a productive day!')
            break
        else:
            print('Invalid choice — please enter a number between 1 and 7.')




if __name__ == '__main__':
    main()