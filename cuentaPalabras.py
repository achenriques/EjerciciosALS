f = open("text", "rU")
count = 0
todo = set()
for line in f:
    s = line.lower().split(" ")
    todo = (todo | set(s))
    for aux in s:
        if(aux != "\n"):
            count += 1

print(count)

f.close
