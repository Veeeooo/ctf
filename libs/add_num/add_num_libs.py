#coding=utf-8
def add_nums(*args):
    # print(args)
    total = 0
    for i in args[1]:
        total = total + i.source
    return total
