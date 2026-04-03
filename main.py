from Module_SourceNotes.source_notes import SourceNotes_Extractor
from Module_Storage.storage import DatabaseManager
from Module_Zettelkasten.zettelkasten import Zettelkasten

# Test to use for now: https://www.youtube.com/watch?v=g2-_pnmhO4A&list=PLyxTU7oQdPUUaTxPYdGe7x_V03x2SI5Zf&index=3




sources = [] #this is for a temporary holding place for all the source notes added since the storage module is stil being worked on. Once its done delete this.



def main():
    print("TEST VERSION FOR APP\nWelcome to the Zettelkasten Note Taking App")
    while True:
        print("--------------------------------------------")
        print("1. New Zettel")
        print("2. View Zettels") # saves users progress so they can come back [inside of here it will be like a libary of like chats of all the study sessions and in here we can have sub objects for flashcards/quizzes for specific chats]
        print("3. View Second Brain") # gonna show the mind map if I can even figure it out [would be a total mind map of all notes regardless of what chats to show connections]
        print("4. View Source Notes") # not sure what we can have this as
        print("5. Quit")
        print("--------------------------------------------")


        select_screen = input("Select a option: ")

        if select_screen == "1":
            choose_sources()
        
        elif select_screen == "2":
            pass

        elif select_screen == "3":
            pass

        elif select_screen == "4":
            source_notes = DatabaseManager().get_all_notes()
            for index, note in enumerate(source_notes, start=1):
                    print(f"{index}. {note[1]}") 
        
            try: 
                chosen_number = int(input("Enter number: "))
                if chosen_number < 1 or chosen_number > len(source_notes):
                    print("Invalid selection, please pick a valid number")
                else:
                    chosen_id = source_notes[chosen_number - 1][0]  # gets the UUID at that position
                    note = DatabaseManager().get_note_by_id(chosen_id)  
                    print(note[0])
            except ValueError:
                    print("Invalid input, please enter a number")
                    continue
                

        elif select_screen == "5":
            break   

        else:
            print("Invalid option, please pick from 1, 2, 3, 4, or 5")





def choose_sources():
    sources_database = DatabaseManager()
    print("\n" * 5)
    print("Please submit some form of source notes to get started")
    while True: 
        print("--------------------------------------------")
        print("1. YouTube transcript")
        print("2. Upload any file (.pdf, .docx, etc)")
        print("3. Raw Text")
        print("4. Done adding sources")
        print("--------------------------------------------")

        choice = input("Select option 1, 2, 3, 4, or 5: ").strip()

        if choice == "1":
            url = input("Enter your url:").strip()
            note = SourceNotes_Extractor().extract_transcript(url)
            sources_database.save_source_notes(note)  
            #sources.append(note) # just for test for visuals delete this later
           

        elif choice == "2":
            path = input("Enter local source path (.pdf, .docx, etc): ").strip()
            note = SourceNotes_Extractor().extract_transcript(path)
            sources_database.save_source_notes(note)
            #sources.append(note)


        elif choice == "3":
            user_text = input("Paste your copied text: ")
            user_text_title = input("Enter title: ") #in the future we need to update this so after the user pastes some text an AI just gives a Title instead since rn this kinda tedious for the user
            note = SourceNotes_Extractor().manual_text_transcript(user_text, user_text_title)
            sources_database.save_source_notes(note)
            #sources.append(note)

        elif choice == "4":
            take_notes()
            break


        # elif choice == "5":
        #     print("Goodbye!")
        #     break
        else:
            print("Invalid option, please pick from 1, 2, 3, 4, or 5")


def take_notes():
    notes_database = DatabaseManager()

    print("Here is the simplified sources:")
    print("\n" * 5)
    
    if not sources or sources[0] is None:
        print("No valid sources were added into the temporary list to view transcripts")
        return
    else:
        print(sources[0].transcript)

    while True:
        print("--------------------------------------------")
        print("1. Add notes")
        print("2. Done")
        print("3. Save Progress") # eventually will quit and save progress for the user so they can come back later [may not need to be a button but just whenever the user closes the program or smth else]
        print("--------------------------------------------") 
        select_screen = input("Select option 1, 2 or 3: ")

        if select_screen == "1":
            user_input = input("Type here: ")
            user_note = Zettelkasten(sources[0]).add_note(user_input) # other than the user input the other thing this line of code takes in is a source note object which will later be changed after the Storage Module is complete
            # notes_database.user_note(user_note) ----> add method for this
            
        elif select_screen == "2":
            user_input = input("What did you learn in a nutshell?\n")
            reference_note = Zettelkasten(sources[0]).take_reference_notes(user_input)

        elif select_screen == "3":
            break

        else:
            print("Invalid option, select again")





if __name__ == "__main__":  
    main()


    