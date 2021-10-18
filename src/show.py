from db import conn

def show():
    cur = conn.cursor()
    cur.execute('select * from product')
    product = cur.fetchall()
    p_desc = cur.description
    
    cur.execute('select * from provider')
    provider = cur.fetchall()
    pr_desc = cur.description

    cur.execute('select * from batch')
    batch = cur.fetchall()
    b_desc = cur.description

    d = {
        'product': product,
        'provider': provider,
        'batch': batch
    }

    for k, v in d.items():
        print(f'\n{k}\n')
        for i in v:
            print('  ', *i)

if __name__ == "__main__":
    show()
