def solutions(S):
    if S[0] !=S[-1]:
        return 0
    else:
        count = S.count(S[0])
        return count
s1 = solutions('abbaa') 
print(s1)
s2 = solutions('aaaa')
print(s2)
s3=solutions('abab')
print(s3)