"""
TinyURL is a URL shortening service where you enter a URL such as https://leetcode.com/problems/design-tinyurl and it 
returns a short URL such as http://tinyurl.com/4e9iAk.

Design the encode and decode methods for the TinyURL service. There is no restriction on how your 
encode/decode algorithm should work. You just need to ensure that a URL can be encoded to a tiny 
URL and the tiny URL can be decoded to the original URL.

"""

class hashMap:
    def __init__(self):
        self.mapping = [[]]*25
    
    def put(self, key, val):
        hash_key = hash(val) % len(self.mapping)
        bucket = self.mapping[hash_key]
        key_exists = False
        for i, kv in enumerate(bucket):
            k, v = kv
            if key == k:
                key_exists = True
                break
        if key_exists:
            bucket.append((hash_key, val))
        else: 
            self.mapping[hash_key] = [(hash_key,val)]
        return key

    def get(self, key):
        hash_key = hash(key) % len(self.mapping)
        bucket = self.mapping[hash_key]
        for i, kv in enumerate(bucket):
            k,v = kv
            return v
        raise KeyError



class Codec:

    def __init__(self):
        self.urlShortener = hashMap()

    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """
        return self.urlShortener.put(hash(longUrl), longUrl)

        

    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
        return self.urlShortener.get(shortUrl)
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))