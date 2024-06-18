import tkinter as tk
from tkinter import messagebox

def FCFS(arr, head):
    totalDistance = 0
    for cur_track in arr:
        totalDistance += abs(head - cur_track)
        head = cur_track
    return totalDistance

def SSTF(arr, head):
    totalDistance = 0
    visited = [False] * len(arr)
    for _ in range(len(arr)):
        min_distance = float('inf')
        min_index = -1
        for i in range(len(arr)):
            if not visited[i] and abs(head - arr[i]) < min_distance:
                min_distance = abs(head - arr[i])
                min_index = i
        visited[min_index] = True
        totalDistance += min_distance
        head = arr[min_index]
    return totalDistance

def SCAN(arr, head, disk_size):
    totalDistance = 0
    left = [0]
    right = [disk_size - 1]
    for req in arr:
        if req < head:
            left.append(req)
        else:
            right.append(req)
    left.sort()
    right.sort()
    for track in right:
        totalDistance += abs(head - track)
        head = track
    for track in reversed(left):
        totalDistance += abs(head - track)
        head = track
    return totalDistance

def CSCAN(arr, head, disk_size):
    totalDistance = 0
    left = [0]
    right = [disk_size - 1]
    for req in arr:
        if req < head:
            left.append(req)
        else:
            right.append(req)
    left.sort()
    right.sort()
    for track in right:
        totalDistance += abs(head - track)
        head = track
    head = 0
    for track in left:
        totalDistance += abs(head - track)
        head = track
    return totalDistance

def get_input():
    global arr, head, disk_size
    try:
        n = int(entry_n.get())
        arr = list(map(int, entry_arr.get().split()))
        head = int(entry_head.get())
        disk_size = int(entry_disk_size.get())
        if len(arr) != n:
            raise ValueError
        return True
    except ValueError:
        messagebox.showerror("Input Error", "Invalid input. Please enter valid numbers.")
        return False

def calculate():
    if get_input():
        choice = var.get()
        if choice == 1:
            result = FCFS(arr, head)
        elif choice == 2:
            result = SSTF(arr, head)
        elif choice == 3:
            result = SCAN(arr, head, disk_size)
        elif choice == 4:
            result = CSCAN(arr, head, disk_size)
        else:
            messagebox.showerror("Selection Error", "Please select an algorithm.")
            return
        result_label.config(text=f"Total distance: {result}")

app = tk.Tk()
app.title("Disk Scheduling Algorithms")

header_font = ('Arial', 14, 'bold')
label_font = ('Arial', 14)
entry_font = ('Arial', 14)
result_font = ('Arial', 16, 'bold')

# Adding the main heading
tk.Label(app, text="HDD Scheduling", font=('Arial', 20, 'bold')).grid(row=0, column=0, columnspan=2, pady=20)

tk.Label(app, text="Enter the size of the request array:", font=header_font).grid(row=1, column=0, padx=10, pady=10, sticky='e')
entry_n = tk.Entry(app, font=entry_font)
entry_n.grid(row=1, column=1, padx=10, pady=10)

tk.Label(app, text="Enter the request array:", font=header_font).grid(row=2, column=0, padx=10, pady=10, sticky='e')
entry_arr = tk.Entry(app, font=entry_font)
entry_arr.grid(row=2, column=1, padx=10, pady=10)

tk.Label(app, text="Enter the initial head position:", font=header_font).grid(row=3, column=0, padx=10, pady=10, sticky='e')
entry_head = tk.Entry(app, font=entry_font)
entry_head.grid(row=3, column=1, padx=10, pady=10)

tk.Label(app, text="Enter the disk size:", font=header_font).grid(row=4, column=0, padx=10, pady=10, sticky='e')
entry_disk_size = tk.Entry(app, font=entry_font)
entry_disk_size.grid(row=4, column=1, padx=10, pady=10)

tk.Label(app, text="Choose an algorithm:", font=header_font).grid(row=5, column=0, padx=10, pady=10, sticky='e')
var = tk.IntVar()
tk.Radiobutton(app, text="FCFS", variable=var, value=1, font=label_font).grid(row=6, column=0, sticky='w', padx=10, pady=5)
tk.Radiobutton(app, text="SSTF", variable=var, value=2, font=label_font).grid(row=6, column=1, sticky='w', padx=10, pady=5)
tk.Radiobutton(app, text="SCAN", variable=var, value=3, font=label_font).grid(row=7, column=0, sticky='w', padx=10, pady=5)
tk.Radiobutton(app, text="C-SCAN", variable=var, value=4, font=label_font).grid(row=7, column=1, sticky='w', padx=10, pady=5)

tk.Button(app, text="Calculate", command=calculate, font=label_font).grid(row=8, column=0, columnspan=2, padx=10, pady=20)

result_label = tk.Label(app, text="Total distance: ", font=result_font)
result_label.grid(row=9, column=0, columnspan=2, padx=10, pady=10)

app.mainloop()
