class Solution:
    def groupStrings(self, strings: List[str]) -> List[List[str]]:

        def key(s):
            k = '#'
            for i in range(1, len(s)):
                b = s[i]
                a = s[i - 1]
                d = (ord(b) + 26 - ord(a)) % 26
                k = k + str(d) + '#'
            return k

        num = len(strings)
        if num <= 0:
            return None

        r_dict = {}
        result = []
        for i in range(len(strings)):
            k = key(strings[i])
            if k in r_dict.keys():
                r_dict[k].append(strings[i])
            else:
                r_dict[k] = [strings[i]]

        result = list(r_dict.values())
        return result





