numbers = [10, 20, 30, 40, 50]
key = int(input("Enter the element to search: "))
for i in range(len(numbers)):
    if numbers[i] == key:
        print("Element found at position", i + 1)
        break
else:
    print("Element not found")