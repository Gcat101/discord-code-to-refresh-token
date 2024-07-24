# Discord Code To Refresh Token

A simple flask server which can be used as a `redirect_uri` for discord oauth2 applications. Transforms the `code` query param into a `refresh_token`, which can then be used whenever to get the actual access token.

## Config

To get this to work, you need to create a .env file, which should look something like this:

```env
CLIENT_ID = "<App's client ID from the developer panel>"
CLIENT_SECRET = "<App's client secret also from the developer panel>"

REDIRECT_URL = "<The redirect uri you've specified>"
```