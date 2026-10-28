class ExpenseTracker:
    def __init__(self, monthly_budget: float):
        self.monthly_budget = monthly_budget
        self.expenses = []

    def add_expense(self, name: str, amount: float, category: str):
        if amount < 0:
            raise ValueError("Expense amount cannot be negative.")
        self.expenses.append({
            "name": name,
            "amount": round(amount, 2),
            "category": category.lower()
        })

    def get_total_spent(self) -> float:
        return round(sum(item["amount"] for item in self.expenses), 2)

    def get_remaining_budget(self) -> float:
        return round(self.monthly_budget - self.get_total_spent(), 2)

    def get_expenses_by_category(self, category: str) -> float:
        target = category.lower()
        total = sum(
            item["amount"] for item in self.expenses 
            if item["category"] == target
        )
        return round(total, 2)

    def apply_category_discount(self, category: str, discount_percent: float):
        """
        Applies a percentage discount (0-100) to all expenses in a given category.
        """
        if not (0 <= discount_percent <= 100):
            raise ValueError("Discount percentage must be between 0 and 100.")
        
        target = category.lower()
        for item in self.expenses:
            if item["category"] == target:
                # BUG: Calculates the discount amount and sets it as the new price,
                # instead of subtracting the discount amount from the original price.
                discount_multiplier = discount_percent / 100.0
                item["amount"] = round(item["amount"] * discount_multiplier, 2)