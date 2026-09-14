import numpy as np
def definir_vectores(dtype):
    ks = np.arange(1, 11)
    a_list, b_list = [], []
    for k in ks:
        a = np.array([1.0, 0.0, 0.0], dtype=dtype)
        b = np.array([1.0, 10.0**(-k), 0.0], dtype=dtype)
        a_list.append(a)
        b_list.append(b)
        print(f"k={k:2d} | a = {a} | b = {b}")
    return ks, a_list, b_list

print("DEFINICIÓN DE VECTORES CASI PARALELOS (dtype=float32)")
ks, a_list, b_list = definir_vectores(np.float32)
