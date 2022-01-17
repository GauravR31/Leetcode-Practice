class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        for r in range(len(image)):
            image[r] = image[r][::-1]
            
        for r in range(len(image)):
            for c in range(len(image[r])):
                if image[r][c] == 0:
                    image[r][c] = 1
                else:
                    image[r][c] = 0
                    
        return image