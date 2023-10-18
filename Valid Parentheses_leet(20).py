20. Valid Parentheses

Given a string s containing just the characters '(', ')', '{', '}', '[' and ']',
determine if the input string is valid.

An input string is valid if:
Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
 
Example 1:

Input: s = "()"
Output: true

def isValid(self, s: str) -> bool:
        st=deque()
      
        for i in s:
            if i=="{" or i=="(" or i=="[":
                st.append(i)
            else:
                if not st:
                    return False
                elif i==')' and st[-1]=='(':
                    st.pop()
                elif i==']' and st[-1]=='[':
                    st.pop()
                elif i=='}' and st[-1]=='{':
                    st.pop()
                else:
                     return False
               
        if not st:
            return True
        else:
            return False

        