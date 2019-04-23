# coding:utf-8
import random
import hashlib
import time

class RandomChar:
    def random_char(self,string,length,bool):
        # 生成随机数，string为前缀字符串，length为随机数的长度，bool=0表示纯数字，非0表示数字字母混合。
        for i in range(length):
            bool = random.randint(0,bool)
            if bool == 0:
                y = str(random.randint(0,9))
            else:
                y = chr(random.randint(97, 122))
            string.append(y)
        string = ''.join(string)
        return string

    def hash(self,seed):
        m1=hashlib.md5()
        m1.update(seed.encode("utf-8"))
        m=m1.hexdigest()
        return m

    def localtime(self):
        t=time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))     # 格式化：2019-04-23 11:11:27
        return t

if __name__ == '__main__':
    # string =[]
    # length = 5
    test=RandomChar()
    # qqq=test.random_char(string,length,1)
    # print(qqq)
    seed="this is a md5 test."
    q=test.hash(seed)
    print(q)
    y=test.localtime()
    print(y)

