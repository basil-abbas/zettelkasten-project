import sqlite3
from Module_SourceNotes.source_note_data import SourceNote
from datetime import datetime
from Module_Zettelkasten.zettelkasten_data import ZettelkastenNote
import uuid


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
                source_path TEXT, 
                transcript TEXT NOT NULL, 
                created_at TEXT NOT NULL)
            """)

            cursor.execute("""
            CREATE TABLE IF NOT EXISTS links(
                id TEXT PRIMARY KEY,
                from_id TEXT NOT NULL,
                to_id TEXT NOT NULL,
                relation_type TEXT NOT NULL)
            """)

            cursor.execute("""
            CREATE VIRTUAL TABLE IF NOT EXISTS notes_fts 
                USING fts5(title, transcript ,id);""") #fts5 is a full text search engine that allows for fast search of the database  

            cursor.execute("""
            CREATE TABLE IF NOT EXISTS zettelkasten_notes(
                id TEXT PRIMARY KEY,
                source_note_id TEXT NOT NULL,
                note_status_id TEXT NOT NULL,
                note_contents TEXT NOT NULL,
                created_at TEXT NOT NULL)
            """)

    def save_source_notes(self, note:SourceNote):#instert the user input with relevent atributes to the data table
        with self.get_connection() as connect:
            cursor = connect.cursor()
            cursor.execute("""
            INSERT INTO source_notes (id, title, source_type, source_path, transcript, created_at)
            VALUES (?,?,?,?,?,?)
            """, (note.id,
                  note.title,
                  note.source_type,
                  note.source_path,
                  note.transcript,
                  note.created_at.isoformat()))
            cursor.execute("""INSERT INTO notes_fts(id, title, transcript) VALUES (?, ?, ?)
            """, (note.id, note.title, note.transcript))

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
            SELECT transcript, created_at, source_path FROM source_notes WHERE id = ?
            """, (id,))
            note = cursor.fetchone()
            return note
    
    def create_link(self, from_id:str, to_id:str, relation_type:str):
        with self.get_connection() as connect:
            cursor = connect.cursor()
            id = str(uuid.uuid4())
            cursor.execute("""
            INSERT INTO links (id, from_id, to_id, relation_type)
            VALUES (?,?,?,?)
            """, (id, from_id, to_id, relation_type))

    def get_links(self, note_id:str):
        with self.get_connection() as connect:
            cursor = connect.cursor()
            cursor.execute("""
            SELECT from_id, to_id, relation_type FROM links WHERE to_id = ? OR from_id = ?
            """, (note_id, note_id))
            links = cursor.fetchall()
            return links

    def search_notes(self, query:str):
        with self.get_connection() as connect:
            cursor = connect.cursor()
            cursor.execute("""
            SELECT * FROM notes_fts WHERE notes_fts MATCH ?
            """
            , (query,))
            notes = cursor.fetchall()
            return notes

    def save_zettelkasten_note(self, note:ZettelkastenNote):
        with self.get_connection() as connect:
            cursor = connect.cursor()
            cursor.execute("""
            INSERT INTO zettelkasten_notes (id, source_note_id, note_status_id, note_contents, created_at)
            VALUES (?,?,?,?,?)
            """, (note.id,
                  note.source_note_id,
                  note.note_status_id,
                  note.note_contents,
                  note.created_at.isoformat()))
