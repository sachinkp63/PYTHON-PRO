#==================Operations===================

# 1 => Arithematic Operations...
# Additions(+)
x = 3 
y = 4
print(x + y)
# Subtraction(-)
print(x - y)
# Multiplication(*)
print(x * y)
# Division(/)
print(x / y)
# Modulus(%)
print(x % y)

# 2 => Comparison(Relations) Operations...
# Equal(==)
print(3==4)
# notequal(!=)
print(3 != 4)
# Greater Than
print(3 > 4)
# Less Than
print(3 < 4)
# Greater Than equal
print(3 >= 4)
# Less Than equal
print(3 <= 4)

# 3 => Logical Operator...
# and - True if both are true
age = 25
has_id = True
if age >= 18 and has_id:
    print("You can enter.")
else:
    print("Access denied")
# or - True if at least one is true
is_admin = False
is_moderator = True
if is_admin or is_moderator:
    print("You have access to he dashboard")
else:
    print("Access denied")
# not - Reverse the boolean value
is_banned = False
if not is_banned:
    print("You are welcome!")
else:
    print("You are banned.")
    
# COMBINED EXAMPLE
username = "Sachin"
is_logged_in = True
is_verified = False
if is_logged_in and (is_verified or username == "Sachin"):
    print("Welcome Sachin")
else:
    print("Access denied")
    
# 4 => Assignment Operators...
# = : Basic assignment
k = 5
print(k)
# += : x+=y -> x = x+y
x=5
y=6
x += y
print(x)
# -= : x-=y -> x = x-y
x -= y
print(x)
# *= : x*=y -> x = x*y
x *= y
print(x)


# 5 => Bitwise Operators...
#

    