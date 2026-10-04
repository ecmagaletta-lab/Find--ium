"""find_ium reads a Latin text file and identifies words ending in -ium."""
chosen_text = "test.txt"
latin_source = open(chosen_text)
latin_content = latin_source.read()
latin_strings = latin_content.split()
for vocabulum in latin_strings:
    clean_vocab = vocabulum.rstrip('.,;:!?"')
    print(clean_vocab)



