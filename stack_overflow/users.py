from comments import Comment
from questions import Question

class User:
    def __init__(self, username:str):
        self.username = username
        self.questions_asked:list[Question] = []
        self.comments_given:list[Comment] = []

    def get_username(self):
        return self.username
    
    def get_reputation(self):
        reputation = 0
        for question in self.questions_asked:
            reputation += question.get_rating()
        
        for comment in self.comments_given:
            reputation += comment.get_rating()
        
        return reputation
    
    def add_questions_asked(self, question):
        self.questions_asked.append(question)
    
    def get_questions_asked(self):
        return self.questions_asked
