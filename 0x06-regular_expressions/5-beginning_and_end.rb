#!/usr/bin/env ruby
# Ruby script that matches words/strings starting with "h" and end "n"

puts ARGV[0].scan(/h.n/).join
