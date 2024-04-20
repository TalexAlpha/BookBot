def main():
   book = readingBook()
   amount_Of_words = getting_word_count(book)
   amount_of_characters = getting_characters(book)
   character_book_report = book_report(amount_of_characters)
   character_book_report.sort(reverse=True, key=sorting_dictionary)
   print(f"--- Begin report of {new_book} ---")
   print(f"{amount_Of_words} words")
   for item in character_book_report:
      print(f"This character '{item['characters']}' has shown {item['numbers']} times.")
   print("--- End of Report ---")


def getting_word_count(book_text):
   words = book_text.split()
   return len(words)

def readingBook():
    with open(new_book) as f:
       return f.read()
def getting_characters(book_text):
   lowered_string = book_text.lower()
   character_amount = {}
   for characters in lowered_string:
      if characters in character_amount:
         character_amount[characters] +=1
      else:
         character_amount[characters] = 1 
   return character_amount
def sorting_dictionary(dictionary):
   return dictionary['numbers']

def book_report(dictionary_char):
   new_dictionary = {}
   for key, value in dictionary_char.items():
      if key.isalpha():
         new_dictionary[key] = {'characters':key,'numbers':value}
   

   return list(new_dictionary.values())

new_book = input("Enter the file path to the book text: ")

main()

