# -*- coding: utf-8 -*-
# @Time : 2020/1/17 下午3:37 
# @Author : kimihiro
# @File : I_Set.py 
# @Software: PyCharm
from abc import ABCMeta
from abc import abstractmethod

# 栈的抽象基类
from typing import Any


class ISet(metaclass=ABCMeta):
    @abstractmethod
    def add(self, element: Any):
        pass

    @abstractmethod
    def contains(self, elememt: Any) -> bool:
        pass

    @abstractmethod
    def remove(self, elememt: Any):
        pass

    @abstractmethod
    def get_size(self) -> int:
        pass

    @abstractmethod
    def is_empty(self) -> int:
        pass
