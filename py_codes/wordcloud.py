from bs4 import BeautifulSoup
import urllib.request
from wordcloud import WordCloud
import matplotlib.pyplot as plt

r = urllib.request.urlopen('https://www.lyrics.com/lyric/15059595/Beyonc%C3%A9/If+I+Were+a+Boy')
soup = BeautifulSoup(r.read(),"html.parser")
text = soup.findAll("pre", {"id": "lyric-body-text"})[0].text

print(text)

wordcloud = WordCloud().generate(text)

#display generated image
plt.figure()
plt.imshow(wordcloud, interpolation="bilinear")
plt.axis("off")
plt.show()


