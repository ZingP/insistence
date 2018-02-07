"""
Given a string, find the length of the longest substring without repeating characters.

Examples:

Given "abcabcbb", the answer is "abc", which the length is 3.

Given "bbbbb", the answer is "b", with the length of 1.

Given "pwwkew", the answer is "wke", with the length of 3. Note that the answer must be a substring, "pwke" is a subsequence and not a substring.
"""


class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        st = []
        count = None
        for i in s:
            if i not in st:
                st.append(i)
            else:
                if count == None or len(st) > count:
                    count = len(st)
                st = st[st.index(i)+1:]
                st.append(i)
        if count == None or len(st) > count:
            count = len(st)
        return count

# O(n)
class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        start = max_length = 0
        used_dic = {}
        for i in range(len(s)):
            if s[i] in used_dic and start <= used_dic[s[i]]:
                start = used_dic[s[i]] + 1
            else:
                max_length = max(max_length, i - start + 1)
            used_dic[s[i]] = i
        return max_length
                         
                        
                        




                         
