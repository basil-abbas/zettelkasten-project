from dataclasses import dataclass
from datetime import datetime

@dataclass
class ZettelkastenNote:
    id: str #unique note ID
    source_note_id: str #Which SourceNote this came from
    note_status_id: str #what kind of note is it? "literature notes" | "bibliographical" | "permanent"
    title: str #Note title?
    note_contents: str #the notes the user made
    created_at: datetime


    