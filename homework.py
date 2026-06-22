try:
    age = int(input("Enter your age: "))

    if age < 0:
        raise ValueError("Age cannot be negative or alphabet")

    print("Valid age")

except ValueError as e:
    print("Error:", e)

finally:
    print("Program finished")
