def tax(income):
    if income <= 2000:
        return "Isento"
    elif 2000 < income <= 3000:
        value = income - 2000
        tax_value = value - (value - ((value / 100) * 8))
        return f"R$ {tax_value:.2f}"
    elif 3000 < income <= 4500:
        value = income - 3000
        first_tax = 1000 - (1000 - ((1000 / 100) * 8))
        second_tax = value - (value - ((value / 100) * 18))
        tax_value = first_tax + second_tax
        return f"R$ {tax_value:.2f}"
    elif income > 4500:
        value = income - 4500
        third_tax = value - (value - ((value / 100) * 28))
        second_tax = 1500 - (1500 - ((1500 / 100) * 18))
        first_tax = 1000 - (1000 - ((1000 / 100) * 8))
        tax = first_tax + second_tax + third_tax
        return f"R$ {tax:.2f}"


income = float(input())
print(tax(income))
