def minUniqueSum(A):
    add = A[0];
    prev = A[0];

    for i in range(1,len(A)): 
        curr = A[i];

        if( prev >= curr ):
            curr = prev+1;
        
        add += curr;
        prev = curr;
    

    return add;