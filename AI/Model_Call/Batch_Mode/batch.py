import asyncio
import json
import os
import httpx
import time
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("OPEN_ROUTER_API")
price = 0.0012
URL = "https://openrouter.ai/api/v1/chat/completions"
MODEL = "liquid/lfm-2.5-2.6b:free"

headers = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json"
}


async def send_prompt(client, item):
    response = await client.post(
        URL,
        headers=headers,
        json={
            "model": MODEL,
            "messages": [
                {
                    "role": "user",
                    "content": item["prompt"]
                }
            ]
        }
    )

    return {
        "id": item["id"],
        "status": response.status_code,
        "response": response.json()
    }


async def main():

    with open("prompt.json", "r") as f:
        prompts = json.load(f)

    async with httpx.AsyncClient(timeout=60) as client:
        start = time.perf_counter()
        tasks = [
            send_prompt(client, item)
            for item in prompts
        ]

        results = await asyncio.gather(*tasks)
    total_cost = 0.0
    for result in results:
        print(result)
        current_result = result
        total_cost=current_result["response"]["usage"]["prompt_tokens"]*price
    end = time.perf_counter()
    print("Cost of batch:",total_cost)
    print("Average cost of batch:",total_cost/len(tasks))
asyncio.run(main())