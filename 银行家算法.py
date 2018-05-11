# -*- coding:utf-8 -*-

'''

@author: leisun

@contact: leisun98@gmail.com

@file: 银行家算法.py

@time: 2018/4/23 下午7:01

'''


def Bigger(list_1,list_2): #比较两个列表中各个值大小
    for i in range(len(list_1)):
        if list_1[i] >= list_2[i]:
            i += 1
        else: return False
    return True

def sum(list_1, list_2, operator): #重新定义两个列表加减
    if len(list_1) == len(list_2):
        res =[]
        for i in range(len(list_2)):
            res.append(list_1[i]+list_2[i])\
                if operator == "+"\
                else res.append(list_1[i]-list_2[i])
        return res
    else: return ""



def Bank(Available): #银行家算法


    Max = {
        "P0": [7, 5, 3],
        "P1": [3, 2, 2],
        "P2": [9, 0, 2],
        "P3": [2, 2, 2],
        "P4": [4, 3, 3]
    }
    Allocation = {
        "P0": [0, 1, 0],
        "P1": [2, 0, 0],
        "P2": [3, 0, 2],
        "P3": [2, 1, 1],
        "P4": [0, 0, 2]
    }

    Need = {}  # 赋值给各进程需要最大需求量以及占用资源量

    for key in Max.keys():
        # print(Bigger(Max[key], Allocation[key]))

        if Bigger(Max[key], Allocation[key]):
            # print(Max[key], Allocation[key])
            Need[key] = sum(Max[key], Allocation[key], "-") # 求出各进程还需要的资源量
        else:
            print("进程占用资源大于Max")
            return Available
    # print(Need)

    process = input("请输入请求的进程名：\n")
    req = input("请输入进程请求的资源数量，格式为：(x,y,z)\n")

    requset = []
    for each in req:
        if each.isdigit():
            requset.append(int(each))

    if Bigger(Need[process], requset):
        if Bigger(Available, requset):
            Available = sum(Available, requset, "-")
            Allocation[process] = sum(Allocation[process], requset, "+")    #系统分配资源并修改对应数据结构值
            Need[process] = sum(Need[process], requset, "-")

            print("\t\tMax\t\tAllocation\t\tNeed\t   Available")
            print("\t\tA B C\t\tA B C\t\tA B C\t\tA B C")
            for key in Max.keys():
                if key == process:
                    print(key, " ", Max[key], "\t", Allocation[key], "\t", Need[key], "\t   ", Available)
                else:
                    print(key, " ", Max[key], "\t", Allocation[key], "\t", Need[key])
            Safe(Available, Allocation, Need)
        else:
            print("需求过多，无法成功分配资源，无安全序列")


    else:
        print("进程{}对资源的申请量大于其说明的最大值,请重新输入".format(process))
        return Bank(Available)
    return Available

def Safe(Available, Allocation, Need): #安全性算法
    Work = Available
    Finish = {}
    for i in range(0,5):
        key = "P" + str(i) #为Finish向量赋初值
        Finish[key] = False

    safe = []
    for i in range(len(Finish.keys())):
        for key in Finish.keys():
            if Finish[key] is False and Bigger(Work, Need[key]):
                Finish[key] = True
                Work = sum(Work, Allocation[key], "+")
                safe.append(key)
            else:
                i += 1

    for val in Finish.values():
        if val is False:
            print("无安全序列")
            break

    if safe:
        print("安全序列为：{", end="")
        for i in range(len(safe)):
            if i < 4:
                print(safe[i], end=",")
            else: print(safe[i], end="")
        print("}")



def main(Available):

    print("Apply:申请资源\t\tExit:退出\n")
    command = input("请输入命令:\n")

    if command == "Exit":
        exit(0)

    elif command == "Apply":
        Available = Bank(Available)
        print("\n\n")
        return main(Available)

    else:
        input("命令错误，请重新输入：\n")
        return main(Available)

if __name__ == '__main__':

    Available = ([3, 3, 2])
    main(Available)