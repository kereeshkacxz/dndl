import os
import sys
from logging import getLogger

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from uvicorn import run


sys.path.append(os.path.join(os.getcwd(), os.pardir, os.pardir))

from app.config import DefaultSettings
from app.config.utils import getSettings
from app.endpoints import listOfRoutes


logger = getLogger(__name__)


def bindRoutes(application: FastAPI, setting: DefaultSettings) -> None:
    for route in listOfRoutes:
        application.include_router(route, prefix=setting.PATH_PREFIX)


def getApp() -> FastAPI:
    description = "Сервис для создания листов персонажей D&D"

    tags_metadata = [
        {
            "name": "Health check",
        },
        {
            "name": "User",
            "description": "Registration and authorization before further actions.",
        },
        {
            "name": "Video",
            "description": "Upload video or download it by name.",
        }
    ]

    application = FastAPI(
        title="DNDL",
        docs_url="/swagger",
        openapi_url="/openapi",
        description=description,
        version="1.0.0",
        openapi_tags=tags_metadata,
    )

    application.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    settings = getSettings()
    bindRoutes(application, settings)
    application.state.settings = settings
    return application


app = getApp()

if __name__ == "__main__":  # pragma: no cover
    settings_for_application = getSettings()
    run(
        "__main__:app",
        port=settings_for_application.BACKEND_PORT,
        reload=True,
        reload_dirs=["app", "tests"],
        log_level="debug",
        host=settings_for_application.BACKEND_HOST,
    )
