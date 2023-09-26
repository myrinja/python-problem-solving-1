def solution(S):
    if S[0] != S[-1]:
        return 0
    else:
        count = S.count(S[0])
        return(count)

S1 = solution("abbaa")
print(S1)
S2 = solution("aaaa")
print(S2)

S3 = solution("abab")
print(S3)
