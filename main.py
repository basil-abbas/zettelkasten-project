import Module_SourceNotes.source_notes as source_notes_module


# Test to use for now: https://www.youtube.com/watch?v=g2-_pnmhO4A&list=PLyxTU7oQdPUUaTxPYdGe7x_V03x2SI5Zf&index=3

print("\n" * 5)
print("Welcome to the Zettelkasten Note Taking App\nPlease select some form of source notes (URL, Video, etc.)")

user_input = input("Enter the source notes url: ")

current_note = source_notes_module.SourceNotes(user_input)

current_note.youtube_transcript()




#-----------------NEW_TEST_CODE--------------------

# print("\n" * 5)
# print("Welcome to the Zettelkasten Note Taking App\nPlease select some form of source notes (Youtube URL, PDF, etc.)")

# user_input = input("Enter the source notes url: ")

# while True:
#     current_note = source_notes_module.SourceNotes()

#     if user_input == 'yt' or '1':
#         current_note.youtube_transcript(user_input)

#     elif user_input == 'pdf' or '2':
#         current_note.pdf_transcript()
#     else:
#         break


