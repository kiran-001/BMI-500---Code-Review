import numpy as np

def troublesmakers(n):
    juice = 1
    milkshake = 1
    for i in range(n):
        #daughter
        pour = 0.35 * juice
        milkshake += pour
        juice -= pour
        
        #son
        pour = 0.2 * milkshake
        juice += pour
        milkshake -= pour
        
    return np.array([juice, milkshake])

final_contents = troublesmakers(10)
print(final_contents)
