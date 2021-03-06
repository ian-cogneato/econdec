#!/bin/bash

IFS=','

mkdir .bak
attrib +h .bak

for f in *.txt; do
	echo "mv $f ${f##*data.}"
	mv $f ${f##data.}
	
	echo "cp $f .bak/$f"
	cp $f .bak/$f
	
	echo "mv $f ${f#*-}"
	mv $f ${f#*-}
done

cat log.csv | while read sub file; do
	echo "mv $file sub-${sub}_task-nback_beh.txt"
	mv $file sub-${sub}_task-nback_beh.txt
done

for f in *.txt; do
	ds=ds$(echo $f | cut -c 5)
	sub=${f%%_*}
	echo cp $f ../$ds/$sub/$f
	cp $f ../$ds/$sub/$f
done
