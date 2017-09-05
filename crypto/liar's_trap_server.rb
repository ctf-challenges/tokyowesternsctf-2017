#!/usr/bin/env ruby
require 'securerandom'
## Parameters
P = 115792089237316195423570985008687907853269984665640564039457584007913129639747
N = 100
K = 25
L = 38 # The number of liars

def apply_polynomial(coeffs, x)
    r = 0
    coeffs.inject(0) do |r, c|
        r = (r * x + c) % P
    end
end

def create_polynomial
    coeff = SecureRandom.hex(64 * K)
    coeff.chars.each_slice(128).map{|a|a.join.to_i(16) % P}
end

secret = SecureRandom.hex(64).to_i(16) % P
polynomial = create_polynomial
polynomial[-1] = secret

# Distribute Secret
user = Array.new(N) {|i| apply_polynomial(polynomial, i + 1)  }

# Some user are liars
[*0...N].shuffle[0, L].each{|i| user[i] = rand(P) }

STDOUT.puts "--- Distributed Secret ---"
N.times do |i|
    STDOUT.puts "User #{i}: #{user[i]}"
end
STDOUT.flush
STDOUT.puts

STDOUT.puts "What's secret? "
STDOUT.flush
input_secret = STDIN.gets.to_i
if input_secret == secret
    STDOUT.puts "OK. I'll give you the flag"
    STDOUT.puts File.read("flag").chomp
else
    STDOUT.puts "Wrong"
end
STDOUT.flush
STDOUT.close