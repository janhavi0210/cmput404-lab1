import requests
print("Requests Version"+requests.__version__)
r=requests.get("https://www.google.com/")
print("Google Homepage:")
print(r.text)
script_clone=request.get("https://raw.githubusercontent.com/janhavi0210/cmput404-lab1/master/lab1.py")
print("Downloaded Source Code:")
print(script_clone.text)
