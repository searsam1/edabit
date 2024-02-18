def is_narcissistic(num)
    digits = num.to_s.chars.map(&:to_i)
    len = digits.length
    sum = digits.inject(0) { |sum, digit| sum + digit ** len }
    sum == num
  end