import numpy as np

def gaussElimination(a_matrix , b_matrix):

    if a_matrix.shape[0] != a_matrix.shape[1]:
        print("Error:Square Matrix not provided")
        return
    
    if b_matrix.shape[1] > 1 or b_matrix.shape[0] != a_matrix.shape[0]:
        print("Error : Constant matrix is not correctly provided")
        return
    #print("Matrix works properly")

    n = len(b_matrix)
    i=0
    m=n-1
    x=np.zeros(n)
    new_line = "\n"

    #augmented matrix formation

    augmented_matrix = np.concatenate((a_matrix,b_matrix), axis=1,dtype=float)
    print(f"the initial augmented matrix is:{new_line}{augmented_matrix}")
    print("solving for upper triangular matrix")

    while i < n:

        #partial pivoting
        for p in range(i+1 , n):
            if abs(augmented_matrix[i,i]) < abs(augmented_matrix[p,i]):
                augmented_matrix[[p,i]] = augmented_matrix [[i,p]]

        if augmented_matrix[i, i] == 0.0:
            print("Divide by zero error")
            return
        
        for j in range(i+1, n):
            scaling_factor = augmented_matrix[j][i] / augmented_matrix[i][i]
            augmented_matrix[j] = augmented_matrix[j] - (scaling_factor * augmented_matrix[i])
            print(augmented_matrix)

        i = i+1

     #backward substitution

    x[m] = augmented_matrix[m][n] / augmented_matrix[m][m]

    for k in range(n-2 , -1 ,-1):
        x[k] = augmented_matrix[k][n]

        for j in range(k+1 , n):
            x[k] = x[k]- (augmented_matrix[k][j] * x[j])

        x[k] = x[k] / augmented_matrix[k][k]

    #Displaying solution 
    print("the following x vectors solve the linear system of equations:")
    for answer in range(n):
        print(f"x{answer+1} is {x[answer]}")
        

        


    

a_matrix = np.array([[1 ,1 , 4], [3, 7 , 4] , [7 , 8 , 5]])
b_matrix = np.array([[1] , [5], [4]])
gaussElimination(a_matrix, b_matrix)