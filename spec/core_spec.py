from datetime import date,datetime,timedelta
from masseuse.core import massage
from mocks import _MockFile
import unittest
import random

def parsedate(x):
    return datetime.strptime(x, "%Y-%m-%d").date()

def _kernel(d):
    if d == 0: return 2
    if d == 1: return 1
    return 0

class MassageSpec(unittest.TestCase):
    def test_acceptance(self):
        def nicerand(n): return [round(random.random(),2) for _ in xrange(n)]
        def nicedate(d): return (date.today() + timedelta(d))
        data = [nicerand(1)+[i+1] for i in xrange(3)]
        times = [nicedate(i+1) for i in xrange(3)]
        mockin = _MockFile(map(lambda (x,xs): "\t".join(map(str,[x]+xs)),
                               zip(times, data)))
        mockout = _MockFile()
        massage(parsedate, _kernel, times, mockin, mockout)

        expected = [[2./3.*data[0][0] + 1./3.*data[1][0] + 0./3.*data[2][0],
                     2./3.*1          + 1./3.*2          + 0./3.*3],
                    [1./4.*data[0][0] + 1./2.*data[1][0] + 1./4.*data[2][0],
                     1./4.*1          + 1./2.*2          + 1./4.*3],
                    [0./3.*data[0][0] + 1./3.*data[1][0] + 2./3.*data[2][0],
                     0./3.*1          + 1./3.*2          + 2./3.*3]]
        for expect,compute in zip(expected,mockout):
            self.assertAlmostEquals(expect[0],compute[0])
            self.assertAlmostEquals(expect[1],compute[1])
