# -*- coding: utf-8 -*-
# @Time : 2019/11/20 下午10:41 
# @Author : kimihiro
# @File : I_Stack.py 
# @Software: PyCharm
from abc import ABCMeta
from abc import abstractmethod

# 栈的抽象基类
from typing import Any


class IStack(metaclass=ABCMeta):
    @abstractmethod
    def get_size(self) -> int:
        pass

    @abstractmethod
    def is_empty(self) -> bool:
        pass

    @abstractmethod
    def push(self, element: Any):
        pass

    @abstractmethod
    def pop(self) -> Any:
        pass

    @abstractmethod
    def peek(self) -> Any:
        pass
