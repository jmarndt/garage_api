from io import BytesIO

from fastapi import FastAPI, APIRouter, Depends
from fastapi.responses import StreamingResponse

from app.authentication import authenticate
from app.lights import LightActions, light_control
from app.doors import GarageDoors, door_control
from app.camera import camera_snapshot


app = FastAPI(title="Garage API", docs_url="/docs", redoc_url=None)
api = APIRouter()


@api.get("/garage/ping")
def health() -> dict:
    """
    Check if API is reachable
    """
    return { "garapge_api": "pong" }


@api.get("/garage/doors", status_code=200, dependencies=[Depends(authenticate)])
def garage_doors(door: GarageDoors) -> dict:
    """
    Activate a garage door
    """
    door_control(door)
    return { "door": door }


@api.get("/garage/lights", status_code=200, dependencies=[Depends(authenticate)])
def garage_lights(action: LightActions) -> dict:
    """
    Turn lights on or off with query parameters
    """
    light_control(action)
    return { "lights": action }


@api.get("/garage/cameras", dependencies=[Depends(authenticate)])
async def garage_cameras() -> bytes:
    """
    Retrieve snapshot of garage camera
    """
    image_bytes = BytesIO(camera_snapshot())
    return StreamingResponse(image_bytes, media_type="image/jpeg")


app.include_router(api)


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8001, log_level="debug")