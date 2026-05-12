class Book:
    # We initialise with all of our attributes
    # Each column in the table should have an attribute here
    def __init__(self,title, author, id = None):
        self.id = id
        self.title = title
        self.author = author

    # This tells Python how to compare two Books. 
    def __eq__(self, other):
        return self.__dict__ == other.__dict__

    # This controls what you see when you print.
    def __repr__(self):
        return f"Book({self.id}, {self.title}, {self.author})"