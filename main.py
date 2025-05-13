from stats import count_words, char_frequency

def main():
  path = "books/frankenstein.txt"
  text = get_book_text(path)
  word_count = count_words(text)
  print(f"{word_count} words found in the document")
  frequency = char_frequency(text)
  print(f"Character frequency: {frequency}")

def get_book_text(path):
  with open(path) as f:
    text = f.read()
  return text

main()