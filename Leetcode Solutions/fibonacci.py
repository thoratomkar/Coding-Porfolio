def fib(self, N):
        """
        :type N: int
        :rtype: int
        """
        f0,f1 = 0,1
        
        if N == 0:
            return 0
        for i in range(2,N):
            fn = f0 + f1
            f0 = f1
            f1 = fn
        fn = f0 + f1
        return fn