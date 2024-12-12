from .healhCheck import apiRouter as healhCheck
from .user import apiRouter as User
from .files import apiRouter as Files
from .character import apiRouter as Character
from .pdf import apiRouter as Pdf

listOfRoutes = [
    healhCheck,
    User,
    Files,
    Character,
    Pdf
]

__all__ = [
    "listOfRoutes",
]
