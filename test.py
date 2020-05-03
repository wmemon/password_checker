import unittest
import password_check

class MyTestCase(unittest.TestCase):
    def test_get_result_less_char(self):
        result = password_check.get_result("06C7")
        self.assertEqual(result, f"[!]Please check the API and the parameter given.")

    def test_get_result_int(self):
        result = password_check.get_result(1234)
        self.assertEqual(result, f"[!]Please check the API and the parameter given.")

    def test_get_result_bool(self):
        result = password_check.get_result(True)
        self.assertEqual(result, f"[!]Please check the API and the parameter given.")

    def test_get_result_float(self):
        result = password_check.get_result(25.157)
        self.assertEqual(result, f"[!]Please check the API and the parameter given.")

    def test_get_result_str_float(self):
        result = password_check.get_result("CR4.5")
        self.assertEqual(result, f"[!]Please check the API and the parameter given.")

if __name__ == '__main__':
    unittest.main()
