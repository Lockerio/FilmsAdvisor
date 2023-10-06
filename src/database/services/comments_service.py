from src.serializers.comments_serializer import CommentSerializer


class CommentService:
    def __init__(self, serializer: CommentSerializer):
        self.serializer = serializer

    def get_one(self, comment_id):
        return self.serializer.get_one(comment_id)

    def get_all(self):
        return self.serializer.get_all()

    def update(self, data):
        return self.serializer.update(data)

    def create(self, data):
        return self.serializer.create(data)

    def delete(self, comment_id):
        self.serializer.delete(comment_id)
