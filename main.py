import argparse
from func.main_funcs import find_min_subnet

parser = argparse.ArgumentParser(description='filename contains ip address list')
parser.add_argument('-f', action="store", dest="filename", type=str, required=True)
parser.add_argument('-v', action="store", dest="ip_version", default='IPv4', type=str,
                    help='ip protocol version. example: IPv4')

args = parser.parse_args()
filename = args.filename  # type: str
print(find_min_subnet(filename))

