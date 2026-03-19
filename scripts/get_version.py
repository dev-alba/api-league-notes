import httpx
import asyncio

VERSIONS='https://ddragon.leagueoflegends.com/api/versions.json'

async def lastest_version():
    async with httpx.AsyncClient() as client:
        response=await client.get(VERSIONS)
        if response.status_code==200:
            data=response.json()
            return data[0]

if __name__ == "__main__":
    asyncio.run(lastest_version())