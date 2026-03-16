from Module_SourceNotes.source_notes import SourceNotes_Extractor
from Module_Storage.storage import DatabaseManager

# Test to use for now: https://www.youtube.com/watch?v=g2-_pnmhO4A&list=PLyxTU7oQdPUUaTxPYdGe7x_V03x2SI5Zf&index=3


def main():
    db = DatabaseManager()
    print("\n" * 5)
    print("TEST VERSION FOR APP\nWelcome to the Zettelkasten Note Taking App\nPlease submit some form of source notes to get started")
    while True: 
        print("--------------------------------------------")
        print("1. YouTube transcript")
        print("2. Upload any file (.pdf, .docx, etc)")
        print("3. Raw Text")
        print("4. Quit")
        print("--------------------------------------------")

        choice = input("Select option 1, 2, 3, or 4: ").strip()

        if choice == "1":
            url = input("Enter your url:").strip()
            note = SourceNotes_Extractor().youtube_transcript(url)
            db.save_source_notes(note)
            print(note.title)
           

        elif choice == "2":
            # path = input("Enter local source path (.pdf, .docx, etc): ").strip()
            # if '.pdf' in path:
            #     note = SourceNotes_Extractor().pdf_transcript_v2(path)
            #     db.save_source_notes(note)
            #     print(note.transcript)
            # else:
            #     note = SourceNotes_Extractor().word_docx_transcript(path)
            #     db.save_source_notes(note)
            #     print(note.transcript)
            pass

        elif choice == "3":
            user_text = input("Paste your copied text: ")
            user_text_title = input("Enter title: ") #in the future we need to update this so after the user pastes some text an AI just gives a Title instead since rn this kinda tedious for the user
            note = SourceNotes_Extractor().manual_text_transcript(user_text, user_text_title)
            db.save_source_notes(note)
            print(note.title)

        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid option, please pick from 1, 2, 3, or 4")

if __name__ == "__main__":  
    main()


    