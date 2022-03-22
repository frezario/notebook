'''
    The Menu class implementation.
'''
import sys
from notebook import Notebook

class Menu:
    '''The menu class'''
    def __init__(self):
        self.notebook = Notebook()
        self.choices = {
            "1": self.show_notes,
            "2": self.search_notes,
            "3": self.add_note,
            "4": self.modify_note,
            "5": self.quit
        }

    def display_menu(self):
        print("""
        Notebook Menu
        1. Show all Notes
        2. Search for Notes
        3. Add Note
        4. Modify Note
        5. Exit
        """)

    def run(self):
        '''Executes main menu.'''
        while True:
            self.display_menu()
            choice = input("Enter an option: ")
            action = self.choices.get(choice)
            if action:
                action()
            else:
                print("{0} is not a valid choice".format(choice))

    def show_notes(self, notes=None):
        if not notes:
            notes = self.notebook.notes
        for note in notes:
            print("{0}: {1}\n{2}".format(
                note.id, note.tags, note.memo))

    def search_notes(self):
        search_filter = input("Search for: ")
        notes = self.notebook.search(search_filter)
        self.show_notes(notes)

    def add_note(self):
        memo = input("Enter a memo: ")
        tags = input("Enter tags: ")
        self.notebook.new_note(memo, tags)
        print("Your note has been added succesfully.")

    def modify_note(self):
        while True:
            try:
                id = int(input("Enter a note id: "))
                memo = input("Enter a memo: ")
                tags = input("Enter tags: ")
                self.notebook.modify_memo(id, memo)
                self.notebook.modify_tags(id, tags)
                break
            except (AssertionError, ValueError):
                print('Pls, enter the correct id value.')

    def quit(self):
        print("Bye!")
        sys.exit(0)

if __name__ == "__main__":
    Menu().run()
