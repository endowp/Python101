s1,s2,s3=input().split()
s1,s2,s3=int(s1),int(s2),int(s3)
if s1+s2>s3 and s2+s3>s1 and s1+s3>s2:
    print("YES")
else:
    print("NO")
