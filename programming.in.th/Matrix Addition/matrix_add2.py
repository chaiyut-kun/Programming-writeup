import numpy as np
m , n = map(int , input().split())
main_ls = np.array([[int(i) for i in input().split()] for _ in range(m)])
add_ls = np.array([[int(i) for i in input().split()] for _ in range(m)])
print("\n".join([' '.join(map(str , res)) for res in main_ls+add_ls]))