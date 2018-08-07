Explore REST API in a heartbeat

```
from tk_rest import TKRest
any_api = TKRest("http://jsonplaceholder.typicode.com")
print(any_api.posts.get().json())
```
