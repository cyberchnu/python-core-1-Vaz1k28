def mean(number):
  # Type your code
  number_str = str(number)
  sum = 0
  for i in number_str:
    sum += int(i)
  return sum / len(number_str)
