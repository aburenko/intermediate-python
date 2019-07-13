# show how basic to create a context manager
# the decorator pattern was used here
# for this pattern there is a lib so look in ctx-lib.py

from sqlite3 import connect

# The code:
#
# with ctx() as x:
#   pass
#
# does actually this:
#
# x = ctx().__enter__
# try:
#   pass
# finally:
#   x.__exit__()


class ContextManager:
    def __init__(self, gen):
        self.gen = gen

    def __call__(self, *args, **kwargs):
        self.args, self.kwargs = args, kwargs
        return self

    def __enter__(self):
        self.gen_inst = self.gen(*self.args, **self.kwargs)
        next(self.gen_inst)

    def __exit__(self, *args):
        next(self.gen_inst, None)


def temp_table(cur):
    print('__enter__')
    cur.execute('create table points(x int, y int)')
    yield
    print('__exit__')
    cur.execute('drop table points')


temp_table = ContextManager(temp_table)


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

# eof


