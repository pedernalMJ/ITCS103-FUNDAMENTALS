def compute_average(numbers):
    s = sum(numbers)
    c = len(numbers)
    return s / c


def compare_average(avg, word):
    length = len(word)

    if avg < length:
        print("The length of the word", word, "is greater than the average")
    elif avg > length:
        print("The length of the word", word, "is less than the average")
    else:
        print("The length of the word", word, "is equal to the average")
      
word = input("Enter a word: ")
length = len(word)

l = []
for i in range(length):
    num = int(input(f"Enter a number {i + 1}: "))
    l.append(num)

average = compute_average(l)

print(l)
print("The length of the word is:", length)
print("The average of the numbers is:", average)

compare_average(average, word)
