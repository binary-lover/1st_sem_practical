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

