import redis

whost = "w_hotevents_6325_rds.lzdb.com"
port = 6325
rhost = "r_hotevents_6325_rds.lzdb.com"

rds = redis.StrictRedis(host=whost, port=port)

r = rds.set("name", "lyy")
print(r)