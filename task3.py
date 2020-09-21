s = input("enter text line: ")
l = s.split()
t = []
for i in l:
    t.append(i[::-1])
print("original text was    : %s " %s)
print("text after processing: %s " %" ".join(t))
