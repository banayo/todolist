import tkinter as tk
from tkinter import messagebox, simpledialog

class TodoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List")
        self.root.geometry("400x500")

        self.tasks = []

        # กล่องป้อนงาน
        self.entry = tk.Entry(root, width=30)
        self.entry.pack(pady=10)

        # ปุ่มเพิ่มงาน
        self.add_button = tk.Button(root, text="➕ เพิ่มงาน", command=self.add_task)
        self.add_button.pack()

        # รายการงาน
        self.listbox = tk.Listbox(root, width=40, height=15)
        self.listbox.pack(pady=20)

        # ปุ่มลบ
        self.remove_button = tk.Button(root, text="🗑️ ลบงานที่เลือก", command=self.remove_task)
        self.remove_button.pack(pady=5)

        # ปุ่มบันทึกไฟล์
        self.save_button = tk.Button(root, text="💾 บันทึกลงไฟล์", command=self.save_tasks)
        self.save_button.pack(pady=5)

        # โหลดข้อมูลเดิม (ถ้ามี)
        self.load_tasks()

    def add_task(self):
        task = self.entry.get()
        if task:
            self.tasks.append(task)
            self.listbox.insert(tk.END, task)
            self.entry.delete(0, tk.END)
        else:
            messagebox.showwarning("คำเตือน", "กรุณาป้อนงานก่อนเพิ่ม")

    def remove_task(self):
        selected = self.listbox.curselection()
        if selected:
            index = selected[0]
            self.listbox.delete(index)
            del self.tasks[index]
        else:
            messagebox.showwarning("คำเตือน", "กรุณาเลือกงานก่อนลบ")

    def save_tasks(self):
        with open("tasks.txt", "w", encoding="utf-8") as file:
            for task in self.tasks:
                file.write(task + "\n")
        messagebox.showinfo("สำเร็จ", "บันทึกงานเรียบร้อยแล้ว")

    def load_tasks(self):
        try:
            with open("tasks.txt", "r", encoding="utf-8") as file:
                for line in file:
                    task = line.strip()
                    if task:
                        self.tasks.append(task)
                        self.listbox.insert(tk.END, task)
        except FileNotFoundError:
            pass

# เรียกใช้งานแอป
if __name__ == "__main__":
    root = tk.Tk()
    app = TodoApp(root)
    root.mainloop()
