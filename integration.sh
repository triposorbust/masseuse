#!/bin/sh

python res/generate.py | tee res/generated.tsv
python massage.py --output res/massaged.tsv res/generated.tsv

pushd res &> /dev/null
R --no-save < line.R
popd &> /dev/null

exit 0
