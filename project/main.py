import redis


class PyRedis(object):
    def __init__(self, host='127.0.0.1', port=6379, db=1):
        try:
            self.conn = redis.StrictRedis(host=host, port=port, db=db)
        except Exception as e:
            print(e)

    def exec_command(self):
        self.conn.set("test", "test")
        print("Get Test {}".format(self.conn.get("test")))

    def __del__(self):
        pass

if __name__ == '__main__':
    aa = PyRedis(host='127.0.0.1',port=6379, db=1)
    aa.exec_command()

    var_keyspace = aa.conn.info("keyspace")
    print(type(var_keyspace))
    print(var_keyspace)

    for key, var in var_keyspace.items():
        print("KEY TYPE IS {}".format(type(key)))
        print("VALUE TYPE IS {}".format(type(var)))
        print("{} {}".format(key, var))
        test_var_str = ', '.join('{} : {}'.format(aa, bb) for aa, bb in var.items())
        print("{} Contain {}".format(key, test_var_str))

    var_str = ', '.join('{} : {}'.format(key, value) for key, value in var_keyspace.items())
    print("{}".format(var_str))

    del aa