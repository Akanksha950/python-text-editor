import tkinter as tk
from tkinter import filedialog,messagebox
# main window code
root=tk.Tk()
root.title("Text Editor")
root.geometry("800x600")
# for creating text area
text=tk.Text(
     root,
     wrap=tk.WORD,
     font=("Helvetica",12)
)
text.pack(expand=True,fill=tk.BOTH)

# file function-create new file
def new_file():
    text.delete(1.0,tk.END)

# to open new file
def open_file():
    file_path=filedialog.askopenfilename(
        defaultextension=".txt",
        filetypes=[("Text Files","*.txt")]
    )

    if file_path:
        with open(file_path,"r") as file:
            text.delete(1.0,tk.END)
            text.insert(tk.END,file.read())

# to save file
def save_file():
    file_path=filedialog.asksaveasfilename(
        defaultextension=".txt",
        filetypes=[("Text Files","*.txt")]
    )

    if file_path:
        with open(file_path,"w") as file:
            file.write(text.get(1.0,tk.END))

    messagebox.showinfo("Info","File saved successfully!")      

# menu bar
menu=tk.Menu(root)
root.config(menu=menu)
file_menu=tk.Menu(menu)

menu.add_cascade(label="File",menu=file_menu)

# new,open file,save,exit
file_menu.add_command(label="New",command=new_file)
file_menu.add_command(label="Open",command=open_file)
file_menu.add_command(label="Save",command=save_file)
file_menu.add_separator()
file_menu.add_command(label="Exit",command=root.quit)
# start and keep window open
root.mainloop()