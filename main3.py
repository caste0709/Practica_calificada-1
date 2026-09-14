import numpy as np


def verificar_ortogonalidad(dtype):
    ks = np.arange(1, 11)
    residuos = []
    for k in ks:
        a = np.array([1.0, 0.0, 0.0], dtype=dtype)
        b = np.array([1.0, 10.0**(-k), 0.0], dtype=dtype)
        c = np.cross(a, b)
        residuo = np.abs(np.dot(a, c))
        residuos.append(residuo)
    return ks, np.array(residuos, dtype=dtype)


print("VERIFICACIÓN DE LA ORTOGONALIDAD TEÓRICA  a . (a x b) = 0")

ks, res32 = verificar_ortogonalidad(np.float32)
_, res64 = verificar_ortogonalidad(np.float64)

print(f"{'k':>2} | {'residuo float32':>16} | {'residuo float64':>16}")
print("-" * 45)
for k, r32, r64 in zip(ks, res32, res64):
    print(f"{k:2d} | {r32:16.2e} | {r64:16.2e}")