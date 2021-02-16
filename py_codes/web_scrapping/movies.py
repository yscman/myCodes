import tmdbsimple as tmdb
from api_key import api_key

tmdb.API_KEY = api_key

movie = tmdb.Movies(603)
response = movie.info()
print(movie.title)
print(movie.budget)

search = tmdb.Search()
response = search.movie(query='Matrix')
for s in search.results:
    #print(s['popularity'])
    print(s['budget'])

