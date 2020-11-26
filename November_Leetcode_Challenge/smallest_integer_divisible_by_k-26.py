    def smallestRepunitDivByK(self, K: int) -> int:    
        if K % 2 ==0 or K % 5==0:
            return -1       
        module = 1
        for Ndigits in range(1, K+1):
            if module % K == 0:
                return Ndigits
            module = (module * 10 + 1) % K