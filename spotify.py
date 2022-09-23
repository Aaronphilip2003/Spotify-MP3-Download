import os
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from dotenv import load_dotenv, find_dotenv
import requests,sys,webbrowser,bs4
from pytube import Search
from pytube import YouTube

def split(string):
    return string.split()

def downloadVid(url):
    yt = YouTube(url)
    video = yt.streams.filter(only_audio=True).first()
    download_path=f"D:/mp3"
    out_file = video.download(download_path)

def returnVidID(songName):
    results=Search(songName)
    vid=[]
    for i in results.results:
        vid.append(i)
    searchElement1=vid[0]
    searchElement1string=str(searchElement1)

    vidIDLIST=[]
    vidIDLIST=split(searchElement1string)

    vidID=vidIDLIST[2][8:-1]
    return vidID

def createURLS(id):
    URL=f"https://www.youtube.com/watch?v={id}"
    return URL


# https://open.spotify.com/playlist/469e7pKWmqq5hH6xlbSdQX?si=c25eb9bd2d974115
load_dotenv(find_dotenv())
client_id = os.getenv("CLIENT_ID")
client_secret = os.getenv("CLIENT_SECRET")

sp = spotipy.Spotify(
    auth_manager=SpotifyClientCredentials(
        client_id=client_id, client_secret=client_secret
    )
)


playlist_code = input("Enter the playlist code:")
playlist_dict = sp.playlist(playlist_code)

no_of_songs = playlist_dict["tracks"]["total"]
tracks = playlist_dict["tracks"]
songs = tracks["items"]
songs_download=[]
artists_songs_download=[]


for i in range(0, len(songs)):
    songs_download.append(songs[i]["track"]["name"])
    artists_songs_download.append(songs[i]['track']['album']['artists'][0]['name'])

list=[]
for i in range(0,len(artists_songs_download)):
    list.append(f"{songs_download[i]} {artists_songs_download[i]}")

idsList=[]
urlList=[]
print("fetching Ids.......")
for i in list:
    idsList.append(returnVidID(i))

print("fetching URLs.......")

for i in idsList:
    urlList.append(createURLS(i))

print("downloading songs........")
for i in urlList:
    downloadVid(i)