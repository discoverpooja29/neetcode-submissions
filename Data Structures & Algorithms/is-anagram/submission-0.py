class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        if not (s.islower() and t.islower()):
            return False

        dict1 = dict.fromkeys(s, 0)
        dict2 = dict.fromkeys(t, 0)

        for l in s:
            if l in dict1:
                dict1[l] = dict1[l] + 1

        for l in t:
            if l in dict2:
                dict2[l] = dict2[l] + 1

        return dict1 == dict2