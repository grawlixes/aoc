# This script takes a day (1 - 25) as an input, and for that day, runs the code I wrote and pipes the solution and execution time into a file.

year=$1
day=$2
dir="../$1/day$day"
cd $dir

program1="part1.py"
program2="part2.py"
output="output.txt"

echo "Solution and time (in seconds) for day" $day > $output
echo >> $output

echo "Executing both parts from day" $day

echo "p1:" >> $output
{ \time -f "%e" python3 $program1; } >> $output 2>&1
echo >> $output

echo "Completed part 1 from day" $day

echo "p2:" >> $output
{ \time -f "%e" python3 $program2; } >> $output 2>&1

echo "Completed part 2 from day" $day 
