def count_chars(string):
    d = {}
    for s in string:
        key = s.lower()
        if key in d:
            d[key] = d[key] + 1
        else:
            d[key] = 1
    return d

def count_words(string):
    words = string.split()
    return len(words)

def sort_on(dict):
    return dict["num"]

def main():
    path = "./books/frankenstein.txt"
    with open(path) as f:
        file_contents = f.read()
        number_words = count_words(file_contents)
        number_chars_dict = count_chars(file_contents)
        l = []
        for n in number_chars_dict:
            if n.isalpha():
                l.append({"char": n, "num": number_chars_dict[n]})
        l.sort(reverse=True, key=sort_on)
        print(f"--- Begin report of {path} ---")
        print(f"{number_words} words found in the document")
        print()
        for x in l:
            print(f"The '{x["char"]}' was found {x["num"]} times")
        print("--- End report ---")
main()