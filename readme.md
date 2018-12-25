# parseInst

parseInst - application to parse Instagram data.

## To run:

```
$ git clone https://kharivitalij@bitbucket.org/kharivitalij/parseinst.git 
$ cd parseInt
$ source venv/bin/activate
$ python3 app.py
```

## Some examples:

* http://localhost:5000/api/location - POST with body
```json
{
        "post_url": "https://www.instagram.com/p/BryPljdBfib/"
}
```
returns
```json
{
    "id": "498025257",
    "location": {
        "lat": "56.1",
        "lon": "38.1333"
    },
    "photoSrc": "https://scontent-frt3-2.cdninstagram.com/vp/efbed530961ac1d4c4764793f13d5565/5CCFE029/t51.2885-15/e35/47690624_370553327035409_470915558100859748_n.jpg?_nc_ht=scontent-frt3-2.cdninstagram.com",
    "place": "Krasnoarmeysk, Moskovskaya Oblast', Russia"
}
```

* http://localhost:5000/api/location - POST with body
```json
{
        "post_url": "https://www.instagram.com/p/BmlJrHggOyN/"
}
```
returns
```json
{
    "place": "No place"
}
```

All requests are made with [Postman](https://www.getpostman.com/).