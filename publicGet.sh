# use this script to automatically get your input for a given day in your repository.
# If you add your session cookie and type "./publicGet.sh 2020 1", then your input from year 2020, day 1 should end up in 2020/day1/input.txt.
# Beat out all those noobs that copy and paste the input

cookie='<INSERT YOUR COOKIE HERE'

curl 'https://adventofcode.com/'$1'/day/'$2'/input' -X GET -H 'Cookie: session='$cookie > $1/day$2/input.txt
