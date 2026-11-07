# Chebyshev Polynomials in Cryptography and Numerical Interpolation

This repository contains the Python implementations for **Part C: Case Study and Extension**, based on Section 4.7 of *Linear Algebra With Machine Learning and Data* (Crista Arangala). 

It covers Chebyshev polynomial evaluation, Hill cipher decryption, discrete modular Chebyshev cryptography, and polynomial interpolation of Runge's function.

---

## Table of Contents

- [Overview](#overview)
- [Repository Structure](#repository-structure)
- [Modules & Implementations](#modules--implementations)
  - [C1: Chebyshev Evaluation & Hill Cipher Decryption](#c1-chebyshev-evaluation--hill-cipher-decryption)
  - [C2: Extension – Modular Chebyshev Cryptography (ℤₚ)](#c2-extension--modular-chebyshev-cryptography-ℤₚ)
  - [C3: Equally Spaced vs. Chebyshev Interpolation](#c3-equally-spaced-vs-chebyshev-interpolation)
- [Requirements & Installation](#requirements--installation)
- [Usage](#usage)
- [Citation & References](#citation--references)

---

## Overview

Chebyshev polynomials $T_n(x)$ possess unique algebraic and trigonometric properties:
1. **Trigonometric Representation:** $T_n(x) = \cos(n \arccos x)$ for $x \in [-1, 1]$.
2. **Matrix Recurrence:** $\begin{pmatrix} T_n \\ T_{n+1} \end{pmatrix} = \begin{pmatrix} 0 & 1 \\ -1 & 2x \end{pmatrix}^n \begin{pmatrix} T_0 \\ T_1 \end{pmatrix}$.
3. **Commutativity Under Composition:** $T_r(T_s(x)) = T_{rs}(x) = T_s(T_r(x))$.

This project explores their applications in public-key cryptography, security vulnerabilities over continuous real numbers, modular arithmetic fixes, and their optimality in mitigating Runge's phenomenon during function approximation.

---

## Repository Structure

```text
.
├── README.md                      # Project documentation and summary
├── c1_chebyshev_hill_cipher.py    # Script for C1 (Chebyshev float comparison & Hill cipher)
├── c2_modular_chebyshev.py        # Script for C2 (Modular arithmetic key exchange)
├── c3_chebyshev_interpolation.py  # Script for C3 (Runge function error table & plots)
```

---

## Modules & Implementations

### C1: Chebyshev Evaluation & Hill Cipher Decryption
* **File:** `c1_chebyshev_hill_cipher.py`
* **Key Tasks:**
  * Computes $T_s(x)$, $T_r(x)$, and $T_{rs}(x)$ for parameters $x = 0.065$, $s = 2731$, $r = 1951$ using matrix powers versus trigonometric formula $\cos(n \arccos x)$.
  * Compares floating-point accuracy between the matrix recurrence and trigonometric approaches.
  * Inverts the $2 \times 2$ matrix $A = \begin{pmatrix} 1 & 2 \\ 3 & 4 \end{pmatrix} \pmod{29}$ using modular determinant inversion.
  * Decrypts the ciphertext `"GERPLYNDBX"` back to the original plaintext matrix.

### C2: Extension – Modular Chebyshev Cryptography (ℤₚ)
* **File:** `c2_modular_chebyshev.py`
* **Key Tasks:**
  * **Vulnerability Analysis:** Explains why real-number key exchanges are insecure: an attacker can extract secret key $s$ via the continuous arc-cosine identity $s = \frac{\pm \arccos(T_s(x)) + 2\pi k}{\arccos(x)}$.
  * **Modular Fix:** Replaces continuous field $\mathbb{R}$ with finite field $\mathbb{Z}_p$ (integers modulo a prime $p$).
  * **Implementation:** Implements modular matrix binary exponentiation to perform Diffie-Hellman-style secret key exchange mod $p$.

### C3: Equally Spaced vs. Chebyshev Interpolation
* **File:** `c3_chebyshev_interpolation.py`
* **Key Tasks:**
  * Interpolates Runge's function $f(x) = \frac{1}{1 + 25x^2}$ over $x \in [-1, 1]$ for polynomial degrees $n = 5, 10, 20$.
  * Compares **equally spaced nodes** against **Chebyshev nodes** $x_k = \cos\left(\frac{2k+1}{2n+2}\pi\right)$.
  * Generates a comparative **Maximum Absolute Error Table** and outputs 3-panel comparative plots illustrating Runge's phenomenon at interval endpoints.

---

## Requirements & Installation

Ensure you have Python 3.8+ installed along with the required libraries:

```bash
pip install numpy scipy matplotlib
```

---

## Usage

Run any of the individual scripts from your terminal:

```bash
# Execute Part C1
python c1_chebyshev_hill_cipher.py

# Execute Part C2
python c2_modular_chebyshev.py

# Execute Part C3 (displays error table and generates plots)
python c3_chebyshev_interpolation.py
```

---

## Citation & References

* Arangala, Crista. *Linear Algebra With Machine Learning and Data*. CRC Press. Section 4.7: "CASE STUDY: Chebyshev Polynomials and Cryptography," pages 164–167.
