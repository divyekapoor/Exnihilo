#!/bin/bash

USAGE="Usage: $0 TARGET [PreprocessorArg1 [PreprocessorArg2 ...]]"

if [ "$#" == "0" ]; then
	echo $USAGE
	exit 1
fi

TARGET_DIR=$1
shift

cd src
for f in *.html; do
	g++ $* -x c++ -E $f | egrep -v '^#' | tr -s '[:space:]' > ../$TARGET_DIR/$f
done
