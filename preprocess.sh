#!/bin/sh

cd src
for f in *.html; do
	g++ -DRELEASE -x c++ -E $f | egrep -v '^#' | tr -s '[:space:]' > ../dist/$f
done
