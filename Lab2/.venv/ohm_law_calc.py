def calculate_resistance(voltage, current):
    if current != 0:
        resistance = voltage / current
        return resistance
    else:  # current = 0
        return "Invalid input: current cannot be zero"

result1 = calculate_resistance(9, 0.3)
print(result1)

result2 = calculate_resistance(12, 1.5)
print(result2)

result3 = calculate_resistance(5, 0)
print(result3)