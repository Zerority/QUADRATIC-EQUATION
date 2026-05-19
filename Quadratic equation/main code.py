#Solve equation
#Equation form : ax**2 + bx + c = 0
import math
a = float(input())
b = float(input())
c = float(input())
delta = b**2 - 4*a*c
if a == 0:
    if b == 0:
        if c == 0:
            print("Infinite Solution")
        else:
            print("No Solution")
    else:
        solution = -c/b
        r_solution = round(solution,2)
        print("x =", r_solution)
else:
    if delta == 0:
        solution2 = -b/(2*a)
        r_solution2 = round(solution2,2)
        print("x =", r_solution2)
    elif delta < 0:
        print("No slution")
    else:
        sol1 = (-b + math.sqrt(delta))/(2*a)
        sol2 = (-b - math.sqrt(delta))/(2*a)
        r_sol1 = round(sol1,2)
        r_sol2 = round(sol2,2)
        print("=============TWO SOLUTION POSSIBLE============")
        print("x1 = ", r_sol1)
        print("x2 = ", r_sol2) 
 
            