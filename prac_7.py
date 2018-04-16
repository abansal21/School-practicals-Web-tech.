def linearSearch(arr, n):
    for i in range(len(arr)):
        if(arr[i] == n):
            return i
    return -1
           

def binarySearch(arr, n):
    first = 0
    last = len(arr) - 1
    while(first <= last):
        mid = (first + last) // 2
        if(arr[mid] == n):
            return mid
        else:
            if(n < arr[mid]):
                last = mid - 1
            else:
                first = mid + 1
    return -1

def selectionSort(arr):
    for i in range(len(arr)):
        least = i
        for j in range(i + 1, len(arr)):
            if(arr[j] < arr[least]):
                least = j
        arr[least], arr[i] = arr[i], arr[least]

def insertionSort(arr):
    for i in range(len(arr)):
        temp = arr[i]
        j = i - 1
        while(j >= 0 and arr[j] > temp):
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = temp
    return

def bubbleSort(arr):
    for i in range(len(arr)):
        swapped = False
        for j in range(len(arr) - 1, i, -1):
            if(arr[j] < arr[j - 1]):
                arr[j], arr[j-1] = arr[j-1], arr[j]
                swapped = True
        if not swapped:
            break
    
def fibb():
    first = 1
    second = 1
    fib = []
    n = int(input("Enter the number for terms required:"))
    for i in range(n):
        if(i <= 1):
            num = 1
        else:
            num = first + second
            first = second
            second = num
        fib.append(num)
    print("The fibbonacci seris of length {} is ".format(n))
    print(fib)
def main():
    print("1. Linear Search")
    print("2. Binary Search")
    print("3. Selection Sort")
    print("4. Insertion Sort")
    print("5. Bubble Sort")
    print("6. Fibonacci Series")
    print("0. Exit")
    num = int(input("Enter your choice: "))
    while(num > 6 or num < 0):
        print("Invalid Choice, Try again.")
        num = int(input("Enter your choice: "))
    if(num == 0):
        return
    if(num != 6):
        print("Enter integers in a single line to perform the operation.")
        arr = list(map(int, input().strip().split()))

        if(num <= 2):
            n = int(input("Enter the element to be found: "))
            if(num == 1):
                rs = linearSearch(arr, n)
            else:
                while(arr != sorted(arr) and arr != sorted(arr, reverse = True)):
                    print("Need a sorted list for binary search.")
                    print("Enter integers in a single line to perform the operation.")
                    arr = list(map(int, input().strip().split()))
                rs = binarySearch(arr, n)
            if(rs != -1):
                print("{} found at position {}.".format(n, rs + 1))
            else:
                print("{} not found in the list.".format(n))

        else:
            selectionSort(arr) if num == 3 else insertionSort(arr) if num == 4 else bubbleSort(arr)
            print("The sorted list is: ")
            print(arr)

    else:
        fibb()
            
    
if __name__ == "__main__":
    main()
            
            
            
