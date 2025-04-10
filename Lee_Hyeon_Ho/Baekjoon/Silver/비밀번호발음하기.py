import sys

# 문자열 받기
S = sys.stdin.readline().strip()
vowels = ["a", "e", "i", "o", "u"]

while "end" != S:
    # 모음 있는지 검사
    tmp = 0
    for x in vowels:
        if x in S:
            tmp = 1
    if tmp == 0:
        # print("모음이 없음")
        print(f"<{S}> is not acceptable.")
    
    # 같은 글자가 연속 두개 나오는지 검사, 자음 또는 모음이 세번 연속 나오는지 검사
    else:
        vow = 0
        con = 0
        for i in range(len(S)):
            if S[i] != "o" and S[i] != "e" and (i+1 < len(S)) and (S[i] == S[i+1]):
                # print("같은 문자가 두개 이상 나타남")
                print(f"<{S}> is not acceptable.")
                tmp = 0
                break
            
            if S[i] in vowels:
                vow += 1
                con = 0
            else:
                con += 1
                vow = 0
        
            if vow == 3 or con == 3:
                # print("모음 또는 자음이 세개 연속으로 나타남")
                print(f"<{S}> is not acceptable.")
                tmp = 0
                break
        if tmp != 0:
            print(f"<{S}> is acceptable.")
    
    S = sys.stdin.readline().strip()
    