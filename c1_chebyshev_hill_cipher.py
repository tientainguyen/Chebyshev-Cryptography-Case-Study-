import numpy as np

# --- 1. CHEBYSHEV EVALUATION (MATRIX RECURSION VS. TRIGONOMETRIC) ---
x = 0.065
s = 2731
r = 1951
rs = r * s

def chebyshev_trig(n, x_val):
    return np.cos(n * np.arccos(x_val))

def chebyshev_matrix(n, x_val):
    # Transition matrix for [T_n, T_{n+1}]^T = [[0, 1], [-1, 2x]]^n * [T_0, T_1]^T
    M = np.array([[0.0, 1.0], [-1.0, 2.0 * x_val]], dtype=np.float64)
    Mn = np.linalg.matrix_power(M, n)
    # T_0(x) = 1, T_1(x) = x
    T0_T1 = np.array([1.0, x_val])
    return (Mn @ T0_T1)[0]

for name, val in [("T_s(x)", s), ("T_r(x)", r), ("T_rs(x)", rs)]:
    t_trig = chebyshev_trig(val, x)
    t_mat = chebyshev_matrix(val, x)
    diff = abs(t_trig - t_mat)
    print(f"{name}: Trig = {t_trig:.6f}, Matrix = {t_mat:.6f}, Abs Diff = {diff:.2e}")


# --- 2. HILL CIPHER DECRYPTION OF "GERPLYNDBX" ---
import numpy as np

# Alphabet mapping: A=1, B=2, ..., Z=26
def char2num(c): return ord(c) - ord('A') + 1
def num2char(n): return chr(int(n) - 1 + ord('A'))

ciphertext = "GERPLYNDBX"
nums = [char2num(c) for c in ciphertext]

# FIX 1: Reshape using column-major order ('F')
M_tilde = np.array(nums).reshape(2, -1, order='F')  # 2 x 5 matrix

A = np.array([[1, 2], [3, 4]])
mod = 29

det_A = int(round(np.linalg.det(A))) % mod  # det = -2 = 27 mod 29
det_inv = pow(det_A, -1, mod)               # 27^(-1) mod 29 = 14

adj_A = np.array([[A[1, 1], -A[0, 1]], [-A[1, 0], A[0, 0]]]) % mod
A_inv = (det_inv * adj_A) % mod

# Decrypt M = A^(-1) * M_tilde mod 29
M_decrypted = (A_inv @ M_tilde) % mod

# FIX 2: Flatten column-by-column to read characters in correct sequence
plaintext = "".join(num2char(num) for num in M_decrypted.flatten(order='F'))

print(f"Decrypted Matrix:\n{M_decrypted}")
print(f"Decrypted Message: {plaintext}")
