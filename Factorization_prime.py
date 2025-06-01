def test(num):
  a = 2
  soinsu = []
  while num != 1:
    while num % a != 0:
      a += 1
    soinsu.append(a) # Append as integer to count easily later
    num = num / a

  # Count the occurrences of each prime factor
  from collections import Counter
  soinsu_counts = Counter(soinsu)

  # Format the output string with exponents
  result_parts = []
  for factor, count in sorted(soinsu_counts.items()):
    if count == 1:
      result_parts.append(str(factor))
    else:
      result_parts.append(f"{factor}^{count}")

  return " × ".join(result_parts)

print(test(127323019733204843703270))
