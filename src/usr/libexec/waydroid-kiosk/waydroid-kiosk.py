#!/usr/bin/env python3
import tkinter as tk
import subprocess

class App:
    def __init__(self, root):
        self.root = root
        self.root.config(bg="black")
        self.process = None
        self.center_frame = tk.Frame(root, bg="black")
        self.center_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

        self.title_label = tk.Label(
            self.center_frame, text="Waydroid Runner", font=("sans-serif", 32, "bold"),
            bg="black", fg="white"
        )
        self.title_label.pack(pady=5)

        self.run_btn = tk.Button(
            self.center_frame, text="Run", width=10, command=self.start_process,
            bg="black", fg="white", activebackground="white", activeforeground="black"
        )
        self.run_btn.pack(pady=5)

        self.exit_btn = tk.Button(
            self.center_frame, text="Exit", width=10, command=self.stop_and_exit,
            bg="black", fg="white", activebackground="white", activeforeground="black"
        )
        self.exit_btn.pack(pady=5)

        self.status_label = tk.Label(
            self.center_frame, text='If you want to run Waydroid, just click "Run".\n', font=("sans-serif", 10),
            bg="black", fg="white" 
        )
        self.status_label.pack(pady=10)

    def start_process(self):
        self.run_btn.config(state=tk.DISABLED, disabledforeground="gray")
        self.status_label.config(text='Waydroid is probably running.\nPress "Exit" for exit.')
        self.process = subprocess.Popen(["waydroid", "show-full-ui"]) 

    def stop_and_exit(self):
        if self.process and self.process.poll() is None:
            self.process.terminate()
        self.root.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
    subprocess.run(["waydroid", "session", "stop"])
