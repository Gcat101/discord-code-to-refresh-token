from flask import Flask, request, Response
from requests import post
from os import environ

app = Flask(__name__)

@app.get("/")
def main():
    code = request.args.get("code")
    if not code: return Response("Please provide a \"code\" query parameter.", status=400)

    req = post("https://discord.com/api/oauth2/token", data={
        "grant_type": "authorization_code",
        "code": code,
        "redirect_uri": environ.get("REDIRECT_URL")
    }, headers={"Content-Type": "application/x-www-form-urlencoded"}, auth=(environ.get("CLIENT_ID"), environ.get("CLIENT_SECRET")))
    if req.status_code!=200: return Response(req.text, status=req.status_code)

    return req.json()["refresh_token"]

app.run(port=3214)