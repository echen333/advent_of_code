
f = open('data.txt', 'r')
lines = f.readlines()

tmp =[]
for line in lines:
    line = line.strip()
    tmp.append(line)

# print(tmp, len(tmp))
pritn(len(tmp))
for i in range(len(tmp)//2):
    ans = -1
    tmp = {}
    for j in range(len(tmp[2*i])):
        tmp.add(tmp[2*i][j])
    for j in range(len(tmp[2*i+1])):
        if tmp[2*i+1][j] in tmp:
            ans = ord(tmp[2*i+1][j])
            break
    print(ans)