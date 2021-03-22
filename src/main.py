from fastapi import FastAPI
from fastapi.responses import PlainTextResponse
from routers import v1

app = FastAPI()
app.include_router(v1.router, prefix="/v1")

ref = {
    "/v1/taxcalc": {
        "params": ["amount - float"],
        "returns": "JSON"
    }
}

@app.get("/", response_class=PlainTextResponse)
async def home():
    base = ""

    for key, value in ref.items():
        base += f"{key} - Params: {', '.join(value['params'])} - Returns: {value['returns']}\n"

    return base