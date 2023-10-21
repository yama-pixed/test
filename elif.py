print("Please enter your age: ")
age=int(input())
print("Please enter yor education level: Example 1-16")
education=int(input())

if age < 18:
    print("Sorry You are not eligible to apply because you are under 18 years old.")
elif education<12:
    print("Sorry You are not eligible to apply due to education restriction.")
else:
    print("You can apply!")




