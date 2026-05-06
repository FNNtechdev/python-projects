class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = []

    def deposit(self, amount, description=""):
        """Add funds to the ledger."""
        self.ledger.append({"amount": amount, "description": description})

    def withdraw(self, amount, description=""):
        """Subtract funds if available. Returns True if successful."""
        if self.check_funds(amount):
            self.ledger.append({"amount": -amount, "description": description})
            return True
        return False

    def get_balance(self):
        """Returns the current total in the ledger."""
        return sum(item["amount"] for item in self.ledger)

    def transfer(self, amount, category):
        """Transfers money between categories using check_funds."""
        if self.check_funds(amount):
            self.withdraw(amount, f"Transfer to {category.name}")
            category.deposit(amount, f"Transfer from {self.name}")
            return True
        return False

    def check_funds(self, amount):
        """Returns False if amount is greater than balance, True otherwise."""
        return amount <= self.get_balance()

    def __str__(self):
        """Formats the category into a 30-character wide receipt."""
        title = f"{self.name:*^30}\n"
        items = ""
        for entry in self.ledger:
            # Slice description to 23 chars, format amount to 7 chars
            desc = entry["description"][:23].ljust(23)
            amt = f"{entry['amount']:>7.2f}"
            items += f"{desc}{amt}\n"
        
        total = f"Total: {self.get_balance():.2f}"
        return title + items + total


def create_spend_chart(categories):
    """Generates a bar chart showing percentage spent per category."""
    # 1. Calculate total withdrawals per category
    spendings = []
    for cat in categories:
        # Sum only the negative values (withdrawals)
        spent = sum(abs(item["amount"]) for item in cat.ledger if item["amount"] < 0)
        spendings.append(spent)
    
    total_spent = sum(spendings)
    
    # 2. Calculate percentages rounded down to nearest 10
    # Use max(1, total_spent) to avoid division by zero errors
    percentages = [((s / total_spent) * 100) // 10 * 10 if total_spent > 0 else 0 for s in spendings]

    # 3. Build the graph (Y-axis and 'o' bars)
    chart = "Percentage spent by category\n"
    for i in range(100, -1, -10):
        chart += str(i).rjust(3) + "| "
        for p in percentages:
            chart += "o  " if p >= i else "   "
        chart += "\n"
    
    # 4. Add the horizontal separator line
    chart += "    " + "-" * (len(categories) * 3 + 1) + "\n"

    # 5. Build the vertical category names
    max_len = max(len(cat.name) for cat in categories)
    names = [cat.name.ljust(max_len) for cat in categories]
    
    for i in range(max_len):
        chart += "     "
        for name in names:
            chart += name[i] + "  "
        if i < max_len - 1:
            chart += "\n"
            
    return chart
