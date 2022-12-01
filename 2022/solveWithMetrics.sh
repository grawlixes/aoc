# This script takes a day (1 - 25) as an input, and for that day, runs the code I wrote and pipes the solution and execution time into a file.

# It isn't working right now

year=2022
day=$1
dir="bin/$day"
cd $dir

output="output.txt"

echo "Solution and time (in seconds) for day" $day > $output
echo >> $output

echo "Executing both parts from day" $day

echo "p1 and p2:" >> $output
{ \time -f "%e" dune exec main.exe; } >> $output 2>&1
echo >> $output
