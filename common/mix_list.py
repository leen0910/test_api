from collections import Iterable

def getDict():
    dic={"a":[1,2],"b":[{"k":1},2],"c":1,"d":("a",1)}
    return dic

def analysis(dic):
    li=[]
    print("\n---member---\n")
    for key,value in dic.items():
        print(key+' is :'+type(dic[key]).__name__+"\n")
        if isinstance(dic[key],Iterable):
            for j in dic[key]:
                li.append([key,j])
        else :
            li.append([key,dic[key]])
    print('---end---')
    return li

if __name__=="__main__":
    dic=getDict()
    li=analysis(dic)
    print(li)