# Formatting CLI
Learning using the **argparse** bibliothek for formating console line input.
Give user help and construct the default arguments.

create parser  
`parser = argparse.ArgumentParser()`  

add argument  
`parser.add_argument('--x', type=float, default=1.0, help='What is the first number?')`

parse arguments  
`args = parser.parse_args()`

access arguments  
`args.x`