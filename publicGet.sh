# use this script to automatically get your input for a given day in your repository.
# If you add your session cookie and type "./publicGet.sh 1", then your input from day 1 should end up in day1/input.txt.
# Beat out all those noobs that copy and paste the input

cookie='<INSERT YOUR COOKIE HERE'

curl 'https://adventofcode.com/2020/day/'$1'/input' -X GET -H 'Cookie: session='$cookie > day$1/input.txt
