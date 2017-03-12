#Diccionarios
d0 = {}
d = {"uno": 1, "dos": 2, "tres": 3}

def f1():
    print("f1")
def f2():
    print("f2")

print(d0)
print(d)
print(d["uno"])
print(d.get("dos"))
print(d.get("excepcion"))

print(d.keys())
print(d.values())

for k in d.keys():
    print(d[k], end='')

for k,v in enumerate(d):
    print(str.format("{0} = {1}", k, v))

op = int(input("Option> "))
f = {1: f1, 2: f2}.get(op)



