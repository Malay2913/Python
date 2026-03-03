def print_unique_words(filename):
    with open(filename, 'r') as f:
        text = f.read()
    words = text.split()
    cleaned_words = [word.strip(".,!?;:()[]{}\"'").lower() for word in words]
    unique_words = sorted(set(cleaned_words))
    for word in unique_words:
        print(word)

print_unique_words("sample.txt")