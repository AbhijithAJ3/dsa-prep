#Given two strings s1 and s2, return True if s2 is a rotation of s1; otherwise, return False.


def are_rotations(s1, s2):
    # Write your code here
     
    doubled=s1+s1
    if len(s1)!=len(s2):
        return False
    else:
        return s2 in doubled
        
     
if __name__ == '__main__':
    s1 = "water"
    s2 = "terwa"
    result = are_rotations(s1, s2)
    print(result)
