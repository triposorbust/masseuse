A Nice Massage
==============
For your nice time series!
--------------------------


Package delivers a way to kernel-smooth your time series, hooray! Useful for sparse/sporadic data and or erratic samples, i.e. from composite distributions.

![A massaged time series.](/doc/example.png "Gaussian kernel averaging!")


Quickstart
----------

Kernel-averaging can be run on "wide-format" `.tsv`:

```
% python massage.py <filename>
```

Default output is to `stdout` for piped usage. May be redirected to a file via `-o <filename>` flag.


Usage
-----

Input files are `.tsv` where first column gives a date, and subsequent columns give dimension observations for each date. Averaging is done along rows.

```
% python massage.py --help
usage: python massage.py [-h] [--output STR] [--format STR] [--step N]
                         [--kernel STR] [--parameter N]
                         <filename>

kernel-weighted time series density.

positional arguments:
  <filename>            input time-series tsv files.

optional arguments:
  -h, --help            show this help message and exit

input/output options:
  --output STR, -o STR  file for writing output time-series. default: stdout
  --format STR, -f STR  format string for parsing dates. default: "%Y-%m-%d"

density estimation options:
  --step N, -s N        step size for codomain time-series. default: 1
  --kernel STR, -k STR  kernel function. ("gaussian" or "tricubic")
  --parameter N, -p N   characteristic dimension of kernel. default: 15

Andy's free (as in beer) software.
```

In general, choice of characteristic dimension is much more important than choice of kernel.


Testing
-------

Unit and integration test are provided in package. Unit tests can be run with Python `unittest` package:

```
python -m unittest discover -s spec -p "*spec.py"
```

Unit tests should pass. (Phew!)

Integration test is included in convenience script `integration.sh`.

```
% ./integration.sh
...
```

Integration test should produce a smoothed time-series of irregularly sampled Gaussian.

Authors
-------

 - Andy Chiang
 - ...


License
-------

Distributed under The MIT License. Copyright &copy; Andy Chiang 2013.