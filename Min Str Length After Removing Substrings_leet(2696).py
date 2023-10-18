2696. Minimum String Length After Removing Substrings

You are given a string s consisting only of uppercase English letters.
You can apply some operations to this string where, in one operation, you can
remove any occurrence of one of the substrings "AB" or "CD" from s.
Return the minimum possible length of the resulting string that you can obtain.
Note that the string concatenates after removing the substring and could produce
new "AB" or "CD" substrings.

Example 1:

Input: s = "ABFCACDB"
Output: 2
Explanation: We can do the following operations:
- Remove the substring "ABFCACDB", so s = "FCACDB".
- Remove the substring "FCACDB", so s = "FCAB".
- Remove the substring "FCAB", so s = "FC".
So the resulting length of the string is 2.
It can be shown that it is the minimum length that we can obtain



from collections import deque
class Solution:
    def minLength(self, s: str) -> int:
        st=deque()
        for i in s:
            if not st:
                st.append(i)
            elif i=='B' and st[-1]=='A':
                st.pop()
            elif i=='D' and st[-1]=='C':
                st.pop()
            else:
                st.append(i)
        return len(st)
        