def count_words(text):
  words = text.split()
  return len(words)

def char_frequency(text):
  frequency = {}
  unique_chars = set()
  for char in text:
    lower_char = char.lower()
    if lower_char not in unique_chars:
      unique_chars.add(lower_char)
      frequency[lower_char] = 1
    else:
      frequency[lower_char] += 1
  return frequency