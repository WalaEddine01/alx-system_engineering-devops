#!/usr/bin/env ruby
email_pattern = /\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b/
email = "test.email@example.com"

if email =~ email_pattern
  puts "Valid email address!"
else
  puts "Invalid email address."
end

