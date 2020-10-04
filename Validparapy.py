def checkValidString(s):
        left = 0
        right = 0
        for c in s:
            if c == "(":
                left += 1
                right += 1

            elif c == ")":
                left = max(left-1,0)
                right -= 1
            elif c == "*":
                left = max(left-1,0)
                right += 1
            if right < 0:
                    return False
                
        if left<=0 and 0<=right:
            return True
        return False
s = "(())((())()()(*)(*()(())())())()()((()())((()))(*"

checkValidString(s)