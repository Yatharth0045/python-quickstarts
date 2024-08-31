str = "aabbccbbaa"
k = 2

def get_substr(str):
    substrings = []
    n = len(str)
    for i in range(n):
        for j in range(i+1, n+1):
            substrings.append(str[i:j])
    # print(substrings) 
    return substrings

def get_occurance(substrs, k):
    occurance = {}
    true_values = []
    substr_count = 0
    for str in substrs:
        for char in str:
            if char not in occurance:
                occurance[char] = 1
            else:
                occurance[char] += 1
        
        # print(occurance)
        satisfy_condition = True
        
        
        for occ in list(occurance.values()):
            if occ !=k:
                satisfy_condition = False
                break
                
        # print(list(occurance.values()))
        # for key,value in occurance.items():
        #     # print(value)
        #     if value != k:
        #         satisfy_condition = False
        #         break

        # print(satisfy_condition)
        if satisfy_condition:
            true_values.append(occurance)
            substr_count += 1
            
        # print(occurance)
        occurance = {}
    
    return true_values,substr_count

sub_strings = get_substr(str)
print(sub_strings)
print(get_occurance(sub_strings,k))
