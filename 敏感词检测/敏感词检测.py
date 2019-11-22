#coding:utf-8


"""
# 方案一：正则
import re

def check_filter(keywords, text):
    return re.sub('暴力|色情|敏感词','**',text)

keywords = ('暴力','色情','敏感词')
text = '这句话不包含暴力，也没有色情，更没有其他敏感词'
print(check_filter(keywords, text))
"""



"""
#方案二：确定有限状态自动机
import time

time1 = time.time()

# DFA算法
class DFAFilter(object):
    def __init__(self):
        self.keyword_chains = {}    # 关键词链表
        self.delimit = '\x00'       # 限定

    def add(self, keyword):
        keyword = keyword.lower()   # 字母变小写
        chars = keyword.strip()     # 去除首尾空格换行
        # 关键字为空直接返回
        if not chars:
            return
        level = self.keyword_chains
        # 遍历关键字的每个字
        for i in range(len(chars)):
            # 如果这个字已经存在字符链的key中就进入其子字典
            if chars[i] in level:
                level = level[chars[i]]
            else:
                if not isinstance(level, dict):
                    break
                for j in range(i, len(chars)):
                    level[chars[j]] = {}
                    last_level, last_char = level, chars[j]
                    level = level[chars[j]]
                last_level[last_char] = {self.delimit:0}
                break
        if i == len(chars) - 1:
            level[self.delimit] = 0

    def parse(self, path):
        with open(path, encoding='utf-8') as f:
            for keyword in f:
                self.add(str(keyword).strip())
        print('字典-->',self.keyword_chains)

    def filter(self, message, repl='*'):
        message = message.lower()
        ret = []
        start = 0
        while start < len(message):
            level = self.keyword_chains
            step_ins = 0
            for char in message[start:]:
                if char in level:
                    step_ins += 1
                    if self.delimit not in level[char]:
                        level = level[char]
                    else:
                        ret.append(repl*step_ins)
                        start += step_ins - 1
                        break
                else:
                    ret.append(message[start])
                    break
            else:
                ret.append(message[start])
            start += 1

        return ''.join(ret)

if __name__ == "__main__":
    gfw = DFAFilter()
    path = 'sensitive_words.txt'
    gfw.parse(path)
    text = '你真是个大傻逼，大傻子，傻大个，大坏蛋，坏人。'
    result = gfw.filter(text)
    print(text);print(result)
    print('耗时：' + str(time.time()-time1) + 's')

"""


# 方案三：AC自动机
import time

time1 = time.time()

# ACA算法
class node(object):
    def __init__(self):
        self.next = {}
        self.fail = None
        self.isWord = False
        self.word = ""

class ac_automation(object):
    def __init__(self):
        self.root = node()
    
    # 添加敏感词
    def addword(self, word):
        temp_root = self.root
        for char in word:
            if char not in temp_root.next:
                temp_root.next[char] = node()
            temp_root = temp_root.next[char]
        temp_root.isWord = True
        temp_root.word = word
    
    # 失败指针
    def make_fail(self):
        temp_que = []
        temp_que.append(self.root)
        while len(tem_que) != 0:
            temp = tem_que.pop(0)
            p = None
            for key,value in temp.next.item():
                if temp == self.root:
                    temp.next[key].fail = self.root
                else:
                    p = temp.fail
                    while p is not None:
                        if key in p.next:
                            temp.next[key].fail = p.fail
                            break
                        p = p.fail
                    if p is None:
                        temp.next[key].fail = self.root
                temp_que.append(temp.next[key])
    
    # 查找敏感词
    def search(self, content):
        p = self.root
        result = []
        currentposition = 0
        
        while currentposition < len(content):
            word = content[currentposition]
            while word in p.next == False and p != self.root:
                p = p.fail
            
            if word in p.next:
                p = p.next[word]
            else:
                p = self.root
            
            if p.isWord:
                result.append(p.word)
                p = self.root
            currentposition += 1
        return result
    
    # 加载敏感词库
    def parse(self, path):
        with open(path,encoding='utf-8') as f:
            for keyword in f:
                self.addword(str(keyword).strip())

    # 敏感词替换
    def words_replace(self, text):
        result = list(set(self.search(text)))
        for x in result:
            m = text.replace(x, '*'*len(x))
            text = m
        return text


if __name__ == '__main__':
    ah = ac_automation()
    path = 'sensitive_words.txt'
    ah.parse(path)
    text1 = '新疆的苹果新品发布被骚乱，真雞八贱'
    text2 = ah.words_replace(text1)

    print(text1,'\n',text2)
    print('总共耗时：' + str(time.time() - time1) + 's')














