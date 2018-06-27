#!/usr/bin/env python
#-*-encoding:utf-8-*-

import web

urls = (
    '/','index',
    '/movie/(\d+)','movie',
    '/cast/(.*)','cast',
)

r = web.template.render('templates/')

db = web.database(dbn='sqlite', db='moviesite.db')

class index:
    def GET(self):
        movies = db.select('movie')
        return r.index(movies)

    def POST(self):
        data = web.input()
        print('data',type(data))
        condition = r'title like "%' + data.title + r'%"'
        movies = db.select('movie',  where=condition)
        print('movies',movies)
        return r.index(movies)

class movie:
    def GET(self, movie_id):

        movie_id = int(movie_id)
        movie = db.select('movie', where='id=$movie_id',vars=locals())[0]
        return r.movie(movie)

class cast:
    def GET(self, cast_name):
        print('cast_name',cast_name)
        condition = r'casts like "%' + cast_name + r'%"'
        movies = db.select('movie', where=condition)
        print(movies)
        return r.index(movies)





if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()
