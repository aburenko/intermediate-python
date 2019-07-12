import argparse


def main():
    # create parser
    parser = argparse.ArgumentParser()
    # set parameters
    parser.add_argument("--x", type=float, default=0.0, help="first argument")
    parser.add_argument("--y", type=float, default=0.0, help="second argument")
    parser.add_argument("--op", type=str, default="add", help="operation between arguments")
    # parse and pass on function
    args = parser.parse_args()
    print(calc(args))


def calc(args):
    operation = args.op
    x = args.x
    y = args.y
    if operation == 'add':
        return x + y
    elif operation == 'sub':
        return x - y
    elif operation == 'mul':
        return x * y
    elif operation == 'div':
        return x / y


if __name__ == '__main__':
    main()
