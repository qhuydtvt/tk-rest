import requests


class TKEndPoint:
  def __init__(self, url, end_point):
    self.url = url + "/" + end_point

  def get(self, id=None, headers=None, access_token=None):
    if id is None:
      return requests.get(self.url, headers)
    else:
      return requests.get(self.url + "/" + id, headers)

  def post(self, data, headers=None):
    return requests.post(self.url, json=data, headers=headers)

  def put(self, data, headers=None):
    return requests.put(self.url, json=data, headers=headers)

  def delete(self, id, headers=None):
    return requests.delete(self.url + '/' + id, headers=headers)


class TKRest:
  def __init__(self, url):
    self.url = url
  
  def __getattr__(self, attr):
    return TKEndPoint(self.url, attr)

if __name__ == "__main__":
  t = TKRest("https://learn.techkids.vn/api")
  print(t.classrooms.get().json())
