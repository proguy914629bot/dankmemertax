import pathlib
from fastapi import APIRouter


# Get the endpoints path.
path = pathlib.Path("./routers/v1/endpoints")
# Put all files that that match `*.py` and don't start with a `_`
# and removing the `.py` in a list.
end_points = [x.name[:-3] for x in path.glob("[!_]*.py")]


# Instantiate the API Router.
router = APIRouter()
for ep in end_points:
    # This block creates code (To be executed) that
    # imports the endpoint from the route folder
    # and then includes it in the router.
    block = (
        f"from routers.v1.endpoints import {ep}\n"
        f"router.include_router({ep}.router)"
    )
    # This line then executes the block.
    exec(block)