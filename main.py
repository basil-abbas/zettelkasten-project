import modules.source_notes as source_notes_module


# test_url = https://www.youtube.com/watch?v=g2-_pnmhO4A&list=PLyxTU7oQdPUUaTxPYdGe7x_V03x2SI5Zf&index=3


print("Welcome to the Zettelkasten Note Taking App\nPlease enter some form of source notes (URL, Video, etc.)")

user_input = input("Enter the source notes url: ")

current_note = source_notes_module.SourceNotes(user_input)

current_note.youtube_transcript()



