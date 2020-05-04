#bubble sort

def B_sort(a):
    for i in range(len(a)):
        for j in range(0, len(a)-i-1):
            if a[j]>a[j+1]:					#comparing
                a[j],a[j+1] = a[j+1], a[j]	#swap

def main():
    n = int(input("How many parts in this list: "))
    a = []
    
    for i in range(n):
        a.append(int(input("Enter index {} of list: ".format(i))))


    print("Input list: {}".format(a))
    B_sort(a)
    print("Sorted: {}".format(a))

if __name__ == '__main__':
    main()
