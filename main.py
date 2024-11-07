import tkinter as tk

# Create the main window

root = tk.Tk()
root.title("Tkinter Geometry Managers Example")
root.geometry("700x600")

# Frame 1 using pack()
frame1 = tk. Frame(root, bg='lightblue')
frame1.pack(side=tk.TOP, fill=tk.BOTH, expand=True, padx=10, pady=10)

# Adding buttons to Frame 1 with different padding

button1 = tk.Button(frame1, text='Pack Button 1')
button2 = tk.Button(frame1, text='Pack Button 2')
button3 = tk.Button(frame1, text='Pack Button 3')
button4 = tk.Button(frame1, text='Pack Button 4')
button1.pack(side=tk.LEFT, padx=10, pady=10)
button2.pack(side=tk.RIGHT, padx=10, pady=10)
button3.pack(side=tk.TOP, padx=10, pady=10)
button4.pack(side=tk.BOTTOM, padx=10, pady=10)

# Frame 2 using grid()

frame2 = tk.Frame(root, bg='lightgreen')
frame2.pack(side=tk.TOP, fill=tk.BOTH, expand=True, padx=10, pady=10)

# Adding buttons to Frame 2 with different grid positions

button5 = tk.Button(frame2, text='Grid Button 1')
button6 = tk.Button(frame2, text='Grid Button 2')
button7 = tk.Button(frame2, text='Grid Button 3')
button8 = tk.Button(frame2, text='Grid Button 4')
button5.grid(row=0, column=0, padx=5, pady=5)
button6.grid(row=0, column=1, padx=5, pady=5)
button7.grid(row=1, column=0, padx=5, pady=5)
button8.grid(row=1, column=1, padx=5, pady=5)
frame3 = tk.Frame (root, bg='lightcoral')
frame3.pack(side=tk.TOP, fill=tk.BOTH, expand=True, padx=10, pady=10)

# Adding buttons to Frame 3 with different x, y positions

button9 = tk.Button(frame3, text='Place Button 1')
button10 = tk.Button(frame3, text='Place Button 2')
button11 = tk.Button(frame3, text='Place Button 3')
button12 = tk.Button(frame3, text='Place Button 4')
button9.place(x=10, y=10)
button10.place(x=200, y=10)
button11.place(x=10, y=50)
button12.place(x=200, y=50)

# Start the main Loop

root.mainloop()