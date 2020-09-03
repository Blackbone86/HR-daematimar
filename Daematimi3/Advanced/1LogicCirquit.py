a = bool(int(input("A")))
b = bool(int(input("B")))
c = bool(int(input("C")))

d = 0
# compute d
if (a and not b) or (not a and c):
    d = 1

print("D is", d)

