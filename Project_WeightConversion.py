Weight = input("Enter your weight: ")
weight_Unit = input("(L)bs or (K)gs: ")
if weight_Unit.upper() == "L":
    UserWeight = float(Weight) * 0.45
    print(f"Your weight in Kgs is {UserWeight}")
elif weight_Unit.upper() == "K":
    UserWeight = float(Weight) / 0.45
    print(f"Your weight in Lbs is {UserWeight}")
else:
    print("Invalid Input")