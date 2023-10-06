import hashlib

from src.serializers.users_serializer import UserSerializer


class UserService:
    def __init__(self, serializer: UserSerializer):
        self.serializer = serializer

    def get_one(self, user_id):
        return self.serializer.get_one(user_id)

    def get_all(self):
        return self.serializer.get_all()

    def update(self, data):
        password = data["hashed_password"]
        hashed_password = self.hash_password(password)
        data["hashed_password"] = hashed_password
        return self.serializer.update(data)

    def create(self, data):
        password = data["hashed_password"]
        hashed_password = self.hash_password(password)
        data["hashed_password"] = hashed_password
        return self.serializer.create(data)

    def delete(self, user_id):
        self.serializer.delete(user_id)

    @staticmethod
    def hash_password(password):
        sha256 = hashlib.sha256()
        password_bytes = password.encode('utf-8')
        sha256.update(password_bytes)
        hashed_password = sha256.hexdigest()
        return hashed_password
