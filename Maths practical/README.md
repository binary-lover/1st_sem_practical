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
    ~~~
        eqn1:read("equation 1 is=");
        eqn2:read("equation 2 is=");
        eqn3:read("equation 3 is=");
        eqn4:read("equation 4 is=");

        block(D:augcoefmatrix([eqn1,eqn2,eqn3,eqn4],[x,y,z,a]), 
            S:echelon(D),
        [p.q],X:[x,y,z,a, 1], [p,q]:matrix_size(S),
        for i:1 thru p do(for n:1 thru q do(d(i):=sum(S[i,n]-X[n],n,1,q)=0),
        s:makelist(d(i),i,1,p)),
        solve(s, [x,y,z,a]));
        if solve(s) = [] then print("system of given equations is inconsistent and have no solution") 
        else print("system of given equations is consistent");
    ~~~



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

    ~~~
        /* checking linear dependence of vector wether |A| = 0 or not if zero than it is linearly dependent. */
        v1:[1,2,3];
        v2:[4,5,6];
        v3:[7,8,9];

        /* creating matrix */
        a:transpose(matrix(v1,v2,v3));

        /* Finding determinant */
        determinant(a);
    ~~~
        /* Generate a linear combination of given vectors of Rn/ matrices */
        v1:matrix([1],[2],[3]);
        v2:matrix([4],[5],[6]);
        v3:matrix([7],[8],[9]);

        c1:2;
        c2:-1;
        c3:3;

        V:matrix([v1,v2,v3]);
        c:matrix([c1],[c2],[c3]);

        v:V.c;


#

*  Practical 8: - Find the orthonormal basis of a given vector space using the Gram-Schmidt orthogonalization process.

    ~~~
    load(eigen);
    Matrix_A: matrix([2,1,0,-1], [1,0,2,-1], [0,-2,1,0]);
    ~~~
        Orthogonal_Basis:gramschmidt(Matrix_A);
    ~~~
        A:((2^2)+(1^2)+((-1)^2)+(0^2))^0.5;
        B:[2,1,0,-1]/A;
    ~~~
        C:((0^2)+((-1/2)^2)+(2^2)+((-1/2)^2))^0.5;
        D:[0,-1/2,2,-1/2]/C;
    ~~~
        E:((-2/3)^2+(2^2/3)^2+(1/3)^2+0^2)^0.5; 
        F:[-(2/3),2^2/3,1/3,0]/E;
    ~~~
        Orthonormal_Basis:matrix(B,D,F);

#

* Practical 9: - Check the diagonalizable property of matrices and find the corresponding eigenvalue and verify the Cayley- Hamilton theorem.

     ~~~
      load(eigen);
     ~~~
      load(matrix);
     ~~~
      A: matrix([1,2,1],[6,-1,0],[-1,-2,-1]);
     ~~~
      nondiagonalizable(A);
     ~~~
      load(nchrpl);
     ~~~
      ncharpoly(A,lambda);

#

* Practical 10: - Application of Linear algebra: Coding and decoding of messages using nonsingular matrices

  ~~~
   /* Defining a nonsingular matrix for encoding and decoding */

   A: matrix([2,3],[1,4]);

   /* Define a message vector */
   message: matrix([1],[2]);

   /*Encoding: Multiply the message by the nonsingular matrix*/
   encoded_message : A.message;

   /* Decoding: Multipying the encoded message by the non-singular matrix */
   A_inverse : invert(A);
   decoded_message: A_inverse.encoded_message;

   /*Display the results */
   print("Output Message:");
   print(message);
   print("Encoded Message");
   print(encoded_message);
   print("Decoded Message");
   print(decoded_message);

#

* Practical 11: - Compute Gradient of a scalar field.

  ~~~

  /* Defining the Variables */

  load(vector);

  /* Define the scalar field in terms of variables x,y and z */
  scalar_field: x^2 + 2*y - 3*z;

  /*Compute the gradient of the scalar field*/
  gradient_field : gradient(scalar_field,[x,y,z]);

  /* Display the gradient field */
  print("Gradient of the Scalar Field");
  print(gradient_field);
  
#

* Practical 12: - Compute Divergence of a vector field.

  ~~~

  /* Load Vector */

  load("vector");
  /* Define the Variables */
  [wx,wy,wz]:[x,y,z];

  /* Define the vector field in terms of variables x,y and z */
  vector_field: [2*x*y, x^2-z, y^2*z];
  /*Compute the divergence of the vector field*/
  Divergence : div(vector_field,wx,wy,wz);

  /* Display the curl vector */
  print("Divergence of the Vector Field");
  print(Divergence);
  
#

* Practical 13: - Compute Divergence of a vector field.

  ~~~
  /* Load Vector */

  /* Define the Variables */
  [wx,wy,wz]:[x,y,z];

  /* Define the vector field in terms of variables x,y and z */
  vector_field: [2*y, 3*x*z, x^2-y];
  /*Compute the curl of the vector field*/
  c: curl(vector_field,wx,wy,wz);

  /* Display the curl vector */
  print("Curl of the Vector Field");
  print(c);
