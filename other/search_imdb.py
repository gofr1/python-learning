import imdb

ia = imdb.IMDb()
search = ia.search_movie('Pulp Fiction')

print(search)