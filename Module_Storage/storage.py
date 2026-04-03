import sqlite3
from Module_SourceNotes.source_note_data import SourceNote
from datetime import datetime


class DatabaseManager():
    def __init__(self, db_name="zettelkasten.db") -> None: 
        self.db_name = db_name
        self.init_db()

    def get_connection(self): #connects the sqlite3 database to the database class
        return sqlite3.connect(self.db_name)
    
    def init_db(self):#datatabl structure
        with self.get_connection() as connect:
            cursor = connect.cursor()
            cursor.execute("""
            CREATE TABLE IF NOT EXISTS source_notes(
                id TEXT PRIMARY KEY,
                title TEXT NOT NULL,
                source_type TEXT NOT NULL,
                source_url TEXT, 
                transcript TEXT NOT NULL, 
                created_at TEXT NOT NULL)
            """)
            
    def save_source_notes(self, note:SourceNote):#instert the user input with relevent atributes to the data table
        with self.get_connection() as connect:
            cursor = connect.cursor()
            cursor.execute("""
            INSERT INTO source_notes (id, title, source_type, source_url, transcript, created_at)
            VALUES (?,?,?,?,?,?)
            """, (note.id,
                  note.title,
                  note.source_type,
                  note.source_path,
                  note.transcript,
                  note.created_at.isoformat()))

    def get_all_notes(self):
        with self.get_connection() as connect:
            cursor = connect.cursor()
            cursor.execute("""
            SELECT id, title FROM source_notes
            """
            )
            user_notes = cursor.fetchall() 
            return user_notes

    def get_note_by_id(self, id:str):
        with self.get_connection() as connect:
            cursor = connect.cursor()
            cursor.execute("""
            SELECT transcript, created_at, source_url FROM source_notes WHERE id = ?
            """, (id,))
            note = cursor.fetchone()
            return note