import tkinter as tk
from tkinter import messagebox, simpledialog
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import tkinter.font as tkfont
import os
import sys

# Ensure relative import works from any location
CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.join(CURRENT_DIR, "analyzed_data"))

# Import graph functions (return fig, insight)
from bar_chart_total_money_vs_day import plot_total_money_vs_day
from bar_chart_total_sale_quantitiy_vs_day import plot_total_quantity_vs_day
from horizontal_bar_chart_top5 import plot_top5_sweets
from bar_chart_least5 import plot_least5_sweets
from pie_chart_of_selected_weekday_sale_of_sweets import plot_pie_chart_for_weekday
from heat_map_selected_weekdays_and_sweets import plot_heatmap_for_weekdays


class KantiSweetsApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Kanti Sweets Sales Analysis")
        self.root.geometry("1000x700")
        self.root.configure(bg='light pink')

        self.custom_font = ("Algerian", 32, "bold") if "Algerian" in tkfont.families() else ("Arial Black", 28, "bold")

        self.home_screen()

    def clear_window(self):
        for widget in self.root.winfo_children():
            widget.destroy()

    def home_screen(self):
        self.clear_window()

        label = tk.Label(self.root, text="Kanti Sweets Sales Analysis", bg="light pink", fg="black", font=self.custom_font)
        label.pack(pady=100)

        enter_btn = tk.Button(
            self.root, text="Enter", bg="#D36C8E", fg="black",
            font=("Arial", 16, "bold"), width=12, height=2,
            command=self.graph_selection_screen, relief="raised", bd=3
        )
        enter_btn.pack()

    def graph_selection_screen(self):
        self.clear_window()

        label = tk.Label(self.root, text="Select a Graph to View", bg="light pink", fg="black", font=("Arial", 22, "bold"))
        label.pack(pady=30)

        button_frame = tk.Frame(self.root, bg="light pink")
        button_frame.pack(pady=10)

        button_texts = [
            ("Total Revenue vs Day", self.show_total_money),
            ("Total Quantity vs Day", self.show_total_quantity),
            ("Top 5 Selling Sweets", self.show_top5),
            ("Least 5 Selling Sweets", self.show_least5),
            ("Pie Chart (Sweet Sales by Weekday)", self.show_pie_chart),
            ("Heatmap (Selected Days vs Sweets)", self.show_heatmap),
        ]

        for text, command in button_texts:
            btn = tk.Button(
                button_frame,
                text=text,
                width=35,
                height=3,
                bg="#D36C8E",
                fg="black",
                font=("Arial", 14, "bold"),
                relief="raised",
                bd=4,
                command=command
            )
            btn.pack(pady=12)

    def display_graph(self, fig, insight=""):
        self.clear_window()

        fig.set_size_inches(8, 5)
        canvas = FigureCanvasTkAgg(fig, master=self.root)
        canvas.draw()
        canvas_widget = canvas.get_tk_widget()
        canvas_widget.pack(pady=20)

        if insight:
            insight_label = tk.Label(self.root, text=insight, bg="light pink", fg="black",
                                     font=("Arial", 14), wraplength=900, justify="center")
            insight_label.pack(pady=10)

        back_btn = tk.Button(
            self.root, text="Back", bg="#D36C8E", fg="black",
            font=("Arial", 14), command=self.graph_selection_screen,
            relief="raised", bd=3, width=10, height=2
        )
        back_btn.pack(pady=20)

    # ------------ Graph Button Functions ------------

    def show_total_money(self):
        fig, insight = plot_total_money_vs_day()
        self.display_graph(fig, insight)

    def show_total_quantity(self):
        fig, insight = plot_total_quantity_vs_day()
        self.display_graph(fig, insight)

    def show_top5(self):
        fig, insight = plot_top5_sweets()
        self.display_graph(fig, insight)

    def show_least5(self):
        fig, insight = plot_least5_sweets()
        self.display_graph(fig, insight)

    def show_pie_chart(self):
        self.root.update_idletasks()
        self.root.focus_force()

        weekday = simpledialog.askstring("Input", "Enter weekday (e.g., Mon, Tue, Wed, Thur, Fri, Sat, Sun):")
        if weekday:
            result = plot_pie_chart_for_weekday(weekday)
            if isinstance(result, tuple):
                fig, insight = result
            else:
                fig, insight = result, ""

            if fig:
                self.display_graph(fig, insight)
            else:
                messagebox.showerror("Error", f"No data available for '{weekday}'")

    def show_heatmap(self):
        self.root.update_idletasks()
        self.root.focus_force()

        days_input = simpledialog.askstring("Input", "Enter weekdays (comma-separated, e.g., Mon,Fri,Sat):")
        if days_input:
            selected_days = [d.strip() for d in days_input.split(",")]
            result = plot_heatmap_for_weekdays(selected_days)
            if isinstance(result, tuple):
                fig, insight = result
            else:
                fig, insight = result, ""

            if fig:
                self.display_graph(fig, insight)
            else:
                messagebox.showerror("Error", "No data for selected weekdays.")


# ------------- Run the App -------------
if __name__ == "__main__":
    root = tk.Tk()
    app = KantiSweetsApp(root)
    root.mainloop()
