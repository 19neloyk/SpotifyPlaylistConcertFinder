from bs4 import BeautifulSoup
import requests


def gather(url):
  site = requests.get(url)
  siteData = site.text.encode('utf-8').decode('ascii', 'ignore')
  soup = BeautifulSoup(siteData, "html.parser")
  print(soup.encode('utf-8').decode('ascii', 'ignore'))
  songs = soup.find_all("span",{"class" : "track-name"})
  print(len(songs))
  for song in songs:
      print('song')
      print(song.text.encode('utf-8').decode('ascii', 'ignore'))
  artists = soup.find_all("span",{"class" : "artists-albums"})
  print(len(artists))
  for artist in artists:
      print('artist')
      print(artist.text.encode('utf-8').decode('ascii', 'ignore'))

gather("https://open.spotify.com/playlist/79fgSrtau5uyI891QEiOMq")
