from db import conn
from beautifultable import BeautifulTable
from tkinter import *

def show_tkinter(lst, name):
    class Table:
        def __init__(self, root):
            for i in range(total_rows):
                for j in range(total_columns):
                    self.e = Entry(root, width=20, fg='blue',
                            font=('Arial',16,'bold'))
                    self.e.grid(row=i, column=j)
                    self.e.insert(END, lst[i][j])

    total_rows = len(lst)
    total_columns = len(lst[0])
    root = Tk()
    root.title(name)
    t = Table(root)
    root.mainloop()

    
def show():
    cur = conn.cursor()
    cur.execute('select * from product')
    product = cur.fetchall()
    p_desc = [desc[0] for desc in cur.description] 
    
    cur.execute('select * from provider')
    provider = cur.fetchall()
    pr_desc = [desc[0] for desc in cur.description] 

    cur.execute('select * from batch')
    batch = cur.fetchall()
    b_desc = [desc[0] for desc in cur.description] 

    d = {
        'product': [product, p_desc],
        'provider': [provider, pr_desc],
        'batch': [batch, b_desc]
    }


    #print([p_desc] + product)
    #show_tkinter([p_desc] + product)
    for k, v in d.items():
        print(f'\n{k.upper()}:')
        show_tkinter([v[1]] + v[0], k)
        '''
        table = BeautifulTable()
        table.columns.header = v[1]
        for i in v[0]:
            table.rows.append(i)
        print(table)
        '''
        print()


if __name__ == "__main__":
    show()

