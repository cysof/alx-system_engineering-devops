#!/usr/bin/env ruby
# Ruby script to match "hbttn, hbtttn, hbttttn, hbtttttn"

puts ARGV[0].scan(/hb?tn/).join
