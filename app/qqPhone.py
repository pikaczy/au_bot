import redis

def qqPhone(content,redis_host):
    pool = redis.ConnectionPool(host=redis_host,port=6379,db=0,decode_responses=True)
    r = redis.Redis(connection_pool=pool)
    phone = r.sscan(content)
    if(phone[0]==0):
        return '无结果'
    return phone[1]
