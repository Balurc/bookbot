def main():
  book_path = "books/frankenstein.txt"
  text = get_book_text(book_path)
  total_words = count_words(text)
  chars_count = chars_counter(text)
  sorted_chars_count = dict(sorted(chars_count.items(), key=lambda item: item[1], reverse=True))

  print("--- Begin report of books/frankenstein.txt ---")
  print(f"{total_words} words found in the document")
  print()

  for char in sorted_chars_count:
    if not char.isalpha():
            continue
    print(f"The '{char}' character was found {sorted_chars_count[char]} times")
  print("--- End report ---")

def count_words(text):
  words_split = text.split()
  return len(words_split)

def chars_counter(text):
  chars_count = {}
  for char in text.lower():
    if char not in chars_count:
      chars_count[char] = 1
    else:
      chars_count[char] += 1
  return chars_count

def get_book_text(path):
  with open(path) as f:
    return f.read()

main()


# book_path = "books/frankenstein.txt"
# text = get_book_text(book_path)
# result = chars_counter(text)
# sorted_res = dict(sorted(result.items(), key=lambda item: item[1]))
# print(result)


# for char in sorted_res:
#   print(f"The '{char}' character was found {sorted_res[char]} times")


# words_count = {}

# for word in text.lower().split()[:100]:
#   # print(word)
#   if word not in words_count:
#     words_count[word] = 1
#   else:
#     words_count[word] += 1

# print(words_count)
