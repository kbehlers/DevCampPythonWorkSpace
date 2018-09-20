class Invoice:

    def __init__(self, client, total):
        self._client = client
        self._total = total

    def formatter(self):
        return f'{self._client} owes: ${self._total}'

    #decorator
    @property
    def client(self):
        return self._client

    #decorator
    @client.setter
    def client(self, client):
        self._client = client.lower()

    @property
    def total(self):
        return self._total

google = Invoice('Google', 100)

print(google.client)


#Notice how you still use direct assignment
#Yahoo gets processed by @client.setter
#Setter transforms to .lower(), defined above
google.client = "Yahoo"

print(google.client)