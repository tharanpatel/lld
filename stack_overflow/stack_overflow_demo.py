from stack_overflow import StackOverflow
from questions import Question
from comments import Comment

class StackOverflowDemo:
    def run():
        system = StackOverflow()

        system.add_user("tharan")
        system.add_user("mike")
        system.add_user("john")
        tharan = system.get_user("tharan")
        mike = system.get_user("mike")
        john = system.get_user("john")

        question1 = Question(tharan, "Is stack overflow bad?", "Why is stack overflow so bad?")
        question1.add_tag("stack overflow")
        answer1 = Comment(mike, "Because DeepSeek is better!")
        comment1 = Comment(mike, "Whats the point of this question.")
        reply1 = Comment(tharan, "Because this site keeps getting worse.")
        reply_to_reply1 = Comment(mike, "Sure thing pal.")
        reply2 = Comment(john, "Thats a great question.")

        comment1.add_reply(reply1)
        reply1.add_reply(reply_to_reply1)
        comment1.add_reply(reply2)

        question1.add_answer(answer1)
        question1.add_comment(comment1)
        question1.upvote()
        question1.upvote()
        question1.upvote()

        question2 = Question(tharan, "How to convert int to float?", "What is the python method to do this?")


        system.ask_question(question1)
        system.ask_question(question2)
        system.get_question_by_user(tharan)
        system.get_question_answers(question1)
        system.get_question_comments(question1)
        system.get_user_reputation(tharan)

if __name__ == "__main__":
    StackOverflowDemo.run()