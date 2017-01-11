# Micro-img (Python-backend)

Tiny image previews for everyone

## Tech

Python backend using Flask

## How to get this to work

- sudo pip install Flask
- python microimg.py
- Send a post request:

```bash
curl -X POST -F "image=http://www.w3schools.com/html/pic_mountain.jpg" "http://localhost:5000/v0/"
```

- Response should look like this :

```json
{
    "data": "GgAAAwEBAQEAAAAAAAAAAAAAAwQFAgABBv/EAC4QAAICAAQDBAsBAAAAAAAAAAECAAMEESExBRJR\nFDJhkQYTIiMzQUJScXKBsf/EABcBAQEBAQAAAAAAAAAAAAAAAAEDAAL/xAAaEQEBAQEAAwAAAAAA\nAAAAAAAAARExAyFB/9oADAMBAAIRAxEAPwD6adFFxyHdWhFxVR+rL8xyjYMSBOzzGkk8Q4wmHxC1\nBCwGrHqPCLLx5V5iE/XM/wCzMt2WrTWXtYKo3Jkh/SJVdguHJAOQPNvFuIcR7fSK6yFQNmQTqZP7\nNb8nWGsqreIQWyaHhEt3zMrrgLiutqN1XKIRzHPzleusTO8neu5x6DkpEEbNd2849RVWlS3XVNYp\nfIqPty384IpQxJXBtynUe8O0M06MCZpczNV90QoAlEy99TOVCDMgdRBphLHu5HBUbk+ExjfjmNU+\n1gELannOpkrfak43ZcMNh+SotodQdQTEPWnxh8T3f7BgaCHj+0V//9k=\n",
    "status": "ok"
}
```

That should be it

## Limitations (V0)

+ Only JPEG
+ 42x42 fixed ratio (will square all images)
+ Fixed level of details
+ Static headers extraction


## Heroku

[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy?template=https://github.com/RaedsLab/microimg/tree/python-backend)
