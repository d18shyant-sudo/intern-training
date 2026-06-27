from fastapi import FastAPI
from fastapi.responses import StreamingResponse
import asyncio

app = FastAPI()

@app.get("/events")
async def events():

    async def event_generator():
        count = 0

        while True:
            count += 1
            yield f"data: Counter = {count}\n\n"
            await asyncio.sleep(1)

    return StreamingResponse(
        event_generator(),
        media_type="text/event-stream"
    )