import importlib.util
from pathlib import Path
import subprocess
import sys
import unittest

SCRIPT = Path(__file__).resolve().parent / 'mi-calculadora-python.py'
spec = importlib.util.spec_from_file_location("exercise", SCRIPT)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)


class ExerciseTests(unittest.TestCase):

    def test_operations(self):
        self.assertEqual(module.calcular(6, 3), {"Suma":9,"Resta":3,"Multiplicación":18,"División":2})
    def test_zero_division(self):
        self.assertIsNone(module.calcular(1,0)["División"])
    def test_nonfinite(self):
        for value in (float("nan"),float("inf"),-float("inf")):
            with self.assertRaises(ValueError): module.calcular(value,1)

    def test_invalid_cli(self):
        result = subprocess.run([sys.executable, "-X", "utf8", str(SCRIPT)], input="invalid\n", text=True, capture_output=True, encoding="utf8", timeout=5)
        self.assertEqual(result.returncode, 1)
        self.assertIn("Entrada inválida", result.stdout)
        self.assertNotIn("Traceback", result.stderr)

    def test_valid_cli(self):
        result = subprocess.run([sys.executable, "-X", "utf8", str(SCRIPT)], input='2\n3\n', text=True, capture_output=True, encoding="utf8", timeout=5)
        self.assertEqual(result.returncode, 0)
        self.assertIn('Suma: 5.0', result.stdout)


if __name__ == "__main__":
    unittest.main()
