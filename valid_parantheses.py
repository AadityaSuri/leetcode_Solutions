class Solution:
    def isValid(self, s: str) -> bool:

        hmap = {
            '{' : '}',
            '(' : ')',
            '[' : ']'
        }

        brackstack = []

        for bracket in s:
            if bracket in hmap:
                brackstack.append(bracket)
            else:
                # if stack gets empty before the entire string is parsed
                if len(brackstack) == 0:
                    return False
                
                # if the closing current bracket doesnt match with the corresponding closing bracket of the TOS
                if bracket != hmap[brackstack[-1]]:
                    return False

                brackstack.pop()
            
        return len(brackstack) == 0