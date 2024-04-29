def execute(text):
    import asyncio
    import python_weather

    async def weatherfind(city):
        async with python_weather.Client() as client:
            weather = await client.get(city)
            print(f'In {city} right now, it\'s {weather.temperature} degrees.')

            for daily in list(weather.daily_forecasts)[:7]:
                day = daily.date.strftime('%A')

                average_temp = sum([hourly.temperature for hourly in daily.hourly_forecasts]) / len([hourly.temperature for hourly in daily.hourly_forecasts])
                status = [hourly.description for hourly in daily.hourly_forecasts]
                average_status = max(set(status), key=status.count)

                print(f'-> {day} in {city}: {average_status}, with an average of {average_temp}.')
    city = text.split(' ', 1)[1]
    asyncio.run(weatherfind(city))    

metadata = {
    "name": "weather",
    "description": "Get the current and future weather of a city.",
    "args": " (city)"
}

__all__ = ['execute', 'metadata']