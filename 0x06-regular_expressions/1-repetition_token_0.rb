#!/usr/bin/env ruby
# Ruby script to match "hbttn", "hbtttn", "hbttttn", "hbtttttn"

put ARGV[0].scan(/hbt{2,5}n/).join
