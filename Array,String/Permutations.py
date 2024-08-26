import itertools
a=[2,3,4,5]

p=list(itertools.product(a,repeat=3))
for i in p:
    ps="".join(map(str,p))
print(str(ps))
r=list(itertools.permutations(a))
for i in r:
    rs="".join(map(str,r))
print(str(rs))
