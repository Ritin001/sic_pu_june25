'''def isSameReflection(original_string,rotated_string):
    if len(original_string) != len(rotated_string):
        return False
    else:
        for i in range(len(original_string)):
            if(original_string[i+1:]+ original_string[0:i+1] ) == rotated_string:
                return True
            
        return False
print(isSameReflection("hello", "lohel"))  # True
print(isSameReflection("hello", "world"))  # False'''


def isSameReflection(original_string, rotated_string):
    original_string= original_string+ original_string
    if rotated_string in original_string:
        return True
    else:        return False

print(isSameReflection("hello", "lohel"))  
print(isSameReflection("hello", "world"))  # False   