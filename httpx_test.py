# import httpx

# headers = {
#     'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36'
# }
# response = httpx.get('https://www.httpbin.org/get', headers=headers)
# print(response.status_code)
# print(response.headers)
# print(response.text)


# import httpx

# headers = {
#     'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36'
# }
# with httpx.Client(headers=headers) as client:
#     response = client.get('https://httpbin.org/headers')
#     print(response.json()['headers']['User-Agent'])


# import httpx

# headers = {
#     'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36'
# }
# with httpx.Client(headers=headers, http2=True, verify=False) as client:
#     response = client.get('https://httpbin.org/get')
#     print(response.text)
#     print(response.http_version)
