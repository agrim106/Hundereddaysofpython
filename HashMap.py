class HashMap:
    def __init__(self):
        self.size = 1000
        self.map = [[] for _ in range(self.size)]

    def _hash(self, key):
        return hash(key) % self.size

    def put(self, key, value):
        h = self._hash(key)
        for i, (k, v) in enumerate(self.map[h]):
            if k == key:
                self.map[h][i] = (key, value)
                return
        self.map[h].append((key, value))

    def get(self, key):
        h = self._hash(key)
        for k, v in self.map[h]:
            if k == key:
                return v
        return None

    def remove(self, key):
        h = self._hash(key)
        self.map[h] = [(k, v) for k, v in self.map[h] if k != key]

# Example
hashmap = HashMap()
hashmap.put("name", "Agrim")
hashmap.put("age", 25)
print(hashmap.get("name"))  # Output: Agrim
hashmap.remove("name")
print(hashmap.get("name"))  # Output: None
