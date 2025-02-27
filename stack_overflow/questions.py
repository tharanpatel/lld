from contribution import Contribution
from comments import Comment

class Question(Contribution):
    def __init__(self, author, title, content):
        super().__init__(author, content)
        self.title = title
        self.comments:list[Comment] = []
        self.answers:list[Comment] = []
        self.tags:list[str] = []
    
    def get_comments(self):
        if not self.comments:
            return
        
        for comment in self.comments:
            print(f"{comment.get_content()} @{self.author.username}")
            comment.get_replies()


    def get_answers(self):
        [print(answer.content) for answer in self.answers]
    
    def get_title(self):
        return self.title
    
    def add_comment(self, comment:Comment):
        self.comments.append(comment)

    def remove_comment(self, comment:Comment):
        self.comments.remove(comment)

    def add_answer(self, comment:Comment):
        self.answers.append(comment)

    def remove_answer(self, comment:Comment):
        self.answers.append(comment)

    def add_tag(self, tag:str):
        self.tags.append(tag)
    
    def contains_keyword(self, keyword):
        if keyword in self.content:
            return True
        return False

    def contains_tag(self, tag):
        if tag in self.tags:
            return True
        return False
    
