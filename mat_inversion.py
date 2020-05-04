def mat_transpose(mat):
    return list(map(list,zip(*mat)))
#use return map(list,zip(*mat)) for Python 2

def mat_minor(mat,i,j):
    return [r[:j] + r[j+1:] for r in (mat[:i]+mat[i+1:])]

def mat_determinant(mat):
    if len(mat) == 2:
        return(mat[0][0]*mat[1][1]-mat[0][1]*mat[1][0])
    else:
        det = 0
        for d in range(len(mat)):
            det = det + (pow(-1,d))*mat[0][d]*mat_determinant(mat_minor(mat,0,d))
        return det

def mat_inversion(mat):
    determinant = mat_determinant(mat)
    print("\nDeterminant:",determinant)
    if determinant == 0:
        return "Inverse not possible since the matrix has zero as determinant"
    if len(mat) == 2:
        return [[mat[1][1]/determinant, -1*mat[0][1]/determinant],
                [-1*mat[1][0]/determinant, mat[0][0]/determinant]]
    else:
        mat_cfactor = []
    for r in range(len(mat)):
        mat_cfactor_row = []
        for c in range(len(mat)):
            minor = mat_minor(mat,r,c)
            mat_cfactor_row.append(((-1)**(r+c)) * mat_determinant(minor))
        mat_cfactor.append(mat_cfactor_row)
    mat_cfactor = mat_transpose(mat_cfactor)
    for r in range(len(mat_cfactor)):
        for c in range(len(mat_cfactor)):
            mat_cfactor[r][c] = mat_cfactor[r][c]/determinant
    return mat_cfactor

def main():
    print("\nSquare matrix may have inverse")
    print("If determinant of a matrix is zero, inverse not possible\n")
    #matA = create_mat()
    #mat = [[1.0, 2.0, 3.0], [4.0, 5.0, 6.0], [7.0, 8.0, 9.0]]
    mat = [[2,-1,3],[1,1,1],[1,-1,1]]
    print("Matrix created as follows: ")
    print(*mat,sep="\n")
    #inverse_mat()
    result_mat = mat_inversion(mat)
    print("Inverse matrix:\n",*result_mat,sep="\n")

if __name__ == '__main__':
    main()
