import psutil
import tkinter as tk

class MonitoringApp:
    def __init__(self, root):
        self.root = root
        self.root.title('monitoScript App')

        self.label = tk.Label(root, text="")
        self.label.pack()

        self.update_label()

    def update_label(self):
        cpu_usage = psutil.cpu_percent()
        ram_usage = psutil.virtual_memory().percent
        ram_available = psutil.virtual_memory().available * 100 / psutil.virtual_memory().total

        text = f"CPU Usage: {cpu_usage}%\nRAM Usage: {ram_usage}%\nRAM Available: {ram_available}%"
        self.label.config(text=text)

        self.root.after(100, self.update_label)

class MonitoringManager:
    def __init__(self):
        self.app = None

    def run(self):
        self.app = tk.Tk()
        MonitoringApp(self.app)
        self.app.mainloop()

if __name__ == "__main__":
    manager = MonitoringManager()
    manager.run()
