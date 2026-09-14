import numpy as np
import matplotlib.pyplot as plt


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

ks, res32 = verificar_ortogonalidad(np.float32)
_, res64 = verificar_ortogonalidad(np.float64)
eps32 = np.finfo(np.float32).eps
eps64 = np.finfo(np.float64).eps
res32_plot = np.maximum(res32, eps32)
res64_plot = np.maximum(res64, eps64)

plt.figure(figsize=(8, 5))
plt.semilogy(ks, res32_plot, 'o-', label=f'float32 (eps ≈ {eps32:.1e})')
plt.semilogy(ks, res64_plot, 's-', label=f'float64 (eps ≈ {eps64:.1e})')
plt.xlabel('k')
plt.ylabel(r'Residuo $|\vec{a}\cdot\vec{c}|$')
plt.title('Residuo de ortogonalidad numérica vs. k')
plt.legend()
plt.grid(True, which='both', ls='--', alpha=0.5)
plt.tight_layout()
plt.savefig('residuo_final.png', dpi=150)