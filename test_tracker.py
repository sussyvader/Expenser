import unittest
from tracker import ExpenseTracker

class TestExpenseTracker(unittest.TestCase):
    def setUp(self):
        self.tracker = ExpenseTracker(monthly_budget=500.00)
        self.tracker.add_expense("Coffee", 20.00, "Food")
        self.tracker.add_expense("Lunch", 80.00, "Food")
        self.tracker.add_expense("Bus Pass", 50.00, "Transport")

    def test_total_spent(self):
        self.assertEqual(self.tracker.get_total_spent(), 150.00)

    def test_remaining_budget(self):
        self.assertEqual(self.tracker.get_remaining_budget(), 350.00)

    def test_category_filter_case_insensitive(self):
        self.assertEqual(self.tracker.get_expenses_by_category("FOOD"), 100.00)

    def test_apply_category_discount(self):
        # Applying a 20% discount to $100 worth of Food should leave $80.00
        self.tracker.apply_category_discount("Food", 20.0)
        self.assertEqual(self.tracker.get_expenses_by_category("Food"), 80.00)
        self.assertEqual(self.tracker.get_total_spent(), 130.00)

if __name__ == "__main__":
    unittest.main()