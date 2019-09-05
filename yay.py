import argparse as arg

def range_print(max_val):
    for i in range(max_val):
        print(i+1)

if __name__ == "__main__":
    parser = arg.ArgumentParser(description='Print')
    parser.add_argument('-m', '--max', type=int, help='Max limit to print', default=100)
    # parser.add_argument('--sum', dest='accumulate', action='store_const',
    #                     const=sum, default=max,
    #                     help='sum the integers (default: find the max)')

    args = parser.parse_args()
    range_print(args.max)
    range_print(10)

print('HELLO MARK!')