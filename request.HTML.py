import requests
#enter URL 
res = requests.get('URL')
#ensure the request worked
type(res)
res.status_code == requests.code.ok
#see how long the request is
len(res.text)
#print fris 250 lines of HTMl code
print(res.text[:250])
