import tkinter as tk
import sqlite3
from tkinter import ttk

class Main(tk.Frame):
    def __init__(self,root):
        super().__init__(root)
        self.init_main()
        self.db=db
        self.view_records()

    def init_main(self):
        toolbar=tk.Frame(bg='#d7d8e0',bd=2)
        toolbar.pack(side=tk.TOP,fill=tk.X)
        self.add_img=tk.PhotoImage(file='C:\\Users\\ZhSt\\Desktop\\PythonCore\\Project PythonCore377\\add.gif')
        
        btn_open_dialog = tk.Button(toolbar, text='Додати позицію ', command=self.open_dialog, bg='#d7d8e0', bd=0, 
                                    compound=tk.TOP, image=self.add_img)
        btn_open_dialog.pack(side=tk.LEFT)

        # btn =tk.Button(toolbar,text='Додати позицію ', command=self.open_dialog)
        # btn.pack(side=tk.LEFT)

        self.tree=ttk.Treeview(self,columns=('ID','date','description','costs','total'),height=15,show='headings')

        self.tree.column('ID', width=50, anchor=tk.CENTER)
        self.tree.column('date', width=70, anchor=tk.CENTER)
        self.tree.column('description', width=180, anchor=tk.CENTER)
        self.tree.column('costs', width=230, anchor=tk.CENTER)
        self.tree.column('total', width=120, anchor=tk.CENTER)

        self.tree.heading('ID',text='ID')
        self.tree.heading('date',text='Дата')
        self.tree.heading('description',text='Найменування')
        self.tree.heading('costs',text='Прибуток/витрати/заощадження')
        self.tree.heading('total',text='Сума')

        self.tree.pack()

    def records(self,date,description,costs,total):
        self.db.insert_dates(date,description,costs,total)
        self.view_records()

    def view_records(self):
        self.db.c.execute('''SELECT * FROM Personal_finance''')
        [self.tree.delete(i) for i in self.tree.get_children()]
        [self.tree.insert('','end',values=row) for row in self.db.c.fetchall()]

    def open_dialog(self):
        Add_position()
        

class Add_position(tk.Toplevel):
    def __init__(self):
        super().__init__(root)
        self.init_add_position()
        self.view=app

    def init_add_position(self):
        self.title("Додати Прибуток/витрати/заощадження")
        self.geometry('400x220+400+300')
        self.resizable(False,False)

        label_description=tk.Label(self,text="Дата (XX.YY.ZZZZ)")
        label_description.place(x=50,y=20)
        label_description=tk.Label(self,text="Найменування")
        label_description.place(x=50,y=50)
        label_select=tk.Label(self,text="Прибуток/витрати/заощадження:")
        label_select.place(x=7,y=80)
        label_sum=tk.Label(self,text="Сума:")
        label_sum.place(x=50,y=110)
        
        self.entry_date = ttk.Entry(self)
        self.entry_date.place(x=200,y=20)
      
        self.entry_description = ttk.Entry(self)
        self.entry_description.place(x=200,y=50)

        self.entry_money = ttk.Entry(self)
        self.entry_money.place(x=200,y=110)

        self.combobox=ttk.Combobox(self,values=[u'Дохід',u'Витрати',u'Заощадження'])
        self.combobox.current(0)
        self.combobox.place(x=200,y=80)

        btn_cancel= ttk.Button(self,text='Закрити',command=self.destroy)
        btn_cancel.place(x=300,y=170)

        btn_add= ttk.Button(self,text='Додати')
        btn_add.place(x=220,y=170)
        btn_add.bind('<Button-1>',lambda event: self.view.records(self.entry_date.get(),
                                                                  self.entry_description.get(),
                                                                  self.combobox.get(),
                                                                  self.entry_money.get()))
  

class Data_Base:
    def __init__(self):
        self.conn= sqlite3.connect('Personal_finance.db')
        self.c=self.conn.cursor()
        self.c.execute(''' CREATE TABLE IF NOT EXISTS Personal_finance(id integer primary key,date real,description text,costs text, total real)''')
        self.conn.commit()

    def insert_dates(self,date,description,costs,total):
        self.c.execute(''' INSERT INTO Personal_finance(date,description,costs,total) VALUES (?, ?, ?, ?)''',(date,description,costs,total))
        self.conn.commit()
        
if __name__=="__main__":
    root=tk.Tk()
    db=Data_Base()
    app=Main(root)
    app.pack()
    root.title("Personal finance")
    root.geometry("650x450+300+200")
    root.resizable(False,False)
    root.mainloop()
