# Maima Practical With code

* Practical 1: - Create and transform vectors and matrices (the transpose vector (matrix) conjugate transpose of a vector (matrix))

    ~~~
        V:matrix([1],[2],[3]); /*Vector V*/
    ~~~
    
    ~~~
        M:matrix([1,2,3],[4,5,6],[7,8,9]); /*Matrix M*/
    ~~~
    ~~~
        transpose(V); /*Transpose of V */
        transpose(M);
    ~~~
    ~~~
        conjugate(V);
        conjugate(M);
    ~~~
    ~~~
        transpose(conjugate(M));
        transpose(conjugate(V));
    ~~~

#

* Practical 2: - Generate the matrix into echelon form and find its rank.

    ~~~
        M:matrix([1,2,3],[4,5,6],[7,8,9]); /*Matrix M*/
        echelon(M);
        rank(M);
    ~~~

#

* Practical 3: - Find cofactors, determinant, adjoint and inverse of a matrix

    ~~~
        /*Create Matrix A*/
        A:matrix([2,3,1],[0,-3,4],[5,2,3]); /*Matrix A*/
    ~~~
        /*Cofactors matrix*/
        transpose(adjoint(A));
    ~~~
        /*determinant of A*/
        determinant(A);
    ~~~    
        /*adjoint*/
        adjoint(A);
    ~~~
        /*inverse*/
        invert(A);
    ~~~

#

* Practical 4: - Solve a system of Homogeneous and non-homogeneous equations using Gauss elimination method




#

* Practical 5: - Solve a system of Homogeneous equations using the Gauss Jordan method.

    ~~~
        Coefficient_matrix: matrix([1,1,1],[2,-3,4],[3,4,5]);
        Column_Matrix: matrix([9,13,40]);
    ~~~
        Inv_of_Coefficient_Matrix: invert(Coefficient_Matrix);
    ~~~
        Solution_of_the_system_of_Equations: Inv_of_Coefficient_Matrix .Column_Matrix;
    ~~~

#
* Practical 6: -Generate basis of column space, null space, row space and left null space of a matrix space

    ~~~
        /* Creating Matrix */
        A: matrix([-1,3,1],[1,1,0],[1,1,0]);
    ~~~
        /* Basis of comumn space*/
        columnspace(A);
    ~~~
        /*create nullspace*/
        nullspace(A); 
    ~~~
        /* Row space */
        rowspace(A);
    ~~~
        /* left Null space */
        left_null_space: nullspace(transpose(A));
    ~~~

#
* Practical 7: - Check the linear dependence of vectors. Generate a linear combination of given vectors of Rn/ matrices of the same size and find the transition matrix of given matrix space


