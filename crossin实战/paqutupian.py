import urllib.request
import web
import time
import os

def get_poster(id, url):
    pic = urllib.request.urlopen(url).read()
    file_name = 'static/poster/%d.jpg' %id
    f = open(file_name, "wb")
    f.write(pic)
    f.close()


db = web.database(dbn='sqlite', db='moviesite.db')
movies = db.select('movie')
count = 0
for movie in movies:
    get_poster(movie.id, movie.image)
    count += 1
    print(count, movie.title)
    time.sleep(2)
