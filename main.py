#1- misol
tupl = (12, 9, 0, 5, 5)
print(tupl)

yigindi = 0

for i in tupl:
    yigindi += i

print(f"Tuple yigindisi : {yigindi}")

#2-misol
t = ()
t = list(t)
for i in range(5):
    t.append(int(input(f"{i+1} - son kirit: ")))

t = tuple(t)
print(f"Eng kattasi : {max(t)}")

#2-misol ikkinchi usul
numbers = tuple(map(int, input("sonlar kirit: ").split()))
maxsnum = max(numbers)
print(f"Eng kattasi :{maxsnum}")

#3-misol
tup1 = (12, 7, 8, 4)
tup2 = (85, 9, 2, 0)
tup = tup1 + tup2
print(f"Birlashgan yangi tuple: {tup}")

#4-misol
tupll = (12, 3, 4, 7, 9)
juft = tuple(filter(lambda a: a % 2 == 0, tupll))
print(juft)

#5-misol
tuplee = (12, 2, 3, 8, 9)
print(tuplee)

tuplee = tuplee[::-1]
print(tuplee)

