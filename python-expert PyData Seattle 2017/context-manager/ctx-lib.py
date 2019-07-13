from contextlib import contextmanager
from sqlite3 import connect


@contextmanager
def temp_table(cur):
    print('__enter__')
    cur.execute('create table points(x int, y int)')
    try:
        yield
    finally:
        print('__exit__')
        cur.execute('drop table points')


with connect('test.db') as conn:
    cur = conn.cursor()
    with temp_table(cur):
        cur.execute('insert into points(x, y) values(1, 1)')
        cur.execute('insert into points(x, y) values(1, 2)')
        cur.execute('insert into points(x, y) values(2, 1)')
        cur.execute('insert into points(x, y) values(0, 0)')

        for row in cur.execute('select x, y from points'):
            print(row)
        for row in cur.execute('select sum(x * y) from points'):
            print(row)
