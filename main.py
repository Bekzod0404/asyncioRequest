import aiohttp
import asyncio
import json


def write_to_file(data):
    with open('names.json', 'a') as file:
        json.dump(data, file, indent=4)


async def get_data(name):
    async with aiohttp.ClientSession() as session:
        async with session.get(f'https://api.agify.io?name={name}') as response:
            data = await response.json()
            return data


async def main():
    names = list(map(str, input('Ism kiriting: ').split()))
    tasks = [asyncio.create_task(get_data(name)) for name in names]
    data = await asyncio.gather(*tasks)
    write_to_file(data)


if __name__ == '__main__':
    asyncio.run(main())
