word = input("Enter a word:")
length = len(word)


l = []
for i in range(1, 7):
    num = eval(input(f"Enter a number {i}: "))
    l.append(num)
s = sum(l)
c = len(l)
a = s/c



print(l)
print("the leng of the word is:",length)
print("the average of the number is",a)
if a <length:
    print("The length  of the word",word,"is greater than the average")
else:
    print("The length of the word",word,"is less than the average")




    

