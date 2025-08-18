import numpy as np

def calculate(list):
    """
    Recebe uma lista com 9 números, converte para uma matriz 3x3 (NumPy) e
    retorna um dicionário com mean, variance, standard deviation, max, min e sum
    para:
      - colunas (axis=0)
      - linhas (axis=1)
      - array inteiro (flattened)

    Levanta ValueError se a lista não tiver exatamente 9 elementos.
    """
    if len(list) != 9:
        raise ValueError("List must contain nine numbers.")

    arr = np.array(list).reshape(3, 3)

    calculations = {
        'mean': [
            np.mean(arr, axis=0).tolist(),
            np.mean(arr, axis=1).tolist(),
            np.mean(arr).tolist()
        ],
        'variance': [
            np.var(arr, axis=0).tolist(),
            np.var(arr, axis=1).tolist(),
            np.var(arr).tolist()
        ],
        'standard deviation': [
            np.std(arr, axis=0).tolist(),
            np.std(arr, axis=1).tolist(),
            np.std(arr).tolist()
        ],
        'max': [
            np.max(arr, axis=0).tolist(),
            np.max(arr, axis=1).tolist(),
            np.max(arr).tolist()
        ],
        'min': [
            np.min(arr, axis=0).tolist(),
            np.min(arr, axis=1).tolist(),
            np.min(arr).tolist()
        ],
        'sum': [
            np.sum(arr, axis=0).tolist(),
            np.sum(arr, axis=1).tolist(),
            np.sum(arr).tolist()
        ]
    }

    return calculations
