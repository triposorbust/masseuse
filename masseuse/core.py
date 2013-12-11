import datetime as dt
import numpy as np

def massage(parse, kernel, times, infh, outfh):
    """Uses the dates in input file to build kernel-weighted series."""
    def breakline(line):
        ws = line.split()
        return parse(ws[0]),np.array(ws[1:],dtype='float')
    tvs = map(breakline, infh)
    mat = np.vstack([v for _,v in tvs])
    for time in times:
        wts = np.array([kernel(abs((time - t).days)) for t,_ in tvs])
        tot = np.sum(wts)
        vec = np.sum(wts[:,np.newaxis] * mat, axis=0)/tot
        outfh.write("{0}\t{1}\n".format(time.strftime("%Y-%m-%d"),
                                        "\t".join(map(str, vec))))
