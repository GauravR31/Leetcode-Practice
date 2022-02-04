import random
import string

class Codec:

    def encoder(self, url):
        code = ''.join(random.choice(string.ascii_lowercase + string.digits) for _ in range(6))
        while code not in self.decoding_map.keys():
            self.encoding_map[url] = code
            self.decoding_map[code] = url
            
    def __init__(self):
        self.encoding_map = {}
        self.decoding_map = {}
        
    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """
        self.encoder(longUrl)
        return self.encoding_map[longUrl]

    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
        return self.decoding_map[shortUrl]
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))