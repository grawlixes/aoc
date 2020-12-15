#!/bin/bash

# usage: ./publicGet.sh <year> <day>
# the first part of this script gets your personal input to solve, and the second part tries to scrape the page for sample input
# NOTE: you need your cookie to get your own input, but you DON'T need it to get sample input. this isn't super useful without both functionalities, so I suggest entering it.
# Beat out all those noobs that copy and paste the input

cookie='<INSERT YOUR COOKIE HERE>'

curl 'https://adventofcode.com/'$1'/day/'$2'/input' -X GET -H 'Cookie: session='$cookie > ../$1/day$2/input.txt


# this second part of the script takes a year and day, and it will (hopefully) automatically fill a file in $year/day$day/input2.txt with sample input that is (hopefully) provided for that day. most days have sample input, but not all of them do.
# this program expects that you have the following dir structure, and will put the file here: 
# ./<year>/day<day>/input.txt
# basically, it looks for the first HTML element that "looks like" sample input and saves that to sampleInput.txt. it works for every day in 2020 so far except day 5, which had no sample input. Feel free to check out scanForInput.py for more info on how it works

year=$1
day=$2
dir=../$year/day$day

curl 'https://adventofcode.com/'$1'/day/'$day > $dir/rawCurl.txt

# im better at python anyway lol
# calls scanForInput.py with the directory as the argument
python3 scanForInput.py $dir

# clean up
rm $dir/rawCurl.txt
