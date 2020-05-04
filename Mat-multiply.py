#matrix multiplication program

#Function to generate matrix
def create_mat():
    r = int(input("Enter the no. of Rows: "))
    c = int(input("Enter the no. of Cols: "))
    mat = []
    for i in range(r):
        temp = []
        for j in range(c):
            temp.append(int(input("Enter indexed {}{} element: ".format(i,j))))
        mat.append(temp)
    return mat

#Function to multiply matrix
def mult_mat(m1, m2):
    if len(m1[0]) != len(m2):
        print("Matrix multiply not possible to these matrices!")
    else:
        print("Matrix multiplication.")
        res = [[0 for x in range(len(m1))] for y in range(len(m2[0]))]
  
        # explicit for loops
        for i in range(len(m1)):
            for j in range(len(m2[0])):
                for k in range(len(m2)):  
                    # resulted matrix
                    res[i][j] += m1[i][k] * m2[k][j]
        return res       
            

def main():
    print("For matrix A")
    matA = create_mat()
    print(matA)
    print("For matrix B")
    matB = create_mat()
    print(matB)
    result_mat = mult_mat(matA, matB)
    print(result_mat)

if __name__ == '__main__':
    main()
