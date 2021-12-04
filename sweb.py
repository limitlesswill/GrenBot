import socket

class hweb:
  def __init__(self,url="google.com"):
    self.host = url
    self.port = 80
    self.request = b"GET / HTTP/1.0\r\n\r\n"
    self.result = "stage constructor"
    try:
      self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
      self.ip = socket.gethostbyname(self.host)
      self.s.connect((self.ip , self.port))
    except:
      self.result = "connection exception"
    finally:
      self.result = "connection error"

  def get_data(self):
    self.result = "sending request stage"
    try:
      self.s.send(self.request)
    except:
      self.result = "Request exception"
    finally:
      self.result = "Request finally"
    reply = b""
    while True:
      tmp = self.s.recv(80**4)
      reply += tmp
      if(len(tmp) <= 0):
          break
    self.result = "data"
    self.s.close()
    return reply
