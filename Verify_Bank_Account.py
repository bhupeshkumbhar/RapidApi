import requests
api_url = 'https://bank-account-verification.p.rapidapi.com/v3/tasks'
api_qry =  {"request_id":"68bbb910-da9b-4d8a-9a1d-4bd878b19848"}
api_hdr = {
	"X-RapidAPI-Key": "472f53a83bmsh0945009f2fe0c7bp1d4da4jsn137f40e946b5",
	"X-RapidAPI-Host": "bank-account-verification.p.rapidapi.com"
}
api_rsp = requests.request("GET", api_url, headers=api_hdr, params=api_qry)

print(api_rsp.text)