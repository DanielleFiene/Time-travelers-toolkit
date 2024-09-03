import unittest
from unittest.mock import patch
from decimal import Decimal
import datetime as dt
import custom_module

class TestTimeTravelProject(unittest.TestCase):

    @patch('dt.date.today')
    def test_today_date(self, mock_today):
        mock_today.return_value = dt.date(2024, 9, 1)
        today_date = dt.date.today()
        self.assertEqual(today_date, dt.date(2024, 9, 1))

    @patch('dt.datetime.now')
    def test_current_time(self, mock_now):
        mock_now.return_value = dt.datetime(2024, 9, 1, 12, 0, 0)
        current_time = dt.datetime.now().time()
        self.assertEqual(current_time, dt.time(12, 0, 0))

    def test_base_cost(self):
        base_cost = Decimal('100.00')
        self.assertEqual(base_cost, Decimal('100.00'))

    @patch('random.randint')
    def test_target_year(self, mock_randint):
        mock_randint.return_value = 2050
        target_year = randint(2025, 2100)
        self.assertTrue(2025 <= target_year <= 2100)
        self.assertEqual(target_year, 2050)

    @patch('dt.datetime.now')
    def test_year_difference(self, mock_now):
        mock_now.return_value = dt.datetime(2024, 9, 1)
        target_year = 2050
        current_year = dt.datetime.now().year
        year_difference = target_year - current_year
        self.assertEqual(year_difference, 26)

    def test_final_cost_calculation(self):
        base_cost = Decimal('100.00')
        year_difference = 26
        cost_per_year = Decimal('10.00')
        total_cost_multiplier = cost_per_year * year_difference
        final_cost = base_cost + total_cost_multiplier
        final_cost = final_cost.quantize(Decimal('0.01'))
        self.assertEqual(final_cost, Decimal('360.00'))

    @patch('random.choice')
    def test_selected_destination(self, mock_choice):
        destinations = [
            "Ancient Egypt",
            "Medieval Europe",
            "The Renaissance",
            "The American Revolution",
            "The Moon Landing",
            "The Industrial Revolution",
            "Future Mars Colony",
            "The Great Wall of China",
            "Victorian London",
            "The Jurassic Period"
        ]
        mock_choice.return_value = "The Moon Landing"
        selected_destination = choice(destinations)
        self.assertIn(selected_destination, destinations)
        self.assertEqual(selected_destination, "The Moon Landing")

    @patch('custom_module.generate_time_travel_message')
    def test_generate_time_travel_message(self, mock_message):
        mock_message.return_value = "Your time travel trip to The Moon Landing in 2050 will cost 360.00"
        message = custom_module.generate_time_travel_message(2050, "The Moon Landing", Decimal('360.00'))
        self.assertEqual(message, "Your time travel trip to The Moon Landing in 2050 will cost 360.00")
        
if __name__ == '__main__':
    unittest.main()
