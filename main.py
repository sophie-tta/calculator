def calc():
  a = input("Enter a number: ")
  try:
    a = int(a)
  except ValueError:
    print("Incorrect value. Resarting Calculator...")
    calc()
    run()
  b = input("Enter another number: ")
  try:
    b = int(b)
  except ValueError:
    print("Incorrect value.Resarting Calculator...")
    calc()
    run()
  print("To Add these numbers together, type A")
  print("To Subtract your first number from the second, type B")
  print("To Multiply these numbers together, type C")
  print("To Divide the first number by the second, type D")
  print("To times a to the power of b, type E")
  value = input("Type your letter (in capitals) here: ")
  if value == "A":
    print(a + b)
  elif value == "B":
    print(b - a)
  elif value == "C":
    print(a * b)
  elif value == "D":
    print(a/b)
  elif value == "E":
    print(a**b)
  else: 
    print("Incorrect value")

def run():
  runagain = input("Run again? (Y/N): ")
  if runagain == "Y":
    calc()
    run()
  elif runagain == "N":
    print("Thank you for using Chelsea's Calculator. Have a good day.")
  else:
    print("Incorrect Value.")
    run()
calc()
run()