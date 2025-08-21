import unittest
import numpy as np
import mean_var_std

class UnitTests(unittest.TestCase):
    def test_calculate(self):
        data = [2, 6, 2, 8, 4, 0, 1, 5, 7]
        actual = mean_var_std.calculate(data)

        arr = np.array(data).reshape(3, 3)
        expected = {
            'mean': [
                np.mean(arr, axis=0).tolist(),
                np.mean(arr, axis=1).tolist(),
                np.mean(arr).item()
            ],
            'variance': [
                np.var(arr, axis=0).tolist(),      # ddof=0 (populacional)
                np.var(arr, axis=1).tolist(),
                np.var(arr).item()
            ],
            'standard deviation': [
                np.std(arr, axis=0).tolist(),      # ddof=0 (populacional)
                np.std(arr, axis=1).tolist(),
                np.std(arr).item()
            ],
            'max': [
                np.max(arr, axis=0).tolist(),
                np.max(arr, axis=1).tolist(),
                np.max(arr).item()
            ],
            'min': [
                np.min(arr, axis=0).tolist(),
                np.min(arr, axis=1).tolist(),
                np.min(arr).item()
            ],
            'sum': [
                np.sum(arr, axis=0).tolist(),
                np.sum(arr, axis=1).tolist(),
                np.sum(arr).item()
            ]
        }

        # Confere estrutura
        for key in expected:
            self.assertIn(key, actual, f"Missing key: {key}")
            self.assertEqual(len(actual[key]), 3, f"Wrong length for {key}")

        # Compara colunas, linhas e total
        for key in expected:
            np.testing.assert_almost_equal(actual[key][0], expected[key][0], err_msg=f"{key} colunas")
            np.testing.assert_almost_equal(actual[key][1], expected[key][1], err_msg=f"{key} linhas")
            self.assertAlmostEqual(actual[key][2], expected[key][2], msg=f"{key} total")
