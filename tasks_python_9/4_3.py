from collections import deque

def brackets(line):
    dq_line = deque()
    for brackets in line:
        if len(dq_line) is 0 and brackets is ")":
            return False
        elif brackets is "(":
            dq_line.append(brackets)
        elif brackets is ")":
            if len(dq_line) is 0:
                return False
            else:
                dq_line.pop()
    
    if len(dq_line) is 0:
        return True
    else:
        return False
    
print(brackets("(()())"))
# True
print(brackets(""))
# True
print(brackets("(()()))"))
# False
print(brackets(")"))
    
    
            