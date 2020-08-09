def cholesky_decomp(A:list) -> np.array():
    """
    Perform Cholesky Decomposition using
    Cholesky-Banachiewicz Algorithm

    Args:
        list: Two dimensional list constaing
        the target correlation matrix.

    Return:
        np.array(): a numpy array containing
        the resulting lower triangular matrix.

    """

    n = len(A)

    # Initialize a zero matrix for L.
    L = np.zeros(A.shape)

    # Perform the Cholesky decomposition
    for j in range(n):
        for i in range(j, n):
            symmetric_sum = sum(
                L[i][k] * L[j][k] for k in range(i))

            if (j == i): # Diagonal elements
                L[j][j] = np.sqrt(
                    A[j][j] - symmetric_sum)
            else:
                # Non-diagonal elements
                L[i][j] = (1.0 / L[j][j] *
                    (A[i][j] - symmetric_sum))
    return L
