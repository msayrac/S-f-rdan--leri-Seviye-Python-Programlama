
# special methods

class Movie():
    def __init__(self,title,director,duration):
        self.title = title
        self.director = director
        self.duration = duration
        print("movie objesi olusturuldu constructor")
    
    def __str__(self):
        return f"{self.title} by {self.director}"
    
    def __len__(self):
        return self.duration


m = Movie("film adı","yonetmen adı",122)

print(m)
print(len(m))

