import Module_SourceNotes.source_notes as source_notes_module


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

        choice = input("Select option 1, 2, 3, or 4").strip()

        if choice == "1":
            url = input("Enter your url:").strip()
            note = source_notes_module.SourceNotes(url)
            note.youtube_transcript()
            print(note.completed_sourcenotes)
        elif choice == "2":
            path = input("Enter local PDF path (e.g. C:/docs/file.pdf): ").strip()
            note = source_notes_module.SourceNotes()
            note.pdf_transcript(path)
        elif choice == "3":
            url = input("Enter PDF URL: ").strip()
            note = source_notes_module.SourceNotes()
            note.pdf_transcript(url)
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid option, please pick from 1, 2, 3, or 4")

if __name__ == "__main__":  
    main()