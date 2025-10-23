import yt_dlp
import csv

def get_playlist_videos(playlist_url):
    ydl_opts = {
        'quiet': True,
        'extract_flat': True,  # Don't download videos, just extract metadata
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(playlist_url, download=False)
        entries = info.get('entries', [])

        video_urls = [f"https://www.youtube.com/watch?v={entry['id']}" for entry in entries]
        for url in video_urls:
            print(url)

        with open("video_links.csv", "w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            for url in video_urls:
                writer.writerow([url])  # each URL goes on its own line
        
        return video_urls


# Example
if __name__ == "__main__":
    pl_url = "https://www.youtube.com/playlist?list=PLKnIA16_Rmvbr7zKYQuBfsVkjoLcJgxHH"
    links = get_playlist_videos(pl_url)
    print(type(links))
