def openbook(book):
    with open(f"books/{book}.txt") as f:
        file_contents = f.read()
        return file_contents

def letterfreq(book):
    bigstring = openbook(book)
    letterdict = {}
    for letter in bigstring:
        loletter = letter.lower()
        if not loletter in letterdict:
            letterdict.update({loletter:1})
        else:
            letterdict[loletter] += 1
    return letterdict
 
def report(book,count,freq):
    print(f"##### Report of the book {book} #####")
    print(f"{book} has {count} words")
    print(f"Below are the frequency of letters")
    sort = dict(sorted(freq.items(), key = lambda item: item[1], reverse=True))
    for key in sort:
        if key.isalpha():
            print(f"{key} is used {sort[key]} times")


def main():
    report("frankenstein",
           len(openbook("frankenstein").split()),
           letterfreq("frankenstein"))




main()

