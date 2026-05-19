import tkinter as tk
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
tk.Label(frame_enter, text="Enter the b:", font=("Times New Roman", 15), bg="#FFFFFF").grid(row=2, column=0, padx=5, pady=5)
entry_c = tk.Entry(frame_enter, width=8, font=("Times New Roman", 15), justify="center")
entry_c.grid(row=2, column=1, padx=5, pady=5)
#Creating the button
button = tk.Button(root, font = ("Times New Roman", 15), text = "SOLVING EQUATION")
button.pack(pady = 10, padx = 10)
#Solving the equation
label_result = tk.LabelFrame(root, text=" Discussion & Result ", font=("Times New Roman", 20, "italic"), bg="#F5F5F5", padx=10, pady=10)
label_result.pack(pady=10, fill="both", expand=True, padx=20)

label_show = tk.Label(label_result, text="Please enter variables and click the button.", font=("Times New Roman", 15), bg="#F5F5F5", fg="#808080")
label_show.pack(pady=20)

root.mainloop()