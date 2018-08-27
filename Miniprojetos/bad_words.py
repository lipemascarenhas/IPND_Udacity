import urllib

def read_text():
    quotes = open("C:\Users\Felipe\Desktop\UDACITY\Projetos\Projeto04_smoviesite\movie_quotes\movie_quotes.txt")
    content_of_files = quotes.read()
    print content_of_files
    quotes.close()
    check_profanity(content_of_files)
def check_profanity(text_to_check):
    connection = urllib.urlopen("http://www.wdylike.appspot.com/?q="+text_to_check)
    output = connection.read()
    #print output
    if "true" in output:
        print ("Profanity alert!!!")
    elif "false" in output:
        print ("Everything is okay to your doc ;)")
    else:
        print ("Could not scan this file properly.")
    connection.close()
read_text()
