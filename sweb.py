import socket

class hweb:
  def __init__(self,url="google.com"):
    self.host = url
    self.port = 80
    self.request = b"GET / HTTP/1.0\r\n\r\n"
    self.result = "instantiating object problem"
    try:
      self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
      self.ip = socket.gethostbyname(self.host)
      self.s.connect((self.ip , self.port))
      self.result = "constructor stage"
    except:
      self.result = "connection exception"

  def get_data(self):
    self.result = "sending request stage"
    try:
      self.s.send(self.request)
      self.result = "Request Try block"
    except:
      self.result = "Request exception"

    reply = b""
    while True:
      try:
        tmp = self.s.recv(80**4)
        reply += tmp
        if(len(tmp) <= 0):
            break
      except:
        self.result = "data receiving exception"
    try:
      self.s.close()
    except:
      self.result = "closing socket exception"
    return reply
