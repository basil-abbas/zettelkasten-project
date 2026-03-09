from youtube_transcript_api import YouTubeTranscriptApi
import yt_dlp #pip install yt-dlp    <----- import statement
import re

def safe_filename(name: str) -> str:
    # Windows-invalid: <>:"/\|?* plus control chars; also trims trailing dots/spaces
    if not name:
        return ""
    name = re.sub(r'[<>:"/\\|?*\x00-\x1F]+', "_", name)
    return name.strip().strip(".")

class SourceNotes:
    def __init__(self, user_input=""):
        self.video_url = user_input



    
    def youtube_vid_title(self):
        ydl_opts = {'quiet': True}

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(self.video_url, download=False)
            yt_title = info.get('title')

        return safe_filename(yt_title)


    def youtube_transcript(self):
        if "v=" in self.video_url:
            video_id = self.video_url.split("v=")[1].split("&")[0] #Takes the Yt url and splits the list into two halves, where everything between v= is 0 and after is 1 and then it's repeated.
        else:
            video_id = self.video_url.split("/")[-1] #does the same thing splitting the link everywhere with a '/' and then grabbing the last element which is the id
        

        youtube = YouTubeTranscriptApi()
        transcript = youtube.fetch(video_id) #returns a list of transcript segments objects: .text, .start, .duration

        completed_transcript = " ".join([item.text for item in transcript]) #fix the segments objects and form them into a completed transcript

        title = self.youtube_vid_title() or video_id

        filename = f"{title}-Youtube_transcript.txt" #custom file name

        with open(filename, "w", encoding="utf-8") as transcript_file:
            transcript_file.write(completed_transcript)
        print(f"File has been saved: {filename}")



    




    

    def pdf_transcript(self):
        pass