# python-shoper
Magical Shoper REST API Client

## Wstęp
README napisane w języku polskim, ze względu na oczywisty "userbase".

Magiczny, bo jest w stanie obsłużyć każdy zasób REST API platformy Shoper (nawet te które jeszcze nie istnieją).

## Użycie
Potrzebujemy danych dostępowych dla procesu uwierzytelnienia naszej aplikacji. W tym przypadku uwierzytelnienie następuje na podstawie loginu i hasła, jak założyć nowe konto dla aplikacji w Shoper opisałem tutaj:

[Podstawy REST API - Obsługa API platformy Shoper](https://cwsi.pl/ecommerce/shoper/podstawy-restapi-obsluga-api-platformy-shoper/)

### Autentykacja
Aby korzystać z zasobów REST API Allegro.pl potrzebujemy uzyskać `access_token` służący do uwierzytelnienia naszych żądań.
W tym celu podajemy login i hasło. Token możemy przekazać podczas instancjonowania klienta

```python
from shoperapi import ShoperClient

URL = "https://sklepXXXXX.shoparena.pl/webapi/rest"

client = ShoperClient(<URL>, <LOGIN>, <PASSWORD>, access_token='xxxxxxxxxxxxxxxxxxxxx')

```

Jeżeli chcemy by klient zdobył dla nas `access_token`, należy skorzystać z metody `get_user_token()` klasy `ShoperClient`

```python
from shoperapi import ShoperClient

URL = "https://sklepXXXXX.shoparena.pl/webapi/rest"

client = ShoperClient(<URL>, <LOGIN>, <PASSWORD>)
client.get_user_token()
```

### Korzystanie z zasobów REST API
Uwierzytelniony klient ma dostęp do zasobów REST API platformy Shoper.

#### Przykład użycia:
```python
for page in client.product_images.all():
    print(page)
```

#### Przykład użycia:
```python
print(client.product.single(<id>)
```

#### Przykład użycia:
```python
print(client.product.insert(<data>)
```
