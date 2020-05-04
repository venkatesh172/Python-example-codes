#partitioning the list with Pivot
def parting(a, l, h):
        index = l-1
        pivot = a[h]

        for j in range(l, h):
                if a[j] <= pivot:
                        index =index+1
                        a[index], a[j] = a[j], a[index]
        a[index+1], a[h] = a[h], a[index+1]
        return index+1

#Function to perform quick sort
def qsort(a, l, h):
        if l<h:
                p = parting(a, l, h)
                qsort(a, l, p-1)
                qsort(a, p+1, h)


def main():
    n = int(input("How many parts in this list: "))
    a = []
    
    for i in range(n):
        a.append(int(input("Enter index {} of list: ".format(i))))

    print("Unsorted: {}".format(a))
    n = len(a) 
    qsort(a,0,n-1)
    print("Sorted: {}".format(a))

if __name__ == '__main__':
    main()
