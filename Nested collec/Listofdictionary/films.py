
movies = [
    # Malayalam Movies
    {
        "title": "Drishyam",
        "year": 2013,
        "language": "Malayalam",
        "genres": ["Crime", "Drama", "Thriller"],
        "rating": 8.6
    },
    {
        "title": "Premam",
        "year": 2015,
        "language": "Malayalam",
        "genres": ["Comedy", "Drama", "Romance"],
        "rating": 8.3
    },
    {
        "title": "Bangalore Days",
        "year": 2014,
        "language": "Malayalam",
        "genres": ["Comedy", "Drama", "Romance"],
        "rating": 8.3
    },
    # Tamil Movies
    {
        "title": "Kaala",
        "year": 2018,
        "language": "Tamil",
        "genres": ["Action", "Drama"],
        "rating": 7.3
    },
    {
        "title": "Vikram Vedha",
        "year": 2017,
        "language": "Tamil",
        "genres": ["Action", "Crime", "Thriller"],
        "rating": 8.4
    },
    {
        "title": "Super Deluxe",
        "year": 2019,
        "language": "Tamil",
        "genres": ["Drama", "Mystery", "Thriller"],
        "rating": 8.3
    },
    # Hindi Movies
    {
        "title": "Dangal",
        "year": 2016,
        "language": "Hindi",
        "genres": ["Action", "Biography", "Drama"],
        "rating": 8.4
    },
    {
        "title": "3 Idiots",
        "year": 2009,
        "language": "Hindi",
        "genres": ["Comedy", "Drama"],
        "rating": 8.4
    },
    {
        "title": "Gully Boy",
        "year": 2019,
        "language": "Hindi",
        "genres": ["Drama", "Music"],
        "rating": 8.0
    }
]

#q1 total no. of movies

count=len(movies)
# print(count)

#q2 movies with genre drama

genre_drama=[m.get("title") for m in movies if "Drama" in m.get("genres")]
# print(genre_drama)

#q3 latest movie

latest_movie=max(movies,key=lambda m:m.get("year"))
movie_year_filter=[m.get("title") for m in movies if m.get("year")==latest_movie.get("year")]
# print(movie_year_filter)

#q4 movie with highest rating

highest_rating=max(movies,key=lambda m:m.get("rating"))
# print(highest_rating.get("title"))

#q5 movies with language malayalam

mal_movie=[m.get("title") for m in movies if "Malayalam" in m.get("language")]
# print(mal_movie)

#q6 movies released after year 2016

movie_year=[m.get("title") for m in movies if m.get("year")>2016]
# print(movie_year)

#q7 movie with lowest rating

lowest_rating=min(movies,key=lambda m:m.get("rating"))
# print(lowest_rating.get("title"))

#q8 malayalam movies with genre action

genre_action=[m.get("title") for m in movies if "Action" in m.get("genres") and m.get("language")=="Malayalam"]
print(genre_action)

#q9 movies released in same year
movie_dict={}
for m in movies:

    release_year=m.get("year")
    if release_year in movie_dict:

        movie_dict.get(release_year).append(m.get("title"))
    
    else:

        movie_dict[release_year]=[m.get("title")]
# print(movie_dict)

#q10 oldest movie

oldest_movie=min(movies,key=lambda m:m.get("year"))
# print(oldest_movie.get("title"))

#q11 movie name with genres either drama or comedy 

movie_genre_filter=[m.get("title") for m in movies if m.get("genres")=="Drama" or m.get("genres")=="Comedy" ]
# print(movie_genre_filter)

# number of movies released in each year
years=[m.get("year") for m in movies]
year_count={y:years.count(y) for y in years}
# print(year_count)

# print all genres
genre=set()
for m in movies:

    for g in m.get("genres"):

        genre.add(g)

# print(genre)

#number of movies in each genre

all_genres=[g for m in movies for g in m.get("genres")]
genre_count={g:all_genres.count(g) for g in all_genres}
# print(genre_count)


#sort all movie titles

sorted_movies=sorted(movies,key=lambda mov:mov.get("title"))
sorted_movie_title=[m.get("title") for m in sorted_movies]
print(sorted_movie_title)
        