# import Module_SourceNotes.source_notes as SourceNotes_Extractor
from Module_SourceNotes import source_notes, source_note_data


# Test to use for now: https://www.youtube.com/watch?v=g2-_pnmhO4A&list=PLyxTU7oQdPUUaTxPYdGe7x_V03x2SI5Zf&index=3


def main():
    print("\n" * 5)
    print("Welcome to the Zettelkasten Note Taking App")
    while True: 
        print("--------------------------------------------")
        print("1. YouTube transcript")
        print("2. PDF (local file Path)")
        print("3. PDF (URL)")
        print("4. Quit")
        print("--------------------------------------------")

        choice = input("Select option 1, 2, 3, 4, or 5: ").strip()

        if choice == "1":
            url = input("Enter your url:").strip()
            note = source_notes.SourceNotes_Extractor()
            extract = note.youtube_transcript(url)
            print(note.completed_sourcenotes) #The following lines exists for us to see that the transcript was achieved.
            print(extract.title)
            print(extract.source_type)
            print(extract.created_at)

        elif choice == "2":
            path = input("Enter local PDF path (e.g. C:/docs/file.pdf): ").strip()
            note = source_notes.SourceNotes_Extractor()
            note.pdf_transcript(path)

        elif choice == "3":
            url = input("Enter PDF URL: ").strip()
            note = source_notes.SourceNotes_Extractor()
            note.pdf_transcript(url)

        elif choice == "4":
            user_text = input("Paste your copied text: ")
            note = source_notes.SourceNotes_Extractor()
            extract = note.manual_text_transcript(user_text)
            print(extract.title)

        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid option, please pick from 1, 2, 3, 4, or 5")

if __name__ == "__main__":  
    main()