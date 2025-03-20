# Development Notes

## Requirement

- ( 2022-05-15 21:03:21 )
- Client Library
```
jazzwang:~$ source venv/bin/activate
(venv) jazzwang:~$ pip3 install -U googlemaps
```
- ( 2022-05-15 21:03:43 )
- enable Google Maps Places API
  - https://developers.google.com/maps/documentation/places/web-service/cloud-setup
- https://shell.cloud.google.com/
```sh
$ gcloud services enable "places-backend.googleapis.com"
```
- ( 2022-05-15 21:08:54 )
- Creating API keys
  - https://developers.google.com/maps/documentation/places/web-service/get-api-key
```sh
$ gcloud alpha services api-keys create --display-name "places-test"
```
- ( 2022-05-15 21:26:21 )
- get API Key from https://console.cloud.google.com/google/maps-apis/credentials

## Testing

- ( 2022-05-15 21:27:16 )
- Reference: https://github.com/googlemaps/google-maps-services-python/blob/master/tests/test_places.py#L89-L99
```
(venv) jazzwang:~$ ipython
Python 3.8.9 (default, Oct 26 2021, 07:25:54)
Type 'copyright', 'credits' or 'license' for more information
IPython 8.3.0 -- An enhanced Interactive Python. Type '?' for help.

In [1]: import googlemaps
   ...: from datetime import datetime
   ...: gmaps = googlemaps.Client(key='Add Your Key here')
In [2]: gmaps.places(
    ...:     "restaurant",
    ...:     location=(-33.86746, 151.207090),
    ...:     radius=100,
    ...:     min_price=1,
    ...:     max_price=4,
    ...:     open_now=True,
    ...:     type="liquor_store"
    ...:     )
```

## Lesson Learn

- ( 2022-05-15 22:09:42 )
- From https://developers.google.com/maps/documentation/javascript/examples/place-details?hl=zh-tw
  - it uses following link to open github repo https://github.com/googlemaps/js-samples/tree/sample-place-details
    - https://stackblitz.com/github/googlemaps/js-samples/tree/sample-place-details?file=README.md
    - https://codesandbox.io/embed/github/googlemaps/js-samples/tree/sample-place-details
    - https://jsfiddle.net/gh/get/library/pure/googlemaps/js-samples/tree/master/dist/samples/place-details/jsfiddle
    - https://gitpod.io/#https://github.com/googlemaps/js-samples/blob/sample-place-details/src/index.ts
    - https://ssh.cloud.google.com/cloudshell/editor?cloudshell_git_repo=https%3A%2F%2Fgithub.com%2Fgooglemaps%2Fjs-samples&cloudshell_git_branch=sample-place-details&cloudshell_tutorial=cloud_shell_instructions.md&cloudshell_workspace=.&hl=zh-tw
- it's branch `sample-place-details` of https://github.com/googlemaps/js-samples/