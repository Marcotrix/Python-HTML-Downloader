import urllib.request
import chardet
url = input("Enter URL: ")
if url.startswith("https://") or url.startswith("http://"):
    link = url
else:
    link = "https://" + url
    # simple system i made to check if the url has http or https
webUrl  = urllib.request.urlopen(link)

print ("result code: " + str(webUrl.getcode()))
# if everything went right it should be 200

data = webUrl.read()
# print (data) 
# clogs up the terminal so i commented it out
result = chardet.detect(data)
encoding = result['encoding']
decodata = data.decode(encoding, errors="ignore")

def writedecodeidk():
    f = open("test.html", "w")
    return f

f = writedecodeidk()
f.write(decodata)
f.close()

# writes the data to test.html

printoutput = input("Print the data? (Y/n) ")
if printoutput.lower() == "y" or printoutput == "":
    f = open("test.html", "r")
    print(f.read())
    print(url + "'s Data saved!")
else:
    print(url + "'s Data saved!")

    # optionally read the data
