# -*- coding: utf-8 -*-
# @Time : 2020/1/17 下午4:09 
# @Author : kimihiro
# @File : read_files.py 
# @Software: PyCharm


def read_files(file_path: str) -> list:
    with open(file_path, "r", encoding='utf-8') as f:
        txt = f.read()
        result = txt.lower().split(' ')
    return result


if __name__ == "__main__":
    res = read_files("src/pride-and-prejudice.txt")
    print(len(res))
