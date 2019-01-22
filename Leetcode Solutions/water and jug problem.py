def canMeasureWater(self, x, y, z):
        """
        :type x: int
        :type y: int
        :type z: int
        :rtype: bool
        """
        if(x + y < z):
            return False;
    
        if( x == z or y == z or x + y == z ):
            return True
        def hcfnaive(a,b): 
            if(b==0): 
                return a 
            else: 
                return hcfnaive(b,a%b) 
        
        a = hcfnaive(x,y)
        
        return z%a == 0