from fastapi import FastAPI, APIRouter


app = FastAPI(title="Garage API", docs_url="/docs", redoc_url=None)
api = APIRouter()


@api.get("/health")
def health() -> None:
    """
    Check if API is reachable
    """


@api.get("/garage/doors/{door_number}", status_code=200)
def trigger_garage_door(door_number: int) -> dict:
    """
    Trigger garage door by number
    """
    print(f'TODO: trigger door number {door_number}')
    return { "door_number": door_number, "todo": "trigger door" }


app.include_router(api)


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8001, log_level="debug")