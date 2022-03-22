from datetime import date


class Note:
    '''
        A simple Note class.
    '''

    def __init__(self, memo: str, tags='') -> None:
        """
        Args:
            memo (str): an entry.
            tags (str): a tags of entry.
        """
        self.memo = memo
        self.tags = tags
        self.creation_date = date.today()

    def match(self, search_filter: str):
        """
            Returns True if entry contains search_filter
            and False otherwise.
        Args:
            search_filter (str): a search search_filter.
        Returns:
            Boolean.
        """
        return search_filter in self.memo or search_filter in self.tags


class Notebook:
    """
        A notebook class.
    """
    def __init__(self):
        '''Initialize a notebook with an empty list.'''
        self.notes = []

    def search(self, search_filter: str):
        """
            Searches for a notes with certain contents.
        Args:
            search_filter (str): a search_filter of notes.
        Returns:
            list: a list of all notes found.
        """
        return [note for note in self.notes if note.match(search_filter)]

    def new_note(self, memo:str, tags=''):
        """
        Adds a new note to notes list. Returns nothing.
        Args:
            memo (str): an entry of the note.
            tags (str, optional): a tags of the note. Defaults to ''.
        """
        self.notes.append(Note(memo, tags))

    def modify_memo(self, note_id:int, new_memo:str):
        """
            Changes a note to a new value, id remains unchanged.
        Args:
            note_id (int): a not id.
            new_memo (str): a new entry to save.
        """
        assert(note_id > 0 and note_id < len(self.notes))
        self.notes[note_id].memo = new_memo

    def modify_tags(self, note_id:int, new_tags:str):
        """
            Changes tags of the note by id.
        Args:
            note_id (int): _description_
            new_tags (str): _description_
        """        
        assert(note_id > 0 and note_id < len(self.notes))
        self.notes[note_id].tags = new_tags
