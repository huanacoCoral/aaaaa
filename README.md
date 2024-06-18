import numpy as np
import scipy.sparse as sp
import multiprocessing as mp
from multiprocessing import Pool

# Generar matrices dispersas aleatorias grandes
def generate_sparse_matrix(n_rows, n_cols, density=0.01):
    return sp.random(n_rows, n_cols, density=density, format='csr')

# Multiplicar submatrices
def multiply_submatrices(args):
    A, B, rows_range = args
    return A[rows_range].dot(B)

# Multiplicar matrices dispersas usando multiprocesamiento
def parallel_sparse_matrix_multiply(A, B, n_processes=None):
    n_processes = n_processes or mp.cpu_count()
    n_rows = A.shape[0]

    # Dividir las filas de A para los subprocesos
    chunk_size = int(np.ceil(n_rows / n_processes))
    row_chunks = [(i * chunk_size, min((i + 1) * chunk_size, n_rows)) for i in range(n_processes)]

    # Preparar los argumentos para los subprocesos
    args = [(A, B, slice(*rows)) for rows in row_chunks]

    # Usar un pool de procesos para realizar la multiplicación
    with Pool(processes=n_processes) as pool:
        result_chunks = pool.map(multiply_submatrices, args)

    # Combinar los resultados
    return sp.vstack(result_chunks)

if __name__ == "__main__":
    n_rows, n_cols = 1000, 1000
    density = 0.01

    # Generar dos matrices dispersas grandes
    A = generate_sparse_matrix(n_rows, n_cols, density)
    B = generate_sparse_matrix(n_cols, n_rows, density)

    # Multiplicar las matrices usando paralelización
    C = parallel_sparse_matrix_multiply(A, B)

    print("Multiplicación de matrices dispersas completada.")
    print("Dimensiones de la matriz resultante:", C.shape)
