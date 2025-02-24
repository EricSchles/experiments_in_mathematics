import math
import json

triplets = []
for i in range(1, 1001):
    for j in range(1, 1001):
        result = i**2 + j**2
        result_square_root = math.sqrt(result)
        if int(result_square_root) == result_square_root:
            triplets.append(
                (i,j,result_square_root)
            )
    
triplets = list(set(triplets))
json.dump(triplets, open("triplets.json", "w"))
