from argparse import ArgumentParser
from sys import stdout

def argparser():
    """Returns an argument parser that handles CLI."""
    parser = ArgumentParser(prog="python massage.py", description="kernel-weighted time series density.", epilog="Andy's free (as in beer) software.")

    parser.add_argument("infile", metavar="<filename>", type=file, nargs=1, help="input time-series tsv files.")

    group = parser.add_argument_group("input/output options")
    group.add_argument("--output", "-o", metavar="STR", dest="outfile", type=file, default=stdout, help="file for writing output time-series. default: stdout")
    group.add_argument("--format", "-f", metavar="STR", dest="format", type=str, default="%%Y-%%m-%%d", help="format string for parsing dates. default: \"%%Y-%%m-%%d\"")

    group = parser.add_argument_group("density estimation options")
    group.add_argument("--step", "-s", metavar="N", dest="step", default=1, type=float, help="step size for codomain time-series. default: 1")
    group.add_argument("--kernel", "-k", metavar="STR", dest="kernel", default="gaussian", type=str, choices=["gaussian", "tricubic"], help="kernel function. (\"gaussian\" or \"tricubic\")")
    group.add_argument("--parameter", "-p", metavar="N", dest="parameter", default=15, type=float, help="characteristic dimension of kernel. default: 15")

    # That's all, folks!
    return parser
