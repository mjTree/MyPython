#coding:utf-8

class Context:
    def __init__(self):
        self.input = ''
        self.output = ''


class AbstractExpression:
    def Interpret(self, context):
        pass


class Expression(AbstractExpression):
    def Interpret(self, context):
        print('终端解释')


class NonterminalExpression(AbstractExpression):
    def Interpret(self, context):
        print('非终端解释')


if __name__ == '__main__':
    context = ''
    c = []
    c = c + [AbstractExpression()]
    c = c + [Expression()]
    c = c + [NonterminalExpression()]
    c = c + [Expression()]
    c = c + [Expression()]
    for a in c:
        a.Interpret(context)
