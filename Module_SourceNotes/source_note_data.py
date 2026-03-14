from dataclasses import dataclass
from datetime import datetime

@dataclass
class SourceNote:
    id: str
    title: str
    source_type: str  # "youtube" | "pdf" | "manual"
    source_url: str | None
    transcript: str
    created_at: datetime


#only explanation I really have for this class is that it is a way to simplify the code, basically the job for source_notes is 
# just to extract and then save a "instance" of that information here. And then later in main or somewhere else all we have to do is access 
# that data from here and not worry about source_notes.py again. If you want you can try and change this up or look into it yourself i don't 
# understand it much. 