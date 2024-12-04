
from json import load

f=open("C:\\Users\\HP\\Desktop\\python works\\datasets\\books.json")

data=load(f)

# for book in data:
#     print(book)


# all_titles=[book.get("title") for book in data] (to fetch all titles)
# print(all_titles)


# page_filter = [book.get("title") for book in data if book.get("pages")<250] #(to fetch books of pages<250)
# # print(page_filter)


# genres_filter=[book.get("genre") for book in data]
# print(set(genres_filter))


# all_genres=[book.get("genre") for book in data]

# genre_count={genre:all_genres.count(genre) for genre in all_genres}
# print(genre_count)



# costly_book=max(data,key=lambda d:d.get("price"))
# print(costly_book)


#author with more than one book
authors=[book.get("author") for book in data]
author_count={auth:authors.count(auth) for auth in authors}
print([k for k,v in author_count.items() if v>1])
