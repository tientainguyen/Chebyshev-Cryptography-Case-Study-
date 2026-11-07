def chebyshev_mod(n, x, p):
    """Computes T_n(x) mod p using matrix exponentiation mod p."""
    if n == 0: return 1 % p
    if n == 1: return x % p
    
    # State transition: [T_n, T_{n+1}] = [[0, 1], [-1, 2x]]^n * [1, x] mod p
    # Matrix power mod p using binary exponentiation
    A = [[0, 1], [-1 % p, (2 * x) % p]]
    
    def mat_mult(mat1, mat2):
        return [
            [(mat1[0][0]*mat2[0][0] + mat1[0][1]*mat2[1][0]) % p, (mat1[0][0]*mat2[0][1] + mat1[0][1]*mat2[1][1]) % p],
            [(mat1[1][0]*mat2[0][0] + mat1[1][1]*mat2[1][0]) % p, (mat1[1][0]*mat2[0][1] + mat1[1][1]*mat2[1][1]) % p]
        ]
    
    res = [[1, 0], [0, 1]]
    base = A
    power = n
    while power > 0:
        if power % 2 == 1:
            res = mat_mult(res, base)
        base = mat_mult(base, base)
        power //= 2
        
    return (res[0][0] * 1 + res[0][1] * x) % p

# Demonstration of Diffie-Hellman-style key exchange mod p
p = 101       # Prime modulus
base_x = 5    # Base x mod p
s_key = 27    # Secret s
r_key = 19    # Secret r

# Public keys
T_s = chebyshev_mod(s_key, base_x, p)
T_r = chebyshev_mod(r_key, base_x, p)

# Shared secret key computation
shared_s = chebyshev_mod(s_key, T_r, p)
shared_r = chebyshev_mod(r_key, T_s, p)

print(f"Mod p Diffie-Hellman Check: Shared Key S = {shared_s}, Shared Key R = {shared_r}")
