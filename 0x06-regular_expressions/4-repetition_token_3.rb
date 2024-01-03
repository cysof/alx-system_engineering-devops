#!/usr/bin/env ruby
# Ruby script that accept one argument and pass it to a regular expression# matching "hbn", "hbon", "hbtn", "hbttn", "hbtttn", "hbttttn"

puts ARGV[0].scan(/hbt*n/).join
