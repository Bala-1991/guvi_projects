import tkinter as tk

# Initialize the root window
root = tk.Tk()
root.title("Stopwatch")

# Global variables to track the time
hours = 0
minutes = 0
seconds = 0
running = False

# Function to update the time
def update_time():
    global hours, minutes, seconds
    if running:
        # Increment the time manually
        seconds += 1
        if seconds == 60:
            seconds = 0
            minutes += 1
        if minutes == 60:
            minutes = 0
            hours += 1

        # Update the time on the label
        time_string = f"{hours:02}:{minutes:02}:{seconds:02}"
        time_label.config(text=time_string)
        
        # Call the function again after 1000 milliseconds (1 second)
        root.after(1000, update_time)

# Function to start the stopwatch
def start_stopwatch():
    global running
    if not running:
        running = True
        update_time()

# Function to stop the stopwatch
def stop_stopwatch():
    global running
    running = False

# Function to reset the stopwatch
def reset_stopwatch():
    global hours, minutes, seconds, running
    running = False
    hours, minutes, seconds = 0, 0, 0
    time_label.config(text="00:00:00")

# Label to display the time
time_label = tk.Label(root, text="00:00:00", font=("Arial", 50))
time_label.pack()

# Buttons to start, stop, and reset the stopwatch
start_button = tk.Button(root, text="Start", command=start_stopwatch, font=("Arial", 20))
start_button.pack(side=tk.LEFT, padx=20)

stop_button = tk.Button(root, text="Stop", command=stop_stopwatch, font=("Arial", 20))
stop_button.pack(side=tk.LEFT, padx=20)

reset_button = tk.Button(root, text="Reset", command=reset_stopwatch, font=("Arial", 20))
reset_button.pack(side=tk.LEFT, padx=20)

# Start the Tkinter event loop
root.mainloop()

