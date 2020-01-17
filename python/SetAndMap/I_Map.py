# -*- coding: utf-8 -*-
# @Time : 2020/1/17 下午3:24 
# @Author : kimihiro
# @File : I_Map.py 
# @Software: PyCharm
from abc import ABCMeta
from abc import abstractmethod

# 栈的抽象基类
from typing import Any


class IMap(metaclass=ABCMeta):
    @abstractmethod
    def add(self, key: Any, value: Any):
        pass

    @abstractmethod
    def contains(self, key: Any) -> bool:
        pass

    @abstractmethod
    def get(self, key) -> Any:
        pass

    @abstractmethod
    def set(self, key: Any, value: Any):
        pass

    @abstractmethod
    def remove(self, key: Any):
        pass

    @abstractmethod
    def get_size(self) -> int:
        pass

    @abstractmethod
    def is_empty(self) -> bool:
        pass
