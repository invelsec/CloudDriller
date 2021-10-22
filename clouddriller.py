import requests as rq
import optparse, mmh3, base64
from module.shodan import Shodan

class CloudDriller:
    
    MESSAGE = """
        Welcome To, CloudDriller
        github.com/invelsec
        Creator -> Burak Ayvaz
    """

    def __init__(self) -> None:
        optionParse = optparse.OptionParser()
        optionParse.add_option("-u","--url",dest="url",help="Url for the getting favicon")
        (userInput,_) = optionParse.parse_args()
        
        print(self.MESSAGE + "\n")

        if userInput.url != None :
            print(f"URL -> {userInput.url}")
            self.getFavicon(userInput.url)
        else:
            print("Please enter specified url!")
    
    def getFavicon(self,url):
        if not "favicon.ico" in url :
            if url[-1] == "/":
                url += "favicon.ico"
            else:
                url += "/favicon.ico"
        favicon = rq.get(url).content
        favicon_hash = mmh3.hash(base64.encodebytes(favicon))
        print(f"Hash Created! -> '{favicon_hash}'\n")
        Shodan().searchFaviconHash(favicon_hash)


CloudDriller()
