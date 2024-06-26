from fastapi import FastAPI
from dotenv import dotenv_values
import redis
config = dotenv_values(".env")

r = redis.Redis(
  host=config['REDIS_HOST'],
  port=config['REDIS_PORT'],
  password=config['REDIS_PASSWORD'],
  ssl=True
)

async def rate_limiting(ip:str):
    key = f"{ip}"
    if r.exists(key):
        r.incr(key)
        r.expire(key, 60 * 15)
    else:
        r.set(key,1)
    if int(r.get(key))>60:
        return False
    return True