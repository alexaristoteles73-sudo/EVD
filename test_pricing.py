"""Tests for the QuickPrint proposal-based estimate rules."""
import unittest
from decimal import Decimal

from pricing import calculate_total, format_pesos  # type: ignore[import-not-found]  # Local module; verified by unittest.


class PricingTests(unittest.TestCase):
    def test_black_and_white_pages_and_copies(self):
        self.assertEqual(calculate_total("bw-print", 4, 2), Decimal("8"))

    def test_color_print(self):
        self.assertEqual(calculate_total("color-print", 3, 2), Decimal("24"))

    def test_photocopy(self):
        self.assertEqual(calculate_total("photocopy", 5), Decimal("25"))

    def test_lamination_by_item(self):
        self.assertEqual(calculate_total("lamination", 2), Decimal("40"))

    def test_computer_station_by_five_minute_block(self):
        self.assertEqual(calculate_total("computer-station", 30), Decimal("6"))

    def test_unpriced_services_request_quote(self):
        for service in ("scanning", "formatting", "binding"):
            with self.subTest(service=service):
                self.assertIsNone(calculate_total(service, 2))

    def test_non_short_bond_printing_requests_quote(self):
        self.assertIsNone(calculate_total("bw-print", 10, 1, "other-size"))

    def test_invalid_computer_increment_is_rejected(self):
        with self.assertRaisesRegex(ValueError, "5-minute increments"):
            calculate_total("computer-station", 7)

    def test_zero_quantity_is_rejected(self):
        with self.assertRaisesRegex(ValueError, "between 1 and 10,000"):
            calculate_total("bw-print", 0)

    def test_unknown_service_is_rejected(self):
        with self.assertRaisesRegex(ValueError, "choose a listed service"):
            calculate_total("unknown", 1)

    def test_peso_formatting(self):
        self.assertEqual(format_pesos(Decimal("8")), "₱8")
        self.assertEqual(format_pesos(Decimal("6.50")), "₱6.50")


if __name__ == "__main__":
    unittest.main()
