def apply_discount(price, discount):
    # Check if price is a number and NOT a boolean
    if not isinstance(price, (int, float)) or isinstance(price, bool):
        return "The price should be a number"
    
    # Check if discount is a number and NOT a boolean
    if not isinstance(discount, (int, float)) or isinstance(discount, bool):
        return "The discount should be a number"
    
    # Validate price value
    if price <= 0:
        return "The price should be greater than 0"
    
    # Validate discount range
    if discount < 0 or discount > 100:
        return "The discount should be between 0 and 100"
    
    # Calculate final price
    final_price = price * (1 - discount / 100)
    return final_price
