"""Test Module
"""
import unittest


from module.module import Module


class ModuleTest(unittest.TestCase):
    """Module Test

    Args:
        unittest (_type_): _description_
    """
    def test_echo(self) -> None:
        """echo test
        """
        self.assertEqual(Module().echo("test"), "test")


if __name__ == "__main__":
    unittest.main()
