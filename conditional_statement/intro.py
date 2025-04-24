# Conditional Statement:- A conditional statement in Python allows you to execute certain blocks of code based on whether a condition is True or False.
# The basic syntax uses if, elif, and else. 
# 1 => if:- if checks the first condition.
# 2 => else:- else runs if none of the above conditions were true.
# 3 => elif:- elif (short for "else if") checks another condition if the previous ones were false.


# ==================== if condition ==================== #
x = 10
if (x > 0): # or (x > 20) then it will not print anything because the condition is false...
    print("x is greater...")

    
# ==================== if then else condition ==================== #
y = 10
if (y > 20):
    print("y is greater...")
else:
    print("y is lesser...") # the else statement runs only when the if statement will be false.
    

# ===================== elif condition ========================= # 
a = 0
if (a > 20):
    print("a is greater...")
elif (a == 0):  # this statement runs only when multiple of conditions are there.
    print("a equals 0...")
else:
    print("a is lesser...") 
    