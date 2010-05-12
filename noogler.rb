#!/usr/bin/env ruby
require 'time'
require 'rubygems'
require 'active_support'

# Pretty-prints the difference between the current time and a fixed point in
# time.
class UntilCalc
  def to_s
    phrases.reject(&:nil?).join ' '
  end

  # The phrases to be assembled in to a string representation.
  def phrases
    [context, weeks, days, hm].reject &:nil?
  end

  # The 'weeks until/since' phrase.
  def weeks
    count = diff / 86400 / 7
    sprintf '%d weeks', count unless count.zero?
  end

  # The 'days until/since' phrase.
  def days
    count = diff / 86400 % 7
    sprintf '%d days', count unless count.zero?
  end

  # The HH:MM part.
  def hm
    sprintf "%02d:%02d", diff % 86400 / 3600, diff % 3600 / 60
  end

  # The temporal positioning part.
  def context
    now < @t0 ? 't minus' : 't ='
  end

  # Cache of the current time.
  attr_accessor_with_default(:now) { Time.now }

  # The absolute difference between now and when.
  attr_accessor_with_default(:diff) { (@t0 - now).abs.floor }

  # Constructs a new UntilCalc using the etime +t0+.
  def initialize(t0)
    @t0 = t0
  end
end

if __FILE__ == $0
  START = Time.parse('2010-06-07 08:00 -0700')
  print UntilCalc.new(START)
end
