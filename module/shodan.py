import shodan,json

class Shodan:

    def getAPIKey(self) -> str:
        return json.load(open("keys.json"))['SHODAN_API_KEY']

    def searchFaviconHash(self,hash):
        api_key = self.getAPIKey()
        if not "KEY_HERE" in api_key:
            shodan_api = shodan.Shodan(api_key)
            results = shodan_api.search(f"http.favicon.hash:{hash}")
            if results:
                print(f"Total Found -> {results['total']}")
                for i in results['matches']:
                    print("---")
                    print(f"Data -> {i['data']}")
                    print(f"IP -> {i['ip_str']}")
                print("Shodan Query Complete!")
        else:
            print("Please Enter SHODAN APi Key to Keys File..\n")
            exit
