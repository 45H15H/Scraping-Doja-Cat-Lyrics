
albumURLs = ["https://genius.com/albums/Doja-cat/Planet-her-deluxe",
             "https://genius.com/albums/Doja-cat/Planet-her",
             "https://genius.com/albums/Doja-cat/Streets-remixes",
             "https://genius.com/albums/Doja-cat/Hot-pink-japan-version",
             "https://genius.com/albums/Doja-cat/Hot-pink",
             "https://genius.com/albums/Doja-cat/Amala-deluxe-version",
             "https://genius.com/albums/Doja-cat/Amala",
             "https://genius.com/albums/Doja-cat/Purrr-ep"]

albums = ["Planet Her (Deluxe)",
          "Planet Her",
          "Streets (Remixes)",
          "Hot Pink (Japan Version)",
          "Hot Pink",
          "Amala (Deluxe Version)",
          "Amala",
          "Purrr (EP)"]



from bs4 import BeautifulSoup
import lxml
import requests

for _ in range(len(albumURLs)):

    link = albumURLs[_]
    html = requests.get(link).text
    soup = BeautifulSoup(html, 'lxml')

    s = soup.find_all("div", class_ = "chart_row-content")

    album = soup.find("div", class_ = "header_with_cover_art-primary_info").h1.text.strip()
    print(album)

    trackList = [(j.strip()[:-6]).strip().replace("\xa0", " ") for j in [i.text for i in s]]
    print(trackList)
    print(len(trackList))

import pandas as pd

Doja = pd.DataFrame([trackList])
