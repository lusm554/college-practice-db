from db import conn

def data():
    product = [
        ('Морковь', 18.00, 45),
    ]

    provider = [
        ('ТверьПлодОвощ', 5376576676, 'Магнит', 301002760023, 20),
    ]

    batch = [
        ('10.08.2010', 300, 1, 1),
    ]

    return {
        'provider': provider,
        'product': product,
        'batch': batch,
    }

def provider_q():
    return 'insert into provider (name, INN, bank, checking_account, due_date) \
            values (%s, %s, %s, %s, %s)'

def product_q():
    return 'insert into product (name, price, shelf_life) \
            values (%s, %s, %s)'

def batch_q():
    return 'insert into batch (date, count, product_id, provider_id) \
            values (%s, %s, %s, %s)'

def main():
    d = data()
    try:
        cur = conn.cursor()
        for k, v in d.items():
            # v[0]
            if k == 'provider':
                cur.execute(provider_q(), v[0])
            if k == 'product':
                cur.execute(product_q(), v[0])
            if k == 'batch':
                cur.execute(batch_q(), v[0])
        conn.commit()
    except Exception as e:
        print(e)

if __name__ == "__main__":
    main()
