
mx = 0
cur = 0
f = open('data.txt', 'r')
lines = f.readlines()

sums = []
for line in lines:
    line = line.replace('\n','')
    if len(line) > 0:
        cur+=int(line)
        print(int(line), cur)
        mx=max(mx,cur)
    else:
        sums.append(cur)
        cur=0
        mx=max(mx,cur)

sums = sorted(sums)
print(sums[-3]+sums[-2]+sums[-1])
# print(mx)