from collections import deque
class Memory:
    def __init__(self, max_history=5):
        self.history = deque(maxlen=max_history)
    def add(self, query, response):
        self.history.append({
            "query": query,
            "response": response
        })
    def get_history(self):
        return list(self.history)