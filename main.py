import argparse
import sys
from src import Bartender


def _arg_minimum(val):
    """
    Validate the minimum parameter; only values above 0 are allowed
    """
    val = int(val)
    if val <= 0:
        raise argparse.ArgumentTypeError("Value has to be greater than 0")
    return val


def parse_args(args):
    """
    Parse the command line arguments
    
    Returns:
        dict: Command line arguments
    """
    parser = argparse.ArgumentParser(
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('--num-bottom-glasses',
                        '-g',
                        required=True,
                        type=_arg_minimum,
                        help='Number of glasses on the bottom',
                        action='store')
    parser.add_argument('--glass-capacity',
                        '-c',
                        default=250,
                        type=_arg_minimum,
                        help='Milliliter capacity of each glass',
                        action='store')
    parser.add_argument('--pour',
                        '-p',
                        type=_arg_minimum,
                        required=True,
                        help='Milliliter to pour',
                        action='store')

    return vars(parser.parse_args(args))


def _main():
    args = parse_args(sys.argv[1:])

    bartender = Bartender(args['num_bottom_glasses'], args['glass_capacity'])
    bartender.place_order(args['pour'])
    bartender.display_order()


if __name__ == "__main__":
    _main()
