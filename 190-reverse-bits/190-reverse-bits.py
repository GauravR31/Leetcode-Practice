class Solution:
    def reverseBits(self, n: int) -> int:
        binary = []
        res = 0
        
        for i in range(32):
            binary.append(n&1)
            n = n >> 1
        
        print(binary)
        binary = binary[::-1]
        for i in range(len(binary)):
            if binary[i]:
                res += 2**(i)
        
        return res
            