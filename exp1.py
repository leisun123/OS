#coding:utf-8

from queue import Queue

class PCB:
    ready_queue = Queue()
    block_queue = Queue()
    PCBnum = 0
    def __init__(self, name, time, status):
        self.name = name
        self.time = time
        self.status = status
    def CREAT_PCB(self):
        self.name = input("请输入进程名:\n")
        self.time = input("请输入运行时间:\n")
        self.status = "R"
        PCB.ready_queue.put(PCB(self.name, self.time, self.status))
        print("进程创建成功")
    def Run_Finsh(self):
        print("运行进程 %s")%self.name
        if PCB.ready_queue.get().name == self.name:
            print("程序运行成功")
            PCB.ready_queue.get().status = "E"
            print("运行结束")
        else:
            print("Error")
    def Run_WAIT(self):
        print("阻塞进程")
        if PCB.ready_queue.get().name == self.name:
            pcb = PCB.ready_queue.get()
            pcb.status = "B"
            PCB.block_queue.put(pcb)
            print("阻塞成功")
        else:
            print("Error")
    def Run_SIGNAL(self):
        print("唤醒进程")
        if PCB.block_queue.get().name == self.name:
            pcb = PCB.block_queue.get()
            pcb.status = "R"
            PCB.ready_queue.put(pcb)
            print("唤醒成功")
        else:
            print("Error")
    def show(self):
        print("进程" + self.name + ": 运行时间: " + self.time+"进程状态: " + self.status)
        if self.status == "R":
            print("就绪")
        elif self.status == "E":
            print("结束")
        else:
            print("阻塞")

def main():
    num = 0
    while num <= 5:
        print("-------------------------------------------")
        print("New:新建进程\t\tRun<Finish>:运行程序并结束")
        print("Run<Wait>:运行后阻塞\t\tSignal:唤醒阻塞进程")
        print("Show:显示当前所有运行进程\t\tExit:退出程序")
        print("---------------------------------------")
        a = input("请输入命令:")
        if a == "New":
            if num <= 5:
                PCB("","","").CREAT_PCB()
                num += 1
            else:
                print("进程超出")
                exit(0)
        elif a == "Run<Finish>":
            if not PCB.ready_queue.empty():
                PCB.Run_Finsh()
                num -= num
                print("运行成功")
            else:
                print("无可运行进程")
        elif a == "Run<Wait>":
            if not PCB.ready_queue.empty():
                PCB.Run_WAIT()
            else:
                print("无就绪进程")
        elif a == "Signal":
            if not PCB.block_queue.empty():
                PCB.Run_SIGNAL()
                print("唤醒成功")
            else:
                print("无可唤醒进程")
        elif a == "Show":
            if num == 0:
                print("无进程")
            else:
                for i in range(PCB.ready_queue.qsize()):
                    pcb = PCB.ready_queue.get()
                    PCB(pcb.name,pcb.time,pcb.status).show()
                    i += i
                for a in range(PCB.block_queue.qsize()):
                    pcb = PCB.block_queue.get()
                    PCB(pcb.name,pcb.time,pcb.status).show()
                    a += a
        elif a == "Exit":
            exit(0)
        else:
            input("输出错误，请重新输入命令：")
if __name__ == '__main__':
    main()