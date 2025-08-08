import aiohttp
import asyncio
import yaml
import subprocess
import chess.engine

with open("config.yml", "r") as f:
    config = yaml.safe_load(f)

TOKEN = config["token"]
ENGINE_PATH = config["engine_path"]

async def stream_events():
    headers = {"Authorization": f"Bearer {TOKEN}"}
    async with aiohttp.ClientSession() as session:
        async with session.get("https://lichess.org/api/stream/event", headers=headers) as resp:
            async for line in resp.content:
                if line:
                    print("Event:", line.decode())

async def main():
    print("Starting bot...")
    await stream_events()

if __name__ == "__main__":
    asyncio.run(main())
