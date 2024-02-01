import sqlite3
def create_connection(db_name):
    conn = None
    try:
        conn = sqlite3.connect(db_name)
    except sqlite3.Error as e:
        print(e)
    return conn
def create_table(conn, sql):
    try:
        cursor = conn.cursor()
        cursor.execute(sql)
    except sqlite3.Error as e:
        print(e)
def insert_product(conn, product):
    sql = '''INSERT INTO products
    (product_title, price, quantity)    VALUES(?,?,?)
    '''
    try:
        cursor = conn.cursor()
        cursor.execute(sql, product)
        conn.commit()
    except sqlite3.Error as e:
        print(e)
def select_all_products(conn):
    sql = ''' SELECT * FROM products'''
    try:
        cursor = conn.cursor()
        cursor.execute(sql)
        rows_list = cursor.fetchall()
        for row in rows_list:
            print(row)
    except sqlite3.Error as e:
        print(e)

def update_product_quantity(conn, product):
    sql = '''UPDATE products SET quantity = ?    WHERE id = ?'''
    try:
        cursor = conn.cursor()
        cursor.execute(sql, product)
        conn.commit()
    except sqlite3.Error as e:
        print(e)

def update_product_price(conn, product):
    sql = '''
    UPDATE products SET price = ?
    WHERE id = ?'''
    try:
        cursor = conn.cursor()
        cursor.execute(sql, product)
        conn.commit()
    except sqlite3.Error as e:
        print(e)

def delete_product(conn, id):
    sql = ''' DELETE from products WHERE id = ?'''
    try:
        cursor = conn.cursor()
        cursor.execute(sql, (id,))
        conn.commit()
    except sqlite3.Error as e:
        print(e)

def select_products_by_price(conn, price_limit, quantity_limit):
    sql = '''SELECT * FROM products WHERE price <= ? AND quantity >= ?'''
    try:
        cursor = conn.cursor()
        cursor.execute(sql, (price_limit, quantity_limit,))
        rows_list = cursor.fetchall()
        for row in rows_list:
            print(row)
    except sqlite3.Error as e:
        print(e)
def search_by_word(conn, word):
    try:
        sql = '''SELECT * FROM products WHERE product_title LIKE ?'''
        cursor = conn.cursor()
        cursor.execute(sql, ('%'+word+'%',))
        rows = cursor.fetchall()
        for row in rows:
            print(row)
    except sqlite3.Error as e:
        print(e)

sql_to_create_products_table = '''CREATE TABLE products(
    id INTEGER PRIMARY KEY AUTOINCREMENT,    product_title VARCHAR(200) NOT NULL,
    price FLOAT(10, 2) NOT NULL DEFAULT 0.0,    quantity INTEGER NOT NULL DEFAULT 0
)'''
connection = create_connection('hw7.db')
if connection is not None:
    print('Successfully connected to DB!')
    # create_table(connection, sql_to_create_products_table)
    # insert_product(connection,('Хлопья ОРГАНИК геркулес', 40, 80))
    # insert_product(connection,('Мандарин ИК', 180, 100))
    # insert_product(connection,('Чеснок сушеный', 200, 1000))
    # insert_product(connection,('Имбирь корень ', 400, 500))
    # insert_product(connection,('Перец калифорния красный ', 200, 100))
    # insert_product(connection, ('Семя кунжутное белое', 560, 10))
    # insert_product(connection, ('Сыр плавленный HOCHLAND professional сливочный', 340, 15))
    # insert_product(connection,('Йогурт ФРУТТИС cливочный персик', 150, 50))
    # insert_product(connection,('Завтрак готовый ХРУТКА ', 400, 40))
    # insert_product(connection,('Кофе JACOBS MONARCH молотый классический', 440, 1000))
    # insert_product(connection, ('Шпроты ГЛАВПРОДУКТ hansa в масле ', 200, 30))
    # insert_product(connection, ('Творог БЕЛАЯ РЕКА ванильный', 120, 100))
    # insert_product(connection,('Чай черный Tess sunrise 200гр', 176, 100))
    # insert_product(connection, ('Помидор тепличный', 179, 200))
    # insert_product(connection, ('Капуста белокочанная', 31, 100))


    # delete_product(connection, 15)

    # update_product_quantity(connection, (60, 1))
    # update_product_price(connection,(190, 14))

    # select_all_products(connection)
    # select_products_by_price(connection, 100, 5)

    # search_by_word(connection, 'Мандарин')

    connection.close()
