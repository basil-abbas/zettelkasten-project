import youtube_transcript_api
from youtube_transcript_api import YouTubeTranscriptApi

def get_video_transcript(video_url):
    try:
        if "v=" in video_url:
            video_id = video_url.split("v=")[1].split("&")[0]
        else:
            video_id = video_url.split("/")[-1]
            
        print(f"Attempting to fetch transcript for ID: {video_id}")
        
        ytt = YouTubeTranscriptApi()
        transcript_data = ytt.fetch(video_id)
        
        # Join each transcript chunk on its own line for readability
        full_text = "\n".join([item.text for item in transcript_data])
        return full_text
        
    except Exception as e:
        return f"Error: {str(e)}"

if __name__ == "__main__":
    test_url = "https://www.youtube.com/watch?v=g2-_pnmhO4A&list=PLyxTU7oQdPUUaTxPYdGe7x_V03x2SI5Zf&index=3"
    final_output = get_video_transcript(test_url)
    
    print(f"\nTotal transcript length: {len(final_output)} characters")
    print("\n--- Full Transcript ---")
    print(final_output)  # no slicing, prints everything

    # Save to file
    with open("transcript.txt", "w", encoding="utf-8") as f:
        f.write(final_output)
    print(f"Saved to transcript.txt ({len(final_output)} characters)")  