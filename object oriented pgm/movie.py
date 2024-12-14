class movie:

    title=str
    rating=float
    run_time=int
    director=str
    genre=str

    def set_movie(self,title,rating,run_time,director,genre):

        self.title=title
        self.rating=rating
        self.run_time=run_time
        self.director=director
        self.genre=genre

    def display(self):

        print(self.title,self.rating,self.run_time,self.director,self.genre)

movie1=movie()

movie1.set_movie("arm",8.4,129,"basil","action")

movie1.display()