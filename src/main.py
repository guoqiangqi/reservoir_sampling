# -*- coding: utf-8 -*-
'''
reference to https://huangjj27.gitlab.io/posts/fair-lottery/
'''
import random
SAMPLE_COUNT = 10

# 默认使用系统时间作为种子，增加不可预测性
# 如果想要得到重复结果
# 可以使用固定的种子以选取固定的伪随机数数列
random.seed()
# random.seed(12345)

sample_titles = []
for index, line in enumerate(open("sample.txt")):
    # 初始化奖池
    if index < SAMPLE_COUNT:
        sample_titles.append(line)
    else:
        # 以递减的概率替换奖池里的元素
        # 选择从0到index的一个随机数
        r = random.randint(0, index)
        if r < SAMPLE_COUNT:
            sample_titles[r] = line

print sample_titles     # 打印中奖结果
