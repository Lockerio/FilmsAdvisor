from src.models import Comment


class CommentSerializer:
    def __init__(self, session):
        self.session = session

    def get_one(self, comment_id):
        return self.session.query(Comment).get(comment_id)

    def get_all(self):
        return self.session.query(Comment).all()

    def create(self, data):
        comment = Comment(**data)
        self.session.add(comment)
        self.session.commit()
        return comment

    def update(self, comment):
        self.session.add(comment)
        self.session.commit()
        return comment

    def delete(self, comment_id):
        comment = self.get_one(comment_id)
        self.session.delete(comment)
        self.session.commit()
