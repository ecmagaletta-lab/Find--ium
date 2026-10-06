"""find_ium reads a Latin text file and identifies words ending in -ium."""
chosen_text = input("Enter the name or path of a Latin .txt file to analyze: ")
try:

    latin_source = open(chosen_text)
    
except FileNotFoundError:
    print("File not found.")    
else:    
    latin_content = latin_source.read()
    latin_strings = latin_content.split()
    unique_words = set()
    for vocabulum in latin_strings:
        clean_vocab = vocabulum.rstrip('.,;:!?"')
        clean_vocab = clean_vocab.lower()
        if clean_vocab.endswith("ium"):
            unique_words.add(clean_vocab)

    words_alpha = sorted(unique_words)
    for word in words_alpha:
        print(word)



