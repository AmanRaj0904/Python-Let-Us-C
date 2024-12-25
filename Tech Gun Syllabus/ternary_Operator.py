age = int(input("Enter your Age\n"))
if age >=18:
    print("Eligible for Voting\n")
else:
    print("Not Eligible for Voting\n")

# With Ternary Operator
print("Yes, Eligible ") if age >= 18 else print("No, Not Eligilble")


#Ternary operator is a shorthand for an if-else statement that allows conditional expressions to be written in a single line. The syntax is:

#<value_if_true> if <condition> else <value_if_false>
