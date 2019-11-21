# -*- coding: utf-8 -*-
# @Time : 2019/11/21 14:53 
# @Author : kimihiro
# @File : ArrayQCompareLoopQ.py 
# @Software: PyCharm
import time

from StackAndQueue import Queue
from StackAndQueue.I_Queue import IQueue
from StackAndQueue.LoopQueue import LoopQueue


def compare(q: IQueue, count: int):
    start_time = time.time()
    for i in range(count):
        q.enqueue(i)
    for i in range(count):
        q.dequeue()
    end_time = time.time()
    return end_time - start_time


if __name__ == "__main__":
    count = 10000
    array_queue_cost = compare(Queue.Queue(count), count)
    print("ArrayQueue cost time {}".format(array_queue_cost))
    loop_queue_cost = compare(LoopQueue(count), count)
    print("LoopQueue cost time {}".format(loop_queue_cost))
