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
    "photoSrc": "https://scontent-iad3-1.cdninstagram.com/vp/3305116bc714154433d0e03caff1d0bb/5CA0330A/t51.2885-15/e35/c0.135.1080.1080/s150x150/43076000_254325412094710_3047800879953989757_n.jpg?_nc_ht=scontent-iad3-1.cdninstagram.com",
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

Yuo can also use https://parse-inst-ui.herokuapp.com/ to send requests.