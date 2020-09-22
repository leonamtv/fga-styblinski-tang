#!/bin/bash

# NAME="output_blx"
NAME="output_ca"
FOLDER="output/"
FMT=".txt"
NUMGER=10000

if [ ! -d "$FOLDER" ]; then
	mkdir "$FOLDER"
fi

SEPARADOOR="-------------"
trap "exit" INT
for DIMENSION in 2 4 6 8 10 12
do
	FILEOUT="$FOLDER$NAME-$DIMENSION$FMT"
	echo "Testando com $DIMENSION dimensões..."
	echo "Testando com várias taxas de mutação diferentes [ 0.1 a 0.5 ]"
	trap "exit" INT
	for TAXAMUTACAO in 0.1 0.2 0.3 0.4 0.5
	do
		echo "tm = $TAXAMUTACAO"
		COM="python main.py -ng $NUMGER -np 20 -ne 2 -tm $TAXAMUTACAO -v -d $DIMENSION"
		echo $SEPARADOOR >> $FILEOUT
		echo $COM >> $FILEOUT
		eval $COM >> $FILEOUT
	done

	echo "Testando com várias elites diferentes [ 1 a 5 ]"
	trap "exit" INT
	for ELITE in 1 2 3 4 5
	do
		echo "ne = $ELITE"
		COM="python main.py -ng $NUMGER -np 20 -ne $ELITE -tm 0.1 -v -d $DIMENSION"
		echo $SEPARADOOR >> $FILEOUT
		echo $COM >> $FILEOUT
		eval $COM >> $FILEOUT
	done

	echo "Testando com várias polulações diferentes (mantendo a proporção de elite)[ 20, 40 e 60 ] d=$DIMENSION"
	trap "exit" INT
	for POP in 20 40 60
	do
		echo "np = $POP, ne = $((POP/10))"
		COM="python main.py -ng $NUMGER -np $POP -ne 2 -tm 0.1 -v -d $DIMENSION"
		echo $SEPARADOOR >> $FILEOUT
		echo $COM >> $FILEOUT
		eval $COM >> $FILEOUT
	done

	echo "Testando uma execução longa ng = $((NUMGER*5))"
	COM="python main.py -ng $((NUMGER*5)) -np 20 -ne 2 -tm 0.1 -v -d $DIMENSION"
	echo $SEPARADOOR >> $FILEOUT
	echo $COM >> $FILEOUT
	eval $COM >> $FILEOUT
done
trap - INT
