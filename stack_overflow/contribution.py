class Contribution:
    def __init__(self, author, content):
        self.author = author
        self.content = content
        self.rating = 0

    def get_author(self):
        return self.author

    def get_content(self):
        return self.content
    
    def upvote(self):
        self.rating += 1

    def downvote(self):
        self.rating -= 1

    def get_rating(self):
        return self.rating