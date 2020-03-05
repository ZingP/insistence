# redis string

import redis
HOST = "10.144.123.183"
PORT = 6379
PASSWD = "redis123"

# 不推荐
# redisObj = redis.Redis(host=HOST, port=PORT, password=PASSWD)
# res = redisObj.set("key", "v1")
# print(res)

# 使用连接池
pool = redis.ConnectionPool(host=HOST, port=PORT, password=PASSWD,socket_timeout=5,socket_connect_timeout=2)
rds = redis.StrictRedis(connection_pool=pool)
try:
    v = rds.get("key")
    print(v)
except Exception as e:
    print("err:", e)

rds.hset("hash_name", "k1", "v1")
rds.hset("hash_name", "k2", "v2")

r = rds.hget("hash_name", "k2")
print("hget:", r)

print(rds.hgetall("hash_name"))