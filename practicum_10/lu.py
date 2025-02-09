import numpy as np
from numpy.typing import NDArray


def lu(A: NDArray, permute: bool) -> tuple[NDArray, NDArray, NDArray]:
    n = len(A)
    L = np.eye(n)
    P = np.eye(n)
    U = A.copy()   
    
    for j in range(n):
        max_row_idx = j
        max_row_val = abs(U[j, j])

        if permute:
            for i in range(j + 1, n):
                if abs(U[i, j]) > max_row_val:
                    max_row_idx = i
                    max_row_val = abs(U[i, j])

        if j != max_row_idx:
            P[[j, max_row_idx]] = P[[max_row_idx, j]]
            L[[j, max_row_idx], :j] = L[[max_row_idx, j], :j]
            U[[j, max_row_idx], :] = U[[max_row_idx, j], :]

        L[j:, j] = U[j:, j] / U[j, j]
        U[j+1:, j:] -= L[j+1:, j, np.newaxis] * U[j, j:]

    return L, U, P

def solve(L: NDArray, U: NDArray, P: NDArray, b: NDArray) -> NDArray:
    
    # LU x = Pb
    A = np.matmul(L, U)
    B = np.matmul(P, b)
    x = np.linalg.solve(A, B)
    return x


def get_A_b(a_11: float, b_1: float) -> tuple[NDArray, NDArray]:
    A = np.array([[a_11, 1.0, -3.0], [6.0, 2.0, 5.0], [1.0, 4.0, -3.0]])
    b = np.array([b_1, 12.0, -39.0])
    return A, b


if __name__ == "__main__":
    # Let's implement the LU decomposition with and without pivoting
    # and check its stability depending on the matrix elements
    p = 14  # modify from 7 to 16 to check instability
    a_11 = 3 + 10 ** (-p)  # add/remove 10**(-p) to check instability
    b_1 = -16 + 10 ** (-p)  # add/remove 10**(-p) to check instability
    A, b = get_A_b(a_11, b_1)
    # With pivoting
    L, U, P = lu(A, permute=True)
    x = solve(L, U, P, b)
    assert np.all(np.isclose(x, [1, -7, 4])), f"The anwser {x} is not accurate enough"
    # Without pivoting
    L, U, P = lu(A, permute=False)
    x_ = solve(L, U, P, b)
    assert np.all(np.isclose(x_, [1, -7, 4])), f"The anwser {x_} is not accurate enough"
