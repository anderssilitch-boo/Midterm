def longest_word_ending_al(filename):
    """
    Finds and returns the longest word in a file that ends with 'al'.
    """

    longest = ""

    try:
        with open(filename, "r") as f:
            for line in f:
                line = line.lower()


                punctuation = ",.:;!?\"'()[]{}"
                for p in punctuation:
                    line = line.replace(p, "")

                words = line.split()

                for word in words:
                    if word.endswith("al"):
                        if len(word) > len(longest):
                            longest = word

    except FileNotFoundError:
        print("File not found")
        return None

    return longest

result = longest_word_ending_al("textforQ6")
print(result)