# -*- coding: utf-8 -*-
# @Time : 2019/11/20 下午11:37 
# @Author : kimihiro
# @File : I_Queue.py 
# @Software: PyCharm
from abc import ABCMeta
from abc import abstractmethod
from typing import Any


class IQueue(metaclass=ABCMeta):
    @abstractmethod
    def get_size(self) -> int:
        pass

    @abstractmethod
    def is_empty(self) -> bool:
        pass

    @abstractmethod
    def enqueue(self, element: Any):
        pass

    @abstractmethod
    def dequeue(self) -> Any:
        pass

    @abstractmethod
    def get_front(self) -> Any:
        pass
