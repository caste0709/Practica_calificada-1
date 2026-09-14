import numpy as np


def calcular_producto_vectorial(dtype):
    ks = np.arange(1, 11)
    c_list = []
    for k in ks:
        a = np.array([1.0, 0.0, 0.0], dtype=dtype)
        b = np.array([1.0, 10.0**(-k), 0.0], dtype=dtype)
        c = np.cross(a, b)
        c_list.append(c)
        print(f"k={k:2d} | c = a x b = {c}")
    return ks, c_list


print("CÁLCULO DEL PRODUCTO VECTORIAL c = a x b (dtype=float32)")
ks, c_list = calcular_producto_vectorial(np.float32)