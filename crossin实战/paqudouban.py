import urllib

response = urllib.urlopen('http://api.douban.com/v2/movie/top250')

data = response.read()

print(data)