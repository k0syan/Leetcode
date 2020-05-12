class Solution:
    def defangIPaddr(self, address: str) -> str:
        address = address.replace('.', '[.]')
        return address
    
# One liner
class Solution:
    def defangIPaddr(self, address: str) -> str:
        return '[.]'.join(address.split('.'))
