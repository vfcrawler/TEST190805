from random import choice
from redis import StrictRedis
from Sample.ProxyPool.error import PoolEmptyError
from Sample.ProxyPool.setting import REDIS_HOST, REDIS_PORT, REDIS_PASSWORD, REDIS_KEY
from Sample.ProxyPool.setting import MAX_SCORE, MIN_SCORE, INITIAL_SCORE
import re


class RedisClient(object):

    def __init__(self, host=REDIS_HOST, port=REDIS_PORT, password=REDIS_PASSWORD):
        """
        初始化
        :param host: Redis IP地址
        :param port: Redis 端口
        :param password: Redis 密码
        """
        self.db = StrictRedis(host=host, port=port, password=password, decode_responses=True)

    def add(self, proxy, score=INITIAL_SCORE):

        """
        添加代理，设置分数为初始值
        :param proxy: 代理
        :param score: 分数
        :return: 添加结果
        """

        pattern = re.compile('\d+\.\d+\.\d+\.\d+\:\d+')

        if not re.match(pattern, proxy):
            print('代理不符合规范', proxy, '丢弃')
            return

        if not self.db.zscore(REDIS_KEY, proxy):
            return self.db.zadd(REDIS_KEY, {proxy: score})

    def decrease(self, proxy):
        """
        代理分数减1分，小于最小分数则删除
        :param proxy: 代理
        :return: 修改后的代理分数
        """
        score = self.db.zscore(REDIS_KEY, proxy)

        if score and score > MIN_SCORE:
            print('代理', proxy, '当前分数', score, '减1')
            return self.db.zincrby(REDIS_KEY, -1, proxy)
        else:
            print('代理', proxy, '当前分数', score, '移除')
            return self.db.zrem(REDIS_KEY, proxy)

    def random(self):

        #按分数的区间从小到大排序
        ret = self.db.zrangebyscore(REDIS_KEY, MAX_SCORE, MAX_SCORE)

        if len(ret):
            return choice(ret)

        # 按分数的1-100名逆向排序
        ret = self.db.zrevrange(REDIS_KEY, 0, 100)

        if len(ret):
            return choice(ret)
        else:
            raise PoolEmptyError()


if __name__ == '__main__':
    redis_client = RedisClient()

    proxy = '127.0.0.1:8080'

    redis_client.add(proxy)
    redis_client.decrease(proxy)
    print(redis_client.random())
