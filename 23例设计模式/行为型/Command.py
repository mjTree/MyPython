#coding:utf-8

import os
import time

class MoveFileCommand(object):
    def __init__(self, src, dest):
        self.src = src
        self.dest = dest
    
    def execute(self):
        self()
    
    def __call__(self):
        print('renaming {} to {}'.format(self.src, self.dest))
        os.rename(self.src, self.dest)
    
    def undo(self):
        print('renaming {} to {}'.format(self.dest, self.src))
        os.rename(self.dest, self.src)


if __name__ == '__main__':
    command_stack = []
    
    # 命令被推送到命令堆栈中
    command_stack.append(MoveFileCommand('foo.txt', 'bar.txt'))
    command_stack.append(MoveFileCommand('bar.txt', 'baz.txt'))
    
    # 命令可以稍后执行
    for cmd in command_stack:
        cmd.execute()
        time.sleep(3)
    
    # 也可以随意撤销
    for cmd in reversed(command_stack):
        cmd.undo()

