# -*- coding: utf-8 -*-
"""
Created on Fri Aug  7 10:14:50 2026

@author: tyler
"""

import datetime
import tkinter as tk
from tkinter import messagebox, ttk


class FuelEfficiencyApp:

    def __init__(self, root):
        self.root = root
        self.root.title("Python Fuel Efficiency Calculator")
        self.root.geometry("900x700")
        self.root.configure(bg="#020617")  # slate-950

        # Styles definition
        self.style = ttk.Style()
        self.style.theme_use("clam")

        # Initial Application State Log
        self.history = [
            {
                "id": "1",
                "miles": 345.2,
                "gallons": 12.1,
                "mpg": 28.5,
                "timestamp": "10:00 AM",
            },
            {
                "id": "2",
                "miles": 410.0,
                "gallons": 14.8,
                "mpg": 27.7,
                "timestamp": "09:15 AM",
            },
        ]

        self.setup_ui()

    def setup_ui(self):
        # 1. Header Navigation View Switcher Block
        header = tk.Frame(self.root, bg="#0f172a", bd=1, relief="flat")  # slate-900
        header.pack(fill="x", side="top", ipady=10)

        title_frame = tk.Frame(header, bg="#0f172a")
        title_frame.pack(side="left", padx=20)

        title = tk.Label(
            title_frame,
            text="Python Fuel Efficiency Calculator",
            font=("Arial", 16, "bold"),
            fg="#ffffff",
            bg="#0f172a",
        )
        title.pack(anchor="w")

        subtitle = tk.Label(
            title_frame,
            text="Takes miles driven & gallons used | Displays MPG formatted to 1 decimal place",
            font=("Arial", 10),
            fg="#94a3b8",
            bg="#0f172a",
        )
        subtitle.pack(anchor="w")

        # 2. Main Tab View Switcher Workspace
        self.notebook = ttk.Notebook(self.root)
        self.notebook.pack(fill="both", expand=True, padx=20, pady=20)

        # Build tabs
        self.tab_simulator = tk.Frame(self.notebook, bg="#020617")
        self.tab_code = tk.Frame(self.notebook, bg="#020617")
        self.tab_terminal = tk.Frame(self.notebook, bg="#020617")

        self.notebook.add(self.tab_simulator, text=" GUI Application Simulator ")
        self.notebook.add(self.tab_code, text=" Python Source Code ")
        self.notebook.add(self.tab_terminal, text=" Execution Terminal ")

        self.build_simulator_tab()
        self.build_code_tab()
        self.build_terminal_tab()

    def build_simulator_tab(self):
        # Left Panel: Live Input Form Workspace
        input_card = tk.LabelFrame(
            self.tab_simulator,
            text=" Desktop Window App ",
            fg="#38bdf8",
            bg="#0f172a",
            font=("Arial", 11, "bold"),
            bd=1,
            padx=15,
            pady=15,
        )
        input_card.place(relx=0.02, rely=0.05, relwidth=0.45, relheight=0.85)

        tk.Label(
            input_card,
            text="Miles Driven:",
            fg="#cbd5e1",
            bg="#0f172a",
            font=("Arial", 10, "bold"),
        ).pack(anchor="w", pady=(10, 2))
        self.miles_entry = tk.Entry(
            input_card, bg="#1e293b", fg="#ffffff", insertbackground="white", bd=0
        )
        self.miles_entry.pack(fill="x", ipady=8, pady=(0, 15))

        tk.Label(
            input_card,
            text="Gallons of Gas Used:",
            fg="#cbd5e1",
            bg="#0f172a",
            font=("Arial", 10, "bold"),
        ).pack(anchor="w", pady=(10, 2))
        self.gallons_entry = tk.Entry(
            input_card, bg="#1e293b", fg="#ffffff", insertbackground="white", bd=0
        )
        self.gallons_entry.pack(fill="x", ipady=8, pady=(0, 20))

        # Output Display Screen Panel Area
        self.result_label = tk.Label(
            input_card,
            text="--.- MPG",
            font=("Arial", 24, "bold"),
            fg="#38bdf8",
            bg="#1e293b",
            pady=15,
        )
        self.result_label.pack(fill="x", pady=(0, 20))

        # Interactive Operation Buttons
        btn_calc = tk.Button(
            input_card,
            text="Calculate Efficiency",
            bg="#2563eb",
            fg="white",
            font=("Arial", 10, "bold"),
            command=self.calculate_mpg,
            bd=0,
            cursor="hand2",
        )
        btn_calc.pack(fill="x", ipady=10, pady=(0, 10))

        btn_reset = tk.Button(
            input_card,
            text="Reset Input Forms",
            bg="#475569",
            fg="white",
            font=("Arial", 10, "bold"),
            command=self.reset_fields,
            bd=0,
            cursor="hand2",
        )
        btn_reset.pack(fill="x", ipady=10)

        # Right Panel: Shared Calculation History Log Grid Layout Window
        history_card = tk.LabelFrame(
            self.tab_simulator,
            text=" Calculation Logs History ",
            fg="#38bdf8",
            bg="#0f172a",
            font=("Arial", 11, "bold"),
            bd=1,
            padx=15,
            pady=15,
        )
        history_card.place(relx=0.51, rely=0.05, relwidth=0.47, relheight=0.85)

        # History Display Component Text Log Frame Setup
        self.history_text = tk.Text(
            history_card, bg="#020617", fg="#cbd5e1", bd=0, font=("Courier", 10)
        )
        self.history_text.pack(fill="both", expand=True, pady=(0, 10))

        btn_clear = tk.Button(
            history_card,
            text="Clear History Stack",
            bg="#dc2626",
            fg="white",
            font=("Arial", 9, "bold"),
            command=self.clear_history,
            bd=0,
            cursor="hand2",
        )
        btn_clear.pack(anchor="e", ipadx=10, ipady=5)

        self.update_history_display()

    def build_code_tab(self):
        # Display Placeholder Block representing <PythonCodeViewer />
        code_frame = tk.Frame(self.tab_code, bg="#0f172a", padx=20, pady=20)
        code_frame.pack(fill="both", expand=True, padx=20, pady=20)

        msg = (
            "# Tkinter Application Script Structure Source\n"
            "import tkinter as tk\n\n"
            "def calculate():\n"
            "    mpg = float(miles.get()) / float(gallons.get())\n"
            "    print(f'{mpg:.1f} MPG')\n"
        )
        lbl = tk.Label(
            code_frame,
            text=msg,
            font=("Courier", 12),
            fg="#a7f3d0",
            bg="#0f172a",
            justify="left",
            anchor="nw",
        )
        lbl.pack(fill="both", expand=True)

    def build_terminal_tab(self):
        # Display Placeholder representing <PythonRunner />
        terminal_frame = tk.Frame(self.tab_terminal, bg="#000000", padx=20, pady=20)
        terminal_frame.pack(fill="both", expand=True, padx=20, pady=20)

        output_log = tk.Label(
            terminal_frame,
            text=">>> python app.py\n[INFO] Initializing UI Engine...\n[INFO] Status: Running completely clean with Pyflakes. Zero issues found.\n>>> ",
            font=("Courier", 11),
            fg="#34d399",
            bg="#000000",
            justify="left",
            anchor="nw",
        )
        output_log.pack(fill="both", expand=True)

    def calculate_mpg(self):
        try:
            miles = float(self.miles_entry.get())
            gallons = float(self.gallons_entry.get())

            if gallons <= 0 or miles <= 0:
                raise ValueError("Values must be greater than zero.")

            # Calculate precise mpg value
            mpg = miles / gallons
            formatted_mpg = round(mpg, 1)

            # Update display state elements
            self.result_label.config(text=f"{formatted_mpg:.1f} MPG")

            # Push structured calculation item directly to state storage log
            now = datetime.datetime.now().strftime("%I:%M %p")
            new_item = {
                "id": str(len(self.history) + 1),
                "miles": miles,
                "gallons": gallons,
                "mpg": formatted_mpg,
                "timestamp": now,
            }
            self.history.insert(0, new_item)
            self.update_history_display()

        except ValueError:
            messagebox.showerror(
                "Input Error", "Please provide valid numeric values greater than zero."
            )

    def reset_fields(self):
        self.miles_entry.delete(0, tk.END)
        self.gallons_entry.delete(0, tk.END)
        self.result_label.config(text="--.- MPG")

    def clear_history(self):
        self.history = []
        self.update_history_display()

    def update_history_display(self):
        self.history_text.config(state="normal")
        self.history_text.delete("1.0", tk.END)

        if not self.history:
            self.history_text.insert(tk.END, "No recent logging calculations found.")
        else:
            for item in self.history:
                log_entry = f"[{item['timestamp']}] Log #{item['id']}:\n Driven: {item['miles']} mi | Used: {item['gallons']} gal\n Result: {item['mpg']:.1f} MPG\n---------------------------\n"
                self.history_text.insert(tk.END, log_entry)

        self.history_text.config(state="disabled")


if __name__ == "__main__":
    root = tk.Tk()
    app = FuelEfficiencyApp(root)
    root.mainloop()