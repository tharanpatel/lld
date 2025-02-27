from users import User
from questions import Question

class StackOverflow:
    def __init__(self):
        self.users:list[User] = []
        self.questions:list[Question] = [] 
    
    def add_user(self, username):
        new_user = User(username)
        self.users.append(new_user)
    
    def get_user(self, username):
        for user in self.users:
            if user.username == username:
                return user
        
        print(f"User {username} does not exist")

    def ask_question(self, question):
        author = question.get_author()
        author.add_questions_asked(question)
        self.questions.append(question)
    
    def get_question_by_title(self, title):
        for question in self.questions:
            if question.get_title() == title:
                print(question.get_content())
                return question.content
        
        print("This question does not exist.")
    
    def get_question_by_tags(self, tag) -> list[Question]:
        print(f"------------Questions with tag: {tag}------------")
        questions_with_tag = []
        for question in self.questions:
            if tag in question.tags:
                questions_with_tag.append(question.title)
        
        [print(q.get_title()) for q in questions_with_tag]
        print(f"-------------------------------------------------")
        return questions_with_tag if questions_with_tag else f"There are no questions with the tag {tag}."

    def get_question_by_user(self, user) -> list[Question]:
        print(f"------------Questions from: {user.username}------------")
        users_questions = user.get_questions_asked()
        
        [print(q.get_title()) for q in users_questions]
        print(f"-------------------------------------------------")
        return users_questions if users_questions else "The user has no questions posted."
    
    def get_question_comments(self, question):
        print(f"------------Comments for: {question.get_title()}------------")
        question.get_comments()
        print(f"-------------------------------------------------")


    def get_question_answers(self, question):
        print(f"------------Answers for: {question.get_title()}------------")
        question.get_answers()
        print(f"-------------------------------------------------")
    
    def get_user_reputation(self, user):
        print(f"{user.username} has a reputation of {user.get_reputation()}")