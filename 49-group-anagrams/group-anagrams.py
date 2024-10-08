class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        x = {}
        st_w = ''
        for w in strs:
            st_w= ''.join(sorted(w))

            if st_w in x :
                x[st_w].append(w)
            else:
                x[st_w] = [w]
        return list(x.values())