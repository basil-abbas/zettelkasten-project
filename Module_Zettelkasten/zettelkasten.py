from Module_Zettelkasten.zettelkasten_data import ZettelkastenNote
from Module_SourceNotes.source_note_data import SourceNote

import uuid
from datetime import datetime



#Need to implement Knowledge Graph (DAG/Network)

class Zettelkasten():
    def __init__(self, source_note_object):
        self.source_noteOb = source_note_object
        self.note_status = "literature" #default all notes start as literature notes
        self.user_note = ""



    def data_instance(self):
        return ZettelkastenNote (
            id = str(uuid.uuid4()),
            source_note_id = self.source_noteOb.id,
            note_status_id = self.note_status,
            note_contents = self.user_note,
            created_at = datetime.now()
        )

    
    def add_note(self, user_input): # aka literature notes
        self.user_note = user_input

        return self.data_instance()

    def take_reference_notes(self, user_input):
        print(f"These notes are all from: {self.source_noteOb.source_url}") #temporary line of code
        self.user_note = user_input # the user here after done taking notes will submit in a nutshell what they have understood so far.
        self.note_status = "reference"

        return self.data_instance()
        

        
# this needs to be where after the user is done adding notes and stuff they review all the literature notes they have and then they select which ones 
# are the most important and which ones need to get deleted and made permanent    
    def make_permanent_notes(self): 
        pass
