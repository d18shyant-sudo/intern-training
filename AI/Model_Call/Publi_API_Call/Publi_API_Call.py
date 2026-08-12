import httpx
from model import Cat_Fact, Joke, Weather
from tenacity import retry, stop_after_attempt, wait_exponential,RetryError


@retry(
    stop=stop_after_attempt(4),
    wait=wait_exponential(
        multiplier=1,
        min=1,
        max=10
    )
)
def get_api(url, params=None):
    response = httpx.get(
        url,
        params=params,
        timeout=httpx.Timeout(
            connect=5,
            write=5,
            pool=5,
            read=5
        )
    )

    response.raise_for_status()
    return response.json()


# 1. Cat Facts API
try:
    cat_data = get_api(
        "https://catfact.ninja/fact"
    )

    cat = Cat_Fact.model_validate(cat_data)
    print(cat, "\n")

except RetryError as e:
    print("Cat API failed:", e.last_attempt.exception())


# 2. Official Joke API
try:
    joke_data = get_api(
        "https://official-joke-api.appspot.com/jokes/random"
    )

    joke = Joke.model_validate(joke_data)
    print(joke, "\n")

except RetryError as e:
    print("Joke API failed:", e.last_attempt.exception())


# 3. Open-Meteo API
try:
    weather_data = get_api(
        "https://api.open-meteo.com/v1/forecast",
        params={
            "latitude": 80.23,
            "longitude": 80.27,
            "current": "temperature_2m"
        }
    )

    weather = Weather.model_validate(weather_data)
    print(weather, "\n")

except RetryError as e:
    print("Weather API failed:", e.last_attempt.exception())