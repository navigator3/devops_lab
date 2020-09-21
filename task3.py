s = input("enter text line: ")
t = []
for i in s.split():
    t.append(i[::-1])
print("original text was    : %s " % s)
print("text after processing: %s " % " ".join(t))
