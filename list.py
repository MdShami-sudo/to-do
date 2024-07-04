import tkinter as tk
from tkinter import messagebox

class ToDoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Attractive To-Do List")
        self.root.geometry("400x500")
        
        self.tasks = []
        
        self.title_label = tk.Label(root, text="My To-Do List", font=("Helvetica", 20, "bold"))
        self.title_label.pack(pady=10)
        
        self.frame = tk.Frame(root)
        self.frame.pack(pady=10)
        
        self.task_listbox = tk.Listbox(self.frame, width=40, height=10, bd=0, font=("Helvetica", 12))
        self.task_listbox.pack(side=tk.LEFT, fill=tk.BOTH)
        
        self.scrollbar = tk.Scrollbar(self.frame)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.BOTH)
        
        self.task_listbox.config(yscrollcommand=self.scrollbar.set)
        self.scrollbar.config(command=self.task_listbox.yview)
        
        self.task_entry = tk.Entry(root, width=40, font=("Helvetica", 12))
        self.task_entry.pack(pady=20)
        
        self.button_frame = tk.Frame(root)
        self.button_frame.pack(pady=10)
        
        self.add_task_button = tk.Button(self.button_frame, text="Add Task", command=self.add_task, font=("Helvetica", 12))
        self.add_task_button.pack(side=tk.LEFT, padx=10)
        
        self.delete_task_button = tk.Button(self.button_frame, text="Delete Task", command=self.delete_task, font=("Helvetica", 12))
        self.delete_task_button.pack(side=tk.LEFT, padx=10)
        
        self.clear_task_button = tk.Button(self.button_frame, text="Clear Tasks", command=self.clear_tasks, font=("Helvetica", 12))
        self.clear_task_button.pack(side=tk.LEFT, padx=10)
        
    def add_task(self):
        task = self.task_entry.get()
        if task != "":
            self.tasks.append(task)
            self.update_task_list()
            self.task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "You must enter a task.")
    
    def delete_task(self):
        try:
            selected_task_index = self.task_listbox.curselection()[0]
            self.tasks.pop(selected_task_index)
            self.update_task_list()
        except IndexError:
            messagebox.showwarning("Warning", "You must select a task to delete.")
    
    def clear_tasks(self):
        self.tasks.clear()
        self.update_task_list()
        
    def update_task_list(self):
        self.task_listbox.delete(0, tk.END)
        for task in self.tasks:
            self.task_listbox.insert(tk.END, task)

if __name__ == "__main__":
    root = tk.Tk()
    app = ToDoApp(root)
    root.mainloop()
