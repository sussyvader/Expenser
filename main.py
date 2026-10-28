from tracker import ExpenseTracker

def main():
    budget = ExpenseTracker(monthly_budget=1000.00)
    
    budget.add_expense("Groceries", 150.00, "Food")
    budget.add_expense("Internet Bill", 60.00, "Utilities")
    budget.add_expense("Restaurant", 50.00, "Food")
    
    print(f"Total Spent (Before Discount): ${budget.get_total_spent()}")
    print(f"Food Category Total: ${budget.get_expenses_by_category('Food')}")
    
    # Apply a 10% cashback/discount to Food
    print("\nApplying 10% discount to 'Food' category...")
    budget.apply_category_discount("Food", 10.0)
    
    print(f"Food Category Total (After 10% Discount): ${budget.get_expenses_by_category('Food')}")
    print(f"Remaining Budget: ${budget.get_remaining_budget()}")

if __name__ == "__main__":
    main()