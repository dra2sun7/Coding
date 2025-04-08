import sys

string = sys.stdin.readline().strip()
diction = dict()
m_cnt = 0
m_str = 0
tmp = 0


string = string.upper()

for x in string:
    if x not in diction:
        diction[x] = 1
    else:
        diction[x] += 1
    
for x in diction:
    if diction[x] > m_cnt:
        m_cnt = diction[x]
        m_str = x
        tmp = 0
    elif diction[x] == m_cnt:
        tmp += 1

if tmp != 0:
    print("?")
else:
    print(m_str)