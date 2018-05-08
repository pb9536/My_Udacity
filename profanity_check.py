import urllib

def read_text():
    quotes = open("C:\Users\pb9536\Desktop\Hyd Web Dev\Udacity\Quotes.txt")
    content =quotes.read()
    print(content)
    quotes.close()
    check_profanity(content)

def check_profanity(text):
    connection = urllib.urlopen("http://www.wdylike.appspot.com/?q=" + text)
    output = connection.read()
    print (output)
    connection.close()
    if "true" in output:
        print("profinity Alert")
    elif "false" in output:
        print("Your text is so clear")
    else:
        print("could not scan the file")


read_text()
    
