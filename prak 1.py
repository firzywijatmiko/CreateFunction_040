def convert_temperature(value, unit):
  """Converts temperature:

  - 'C' converts Celsius to Fahrenheit
  - 'F' converts Fahrenheit to Celsius
  """
  unit = unit.upper()
  if unit == 'C':
    return (value * 9 / 5) + 32
  elif unit == 'F':
    return (value - 32) * 5 / 9
  else:
    raise ValueError("Invalid unit. Please use 'C' or 'F'.")


print(convert_temperature(25, 'C')) 
print(convert_temperature(77, 'F')) 