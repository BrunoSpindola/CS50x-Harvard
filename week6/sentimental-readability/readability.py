def count_letters(txt):
    return sum(1 for l in txt if l.isalpha())


def count_words(txt):
    words = txt.split()
    return len(words)


def count_sentences(txt):
    return sum(1 for s in txt if s in ".!?")


# Main
text = input("Text: ")

num_letters = count_letters(text)
num_words = count_words(text)
num_sentences = count_sentences(text)

l = (float(num_letters) / float(num_words)) * 100
s = (float(num_sentences) / float(num_words)) * 100

index = round(0.0588 * l - 0.296 * s - 15.8)

if index < 1:
    print("Before Grade 1")

elif index >= 16:
    print("Grade 16+")

else:
    print(f"Grade {index}")
