from .healhCheck import apiRouter as healhCheck
from .user import apiRouter as User
from .files import apiRouter as Files
from .character import apiRouter as Character
from .pdf import apiRouter as Pdf
from .ya_gpt import apiRouter as Gpt

listOfRoutes = [
    healhCheck,
    User,
    Files,
    Character,
    Pdf,
    Gpt,
]

__all__ = [
    "listOfRoutes",
]
