class Node:
  def __init__(self, url: str):
    self.prev = None
    self.next = None
    self.url = url

# A class to represent a browser history
class BrowserHistory:
  def __init__(self, homepage: str):
    self.curr = Node(homepage)

  def visit(self, url: str) -> None:
    self.curr.next = Node(url)
    self.curr.next.prev = self.curr
    self.curr = self.curr.next

  def back(self, steps: int) -> str:
    while self.curr.prev and steps > 0:
      self.curr = self.curr.prev
      steps -= 1
    return self.curr.url

  def forward(self, steps: int) -> str:
    while self.curr.next and steps > 0:
      self.curr = self.curr.next
      steps -= 1
    return self.curr.url


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)

browserHistory = BrowserHistory("leetcode.com")
browserHistory.visit("google.com");       # You are in "leetcode.com". Visit "google.com"
browserHistory.visit("facebook.com");     # You are in "google.com". Visit "facebook.com"
browserHistory.visit("youtube.com");      # You are in "facebook.com". Visit "youtube.com"
browserHistory.back(1);                   # You are in "youtube.com", move back to "facebook.com" return "facebook.com"
browserHistory.back(1);                   # You are in "facebook.com", move back to "google.com" return "google.com"
browserHistory.forward(1);                # You are in "google.com", move forward to "facebook.com" return "facebook.com"
browserHistory.visit("linkedin.com");     # You are in "facebook.com". Visit "linkedin.com"
browserHistory.forward(2);                # You are in "linkedin.com", you cannot move forward any steps.
browserHistory.back(2);                   # You are in "linkedin.com", move back two steps to "facebook.com" then to "google.com". return "google.com"
browserHistory.back(7);                   # You are in "google.com", you can move back only one step to "leetcode.com". return "leetcode.com"