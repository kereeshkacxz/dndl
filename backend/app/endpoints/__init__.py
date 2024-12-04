from .healhCheck import apiRouter as healhCheck
from .user import apiRouter as User
from .files import apiRouter as Files
from .character import apiRouter as Character

listOfRoutes = [
    healhCheck,
    User,
    Files,
    Character
]

__all__ = [
    "listOfRoutes",
]
