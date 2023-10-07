from sqlalchemy.orm import Session
from database import engine

from src.database.serializers.films_serializer import FilmSerializer

from src.database.services.films_service import FilmService


session = Session(bind=engine)


filmSerializer = FilmSerializer(session)

filmService = FilmService(filmSerializer)
