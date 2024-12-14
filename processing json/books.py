from json import load

f=open("dataset/books.json")

data=load(f)

# for book in data:

# print(book)


#print titles of all books

# all_titles=[book.get("title") for book in data]

# print(all_titles)

# print books with pages less than 250

# page_filter=[book.get("title") for book in data if book.get("pages")<250]

# print(page_filter)

# print all genres

all_genres=[book.get("genre") for book in data]

# print(set(all_genres))

# print genre count

genre_count={genre:all_genres.count(genre) for genre in all_genres}

# print(genre_count)

# print costly book 

costly_book=max(data,key=lambda c:c.get("price"))

# print(costly_book)

# print authors with more than one book

all_authors=[book.get("author") for book in data]

author_count={author:all_authors.count(author) for author in all_authors}

print([k for k,v in author_count.items() if v>1])



