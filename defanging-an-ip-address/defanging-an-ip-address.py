class Solution:
    def defangIPaddr(self, address: str) -> str:
        addressList = list(address)
        l = len(addressList)
        for i in range(l):
            if addressList[i] == ".":
                addressList[i] = "[.]"
                
        res = ""
        return res.join(addressList)
                