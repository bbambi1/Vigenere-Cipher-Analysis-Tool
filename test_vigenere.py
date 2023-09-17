import unittest
import vigenere

class TestVigenere(unittest.TestCase):
    def test_encrypt(self):
        self.assertEqual(vigenere.encrypt("HELLO", "KEY"), "RIJVS")
        self.assertEqual(vigenere.encrypt("Hello World", "KEY"), "Rijvs Uyvjn")
        self.assertEqual(vigenere.encrypt("Hello123", "KEY"), "Rijvs123")
        self.assertEqual(vigenere.encrypt("HELLO", "LONGKEY"), "SSYRY")

    def test_decrypt(self):
        self.assertEqual(vigenere.decrypt("RIJVS", "KEY"), "HELLO")
        self.assertEqual(vigenere.decrypt("Rijvs Uyvjn", "KEY"), "Hello World")
        self.assertEqual(vigenere.decrypt("Rijvs123", "KEY"), "Hello123")
        self.assertEqual(vigenere.decrypt("SSYRY", "LONGKEY"), "HELLO")

    def test_kasiski_examination(self):
        text = "BIPULBIPBIWIFWNLFXFAOXYJUIPULANRGWSZRMXUKHNODWZWIYGJF"
        self.assertEqual(24, vigenere.kasiski_examination(text))

    def test_index_of_coincidence(self):
        text = "BIPULBIPBIWIFWNLFXFAOXYJUIPULANRGWSZRMXUKHNODWZWIYGJF"
        expected_ic = 0.04282
        self.assertAlmostEqual(vigenere.index_of_coincidence(text), expected_ic, places=4)

    # Add more tests

if __name__ == '__main__':
    unittest.main()
