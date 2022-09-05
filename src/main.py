# -*- coding: utf-8 -*-
'''
reference to https://huangjj27.gitlab.io/posts/fair-lottery/
'''
# -*- coding: utf-8 -*-
import random
SAMPLE_COUNT = 50

# set number of all users as random seed
random.seed(98)

luck_users = []
for index, line in enumerate(open("./data/all_users.csv",encoding="utf-8")):
    if index < SAMPLE_COUNT:
        luck_users.append(line)
    else:
        r = random.randint(0, index)
        if r < SAMPLE_COUNT:
            luck_users[r] = line

with open("./data/luck_users.csv", "w") as f:
    for user in luck_users:
        f.write(user)
