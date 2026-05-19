import tkinter as tk
from tkinter import messagebox 
import math

def solving_equation():
    try:
        a = float(entry_a.get())
        b = float(entry_b.get())
        c = float(entry_c.get())
        delta = b**2 - 4*a*c
        if a == 0:
            if b == 0:
                if c == 0:
                    result = "Infinite Solution"
                else:
                    result = "No Solution"
            else:
                solution = -c/b
                r_solution = round(solution,2)
                result = "x =", r_solution
        else:
            if delta == 0:
                solution2 = -b/(2*a)
                r_solution2 = round(solution2,2)
                result = "x =", r_solution2
            elif delta < 0:
                result = "No Solution"
            else:
                sol1 = (-b + math.sqrt(delta))/(2*a)
                sol2 = (-b - math.sqrt(delta))/(2*a)
                r_sol1 = round(sol1,2)
                r_sol2 = round(sol2,2)
                result = f"TWO SOLUTIONS POSSIBLE:\nx1 = {r_sol1}\nx2 = {r_sol2}" 

        label_show.config(text=result, fg="#2E7D32", font=("Times New Roman", 30, "bold"))
    except ValueError:
        # Bẫy lỗi nếu người dùng nhập chữ cái hoặc bỏ trống ô dữ liệu
        messagebox.showerror("Input error", "Please enter the coefficients a, b, and c in numerical form!")

#Tkinter
root = tk.Tk()
root.geometry("1000x700")
root.title("SOFTWARE FOR SOLVING QUADRATIC EQUATIONS")
root.config(bg="#F5F5F5")#Change color

label = tk.Label(root, text = "SOLVING QUADRATIC EQUATION", font = ("Times New Roman", 25), fg = "#0000FF")
label.pack(padx = 100, pady = 50)

sub_title = tk.Label(root, text="Standard form: ax² + bx + c = 0", font=("Times New Roman", 20, "italic"), bg="#FFFFFF", fg="#808080")
sub_title.pack()
#Creating the frame
frame_enter = tk.Frame(root, bg = "#FFFFFF")
frame_enter.pack(pady=20)
#Enter a
tk.Label(frame_enter, text="Enter the a:", font=("Times New Roman", 15), bg="#FFFFFF").grid(row=0, column=0, padx=5, pady=5)
entry_a = tk.Entry(frame_enter, width=8, font=("Times New Roman", 15), justify="center")
entry_a.grid(row=0, column=1, padx=5, pady=5)
#b
tk.Label(frame_enter, text="Enter the b:", font=("Times New Roman", 15), bg="#FFFFFF").grid(row=1, column=0, padx=5, pady=5)
entry_b = tk.Entry(frame_enter, width=8, font=("Times New Roman", 15), justify="center")
entry_b.grid(row=1, column=1, padx=5, pady=5)
#c
tk.Label(frame_enter, text="Enter the c:", font=("Times New Roman", 15), bg="#FFFFFF").grid(row=2, column=0, padx=5, pady=5)
entry_c = tk.Entry(frame_enter, width=8, font=("Times New Roman", 15), justify="center")
entry_c.grid(row=2, column=1, padx=5, pady=5)
#Creating the button
button = tk.Button(root, font = ("Times New Roman", 15), text = "SOLVING EQUATION", command = solving_equation)
button.pack(pady = 10, padx = 10)
#Solving the equation
label_result = tk.LabelFrame(root, text=" Discussion & Result ", font=("Times New Roman", 20, "italic"), bg="#F5F5F5", padx=10, pady=10)
label_result.pack(pady=10, fill="both", expand=True, padx=20)

label_show = tk.Label(label_result, text="Please enter variables and click the button.", font=("Times New Roman", 15), bg="#F5F5F5", fg="#808080")
label_show.pack(pady=20)

root.mainloop()