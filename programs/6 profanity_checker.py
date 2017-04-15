import urllib
def read_txt():
    quotes=open("H:\spring term 2016\python programming(oops)- Udacity\programs\movie_quotes.txt")
    content=quotes.read()
    quotes.close()
    print content
    return content

def profanity_check():
    content=read_txt()
    connection=urllib.urlopen("http://www.wdylike.appspot.com/?q="+content)
    output=connection.read()
    connection.close()
    #print '\n',output
    if output=='false':
        print " There is no curse word"
    elif output=='true':
        print " warning: profanity alert"
    else:
        print "the content was nt read properly"

profanity_check()
