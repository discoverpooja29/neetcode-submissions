import base64
import re

class Solution:

    '''
    def encode(self, strs: List[str]) -> str:
        result = ""
        for s in strs:
            encoded = base64.b64encode(s.encode("utf-8"))
            result += str(encoded)
        return result

    def decode(self, s: str) -> List[str]:
        matches = re.findall(r"b'([A-Za-z0-9+/]*={0,2})'", s)
        result = []
        for s in matches:
            result.append(base64.b64decode(s).decode("utf-8"))
        return result
    '''

    def encode(self, strs: List[str]) -> str:
        s = ""
        for i in strs:
            s+=f"{i}|-|"
        return s
    def decode(self, s: str) -> List[str]:
        return s.split("|-|")[:-1]
       
