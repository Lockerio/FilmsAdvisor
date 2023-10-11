from sqlalchemy.orm import Session

from src.database.database import engine
from src.database.serializers.films_serializer import FilmSerializer
from src.database.serializers.users_serializer import UserSerializer

from src.database.services.films_service import FilmService
from src.database.services.users_service import UserService


session = Session(bind=engine)


filmSerializer = FilmSerializer(session)
userSerializer = UserSerializer(session)

filmService = FilmService(filmSerializer)
userService = UserService(userSerializer)
