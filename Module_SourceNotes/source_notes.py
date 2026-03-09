from fileinput import filename
from youtube_transcript_api import YouTubeTranscriptApi
import yt_dlp #pip install yt-dlp    <----- import statement
import re
import os, shutil #To save the files in a specific folder

class SourceNotes:
    def __init__(self, user_input=""):
        self.video_url = user_input
        self.filename = ""

# -----------------------------------------YOUTUBE_TRANSCRIPTS_CODE-----------------------------------------
    def youtube_vid_title(self):
        ydl_opts = {'quiet': True}

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(self.video_url, download=False)
            yt_title = info.get('title')

        yt_title = re.sub(r'[<>:"/\\|?*\x00-\x1F]+', "_", yt_title)
        return yt_title.strip().strip(".")


    def youtube_transcript(self):
        if "v=" in self.video_url:
            video_id = self.video_url.split("v=")[1].split("&")[0] #Takes the Yt url and splits the list into two halves, where everything between v= is 0 and after is 1 and then it's repeated.
        else:
            video_id = self.video_url.split("/")[-1] #does the same thing splitting the link everywhere with a '/' and then grabbing the last element which is the id
        

        youtube = YouTubeTranscriptApi()
        transcript = youtube.fetch(video_id) #returns a list of transcript segments objects: .text, .start, .duration

        completed_transcript = " ".join([item.text for item in transcript]) #fix the segments objects and form them into a completed transcript

        title = self.youtube_vid_title() or video_id

        self.filename = f"{title}-Youtube_transcript.txt" #custom file name

        with open(self.filename, "w", encoding="utf-8") as transcript_file:
            transcript_file.write(completed_transcript)
        print(f"File has been saved: {self.filename}")

        self.save_transcript()
        

    # May need to update code for this not sure
    def save_transcript(self):
        try:
            shutil.move(self.filename,"Module_SourceNotes\Exported_Transcripts") # takes in 2 parameters, the name of the file, and where you are moving it to
            print(self.filename)
            print(f"And was able to move {self.filename} to its destination")
        except FileNotFoundError:
            print(f"Error: The source file '{self.filename}' was not found")
        except Exception as e:
            print(f"Found error: {e}")



# -----------------------------------------PDF_TRANSCRIPTS_CODE-----------------------------------------

    def pdf_transcript(self):
        pass