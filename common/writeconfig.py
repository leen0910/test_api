# -*- coding: utf-8 -*-
"""
/***************************************************************************
rwconfig:
1.读取配置文件
2.修改配置文件
3.创建配置文件

***************************************************************************/
"""
import  configparser
import  os


class rwconfig:
    def __init__(self):
        pass

    # def readconfig(self,chosepar="uint8"):
    #     os.chdir(r"C:\Users\test\AppData\Local\Programs\Python\Python36\autotest\test_api")
    #     cf = configparser.ConfigParser()
    #     cf.read("datatype.conf")
    #
    #     #读取所有选项
    #     # secs = cf.sections()
    #     # print("sections:",secs,type(secs))
    #     # opts = cf.options("datatype")
    #     # print("options",opts,type(opts))
    #     # kvs = cf.items("datatype")
    #     # print("datatype",kvs)
    #
    #     #读取指定项
    #     selection = cf.get("datatype",chosepar)
    #     intSel = int(selection)
    #     print(intSel)
    #     return intSel


    def writeconfig(self,name,value):
        os.chdir(r"C:\Users\test\AppData\Local\Programs\Python\Python36\autotest\test_api")
        cf = configparser.ConfigParser()
        cf.add_section("info")
        cf.set("info", name, value)

        try:
            with open("info.txt","w+") as f:
                cf.write(f)
        except ImportError:
            pass


if __name__=="__main__":
    obj = rwconfig()
    # obj.readconfig()
    path = r"C:\Users\test\AppData\Local\Programs\Python\Python36\autotest\test_api"
    t=12346
    obj.writeconfig('name',str(t))


