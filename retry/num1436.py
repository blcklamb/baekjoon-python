endMovieList = ['666']
endMovie = '666'
def endMovieAdd(movieName, movieList):
    if movieName not in movieList:
        movieList.append(movieName)
for i in range(1, 10):
    endMovie='666'
    endMovie=str(i)+endMovie
    endMovieAdd(endMovie, endMovieList)
for i in range(1, 10):
    endMovie='666'
    endMovie=endMovie+str(i)
    endMovieAdd(endMovie, endMovieList)

endMovieList.remove('666')
print(endMovieList)

endMovieList2=[]

for j in endMovieList:
    for i in range(1, 10):
        endMovie=str(i)+j
        endMovieAdd(endMovie, endMovieList2)
    for i in range(1, 10):
        endMovie=j+str(i)
        endMovieAdd(endMovie, endMovieList2)

endMovieList3 = []

for j in endMovie:
    for i in range(10, 100):
        endMovie=str(i)+j
        endMovieAdd(endMovie, endMovieList2)
    for i in range(0, 10):
        for k in range(0, 10):
            endMovie=j+str(i)+str(j)
            endMovieAdd(endMovie, endMovieList2)
print(endMovieList2)
endMovieList.extend(endMovieList2)
endMovieList.append('666')

intEndMovieList = [int(x) for x in endMovieList]
intEndMovieList.sort()
print(intEndMovieList)
