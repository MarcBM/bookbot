from stats import count_words, char_frequency, sorted_frequency

def main():
  path = "books/frankenstein.txt"
  text = get_book_text(path)
  word_count = count_words(text)
  frequency = char_frequency(text)
  sorted_freq = sorted_frequency(frequency)
  
  print("============ BOOKBOT ============")
  print(f"Analyzing book found at {path}...")
  print("----------- Word Count ----------")
  print(f"Found {word_count} total words")
  print("--------- Character Count -------")
  for char in sorted_freq:
    if char["char"].isalpha():
      print(f"{char["char"]}: {char["num"]}")
  print("============= END ===============")

def get_book_text(path):
  with open(path) as f:
    text = f.read()
  return text

main()