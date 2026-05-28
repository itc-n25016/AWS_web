import unittest
from main import calc_network_address


class TestCalcNetworkAddress(unittest.TestCase):

    def test_class_c(self):
        self.assertEqual(
            calc_network_address("192.168.1.10", "255.255.255.0"),
            "192.168.1.0"
        )

    def test_class_b(self):
        self.assertEqual(
            calc_network_address("172.16.5.4", "255.255.0.0"),
            "172.16.0.0"
        )

    def test_class_a(self):
        self.assertEqual(
            calc_network_address("10.20.30.40", "255.0.0.0"),
            "10.0.0.0"
        )

    def test_small_subnet(self):
        self.assertEqual(
            calc_network_address("192.168.10.77", "255.255.255.192"),
            "192.168.10.64"
        )


if __name__ == "__main__":
    unittest.main()
