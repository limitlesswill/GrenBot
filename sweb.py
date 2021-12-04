import socket

class hweb:
  def __init__(self,url="google.com"):
    self.F = b"F" #General Fail Mark
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
      raise Exception(self.result)

  def get_data(self):
    if self.result == "instantiating object problem":
      raise Exception(self.result)
    try:
      self.s.send(self.request)
      self.result = "Request Try block"
    except:
      self.result = "Request exception"
      raise Exception(self.result)

    reply = b""
    try:
      while True:
        tmp = self.s.recv(80**4)
        reply += tmp
        if(len(tmp) <= 0):
          break
      self.result = "data receiving block"
    except Exception as e:
      self.result = f"data receiving exception {str(e)}"
      raise Exception(self.result)
    try:
      self.s.close()
      self.result = "closing connection block"
    except:
      self.result = "closing socket exception"
      raise Exception(self.result)
    return reply
