import socket

class web:
  def __init__(self,url="google.com.eg"):
    self.host = url
    self.port = 80
    self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    self.ip = socket.gethostbyname(self.host)
    self.s.connect((self.ip , self.port))

  def get_data(self):
    request = b"GET / HTTP/1.0\r\n\r\n"
    self.s.send(request)
    reply = ""
    while True:
      if(len(reply) <= 0):
          break
      reply += self.s.recv(80**4)
    self.s.close()
    return reply
