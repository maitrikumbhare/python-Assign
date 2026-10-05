#(if)
"""age=20
if age >= 18:
    print("you are eligible to vote")"""
     
#(if-else)
"""age=16
if age >= 18:
    print("Eligible to vote")
else:
    print("Not eligible to vote")"""

#(if-elif-else)
"""marks=75
if marks>=90:
    print("Grade A+")

elif marks>=75:
    print("Grade A")

elif marks>=60:
    print("Grade B")

elif marks>=50:
    print("Grade C")

else:
    print("Fail")"""

#Nested (if)
"""age=20
has_id=True
if age>=18:
    if has_id:
       print("Entry allowed")
    else:
        print("ID required")
else:
    print("Entry not allowed")"""

#User se ek number input lo. Agar number positive hai to "Positive Number" print karo.
num=int(input("Enter number:"))
if num > 7:
    print("positive number")

else:
    print("negative number")

#User se ek number input lo aur check karo ki number Even hai ya Odd.