#!/usr/bin/env python

from masseuse.core import massage
from masseuse.cli import argparser
from masseuse.kernels import kernels
import datetime as dt
import re

def makeparser(form):
    def parse(astring):
        return dt.datetime.strptime(astring, form).date()
    return parse

def lintimes(times, lpad=0, rpad=0, step=1):
    minday,maxday = min(times),max(times)
    tdelta = (maxday - minday).days
    return [minday + dt.timedelta(days) for days
            in xrange(0-lpad, tdelta+rpad, step)]

def main(args):
    parser = makeparser(args.format)
    kernel = kernels(args.kernel, args.parameter)
    otimes = [parser(line.split()[0])
              for line in args.infile
              if not line.startswith("#")]
    ntimes = lintimes(otimes, args.step)
    args.infile.seek(0)
    massage(parser, kernel, ntimes, args.infile, args.outfile)

if __name__ == "__main__":
    main(argparser().parse_args())
