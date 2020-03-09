import redis

class PyRedis(object):
    def __init__(self, host='127.0.0.1', port=6379, db=1):
        try:
            self.conn = redis.StrictRedis(host=host, port=port, db=db)
        except Exception as e:
            print("Redis Connection Error MSG : {}".format(e))


    def exec_command(self):
        pass
    
    def __del__(self):
        pass