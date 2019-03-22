import configparser

class ReadConfig:
    """定义读取配置的类"""
    def __init__(self):
        self.cf=configparser.ConfigParser()
        self.cf.read('C:\\Users\\test\\AppData\\Local\\Programs\\Python\\Python36\\autotest\\test_api\\config.txt')  #配置文件的目录

    def get_api(self):
        API=self.cf.get('base', 'api')
        return API

    def get_prefix(self):
        Prefix=self.cf.get('base', 'prefix')
        return Prefix

    def get_account(self):
        account=self.cf.get('base', 'account')
        return account

    def get_pw(self):
        pw=self.cf.get('base', 'pw')
        return pw

if __name__ == '__main__':
    test = ReadConfig()
    API = test.get_api()
    Prefix = test.get_prefix()
    print(API)
    print(Prefix)