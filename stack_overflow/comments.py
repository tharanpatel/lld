from contribution import Contribution
from typing import Optional

class Comment(Contribution):
    def __init__(self, author, content:str):
        super().__init__(author, content)
        self.replies = []
    
    def add_reply(self, comment):
        self.replies.append(comment)
    
    def remove_reply(self, comment):
        self.replies.remove(comment)
    
    def get_replies(self):
        if not self.replies:
            return
        
        for comment in self.replies:
            print(f"{comment.get_content()} @{self.author.username}")
            comment.get_replies()

