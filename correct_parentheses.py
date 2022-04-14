def correct_parentheses(stuff):
    if len(stuff)%2 == 1:
        return False
    if stuff is None or stuff == '':
        return False
    opening = ['(','{','[']
    closing = [')','}',']']
    if stuff[0] not in opening:
        return False
    if stuff[len(stuff)-1] not in closing:
        return False
    stack = []
    for bracket in stuff:
        if bracket in opening:
            stack.append(bracket)
        elif bracket in closing:
            if len(stack) < 1:
                return False
            pop_stack = stack.pop()
            if pop_stack != opening[closing.index(bracket)]:
                return False
    if stack != []:
        return False
    else:
        return True
            
xx = "{}(){{}}{{(())}}"
print(correct_parentheses(xx))