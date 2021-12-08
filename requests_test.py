# import requests

# r = requests.get('https://www.baidu.com/')
# print(type(r), r.status_code, type(r.text), r.text[:100], r.cookies, sep='\n')

# data = {
#     'name': 'germey',
#     'age': 25
# }
# r = requests.get('https://www.httpbin.org/get', params=data)
# print(r.text)


# import requests
# import re

# r = requests.get('https://ssr1.scrape.center/')
# pattern = re.compile('<h2.*?>(.*?)</h2>', re.S)
# titles = re.findall(pattern, r.text)
# print(titles)


# import requests

# r = requests.get('https://scrape.center/favicon.ico')
# with open('favicon.ico', 'wb') as f:
#     f.write(r.content)


# import requests

# headers = {
#     'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36'
# }
# r = requests.get('https://www.httpbin.org/get', headers=headers)
# print(r.text)

# data = {'name': 'germey', 'age': 25}
# r = requests.post('https://www.httpbin.org/post', data=data)
# print(r.text)


# import requests

# files = {'file': open('favicon.ico', 'rb')}
# r = requests.post('https://www.httpbin.org/post', files=files)
# print(r.text)


# import requests

# r = requests.get('https://www.baidu.com')
# print(r.cookies)
# for key, value in r.cookies.items():
#     print(key + ' = ' + value)


# import requests

# headers = {
#     'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36',
#     'Cookie':'dotcom_user=JieTrancender;_gh_sess=HRTTt7bNuziD5EVQhfOKJSsL8jtk1hxpqbJP%2BpUHvVELXiGTbQBU9HhaEtn4uV9a%2F%2BM75LXw5zby6HC5DHvgc9nDTe8agzNmiQVsYAWyeMu1HD0GmLEBcfqpJjFxrIiTRu%2F4Omlz4wBUee%2FrX0%2FMyxdCGdT3hSY%2FggufrCXU1GIpoNIjZGuF0TpVqZF3i%2BWP%2Bwk%2Bl%2Bl4D%2FF5yM%2BW1fEVAyI5BXciI185kfAvDb0z%2BRunZzV2048SyocKIyoqrN2i6FF7LRZnF5RETsyiO6jVjm0wSNVbxgdbJ8Rx7oqs0rKYLeTEUPmMJTWyNMi7WfE6mD8JHN34WltnaNEIsHyLr4W53Tfl5XlEEFz8jzS2YNKJe%2BE5Yf5Gzx7k54PKbJsXsjTFeXn0c%2FK9VK1rhlyqMjQ7%2FlAfFFAAP39AQWBc4fWqBXHulLrC3NaYLN9g4HiKxc3CCFDChk7PRmy%2BGFSRqYW2DTmm91Jn8qm2JpfVDWLDVXZM1VfmodPwTlXFK4GzI9PeqaZihF8o0B096SJBGojqPJpOV9rAeSQvTGwjgjv%2B2Ouqc6XWZUSrOTsIzjEz8KiHDIyH5u5nzAlceH5pWtEtamijZwt6obkMea%2BO2RD15aUiwVj5j5FwzHgeg4OkeQMBBOyDwPa7Ts0JwvyPX7ru2T7t1Opba8XPbV0R83yWHXHBKZibY4oKiQOz%2B23Nnb5qsE5eOzFQFbAL%2FMYfoKLZrQ6DkweKHmgJEzlGlbgm%2BcQkjr5KkL%2FLN1XMpEe7GzEIeDcRnnVHa%2FgF0VwDvUBAD581wVKiFmoT%2FwBT1PVmChenorwj%2F3izgy9gp5rIwws6SEfSVUZH%2BYbHAX2mh4E47QW%2BFqr0Ry7rFK890fnde2oZRejyIjTG0Y20deRcXydoPokIonIZ3Be814%2FVMouW%2Fdw%3D--sVHzbR8FoDyR5Rwa--%2BFul66RR0juiJreOcdQB9w%3D%3D;__Host-user_session_same_site=OQd4wKCbfA-5hGhLe3f5T2MKnFbBIX6WYeVr5__eXJwT1A9Z;has_recent_activity=1;user_session=OQd4wKCbfA-5hGhLe3f5T2MKnFbBIX6WYeVr5__eXJwT1A9Z;tz=Asia%2FSh;_device_id=558bdd706d2cad0c65ba8ad5c705050d;logged_in=yes;color_mode=%7B%22color_mode%22%3A%22light%22%2C%22light_theme%22%3A%7B%22name%22%3A%22light%22%2C%22color_mode%22%3A%22light%22%7D%2C%22dark_theme%22%3A%7B%22name%22%3A%22dark%22%2C%22color_mode%22%3A%22dark%22%7D%7D;_octo=GH1.1.719096467.1638967205'
# }
# r = requests.get('https://github.com', headers=headers)
# with open('index.html', 'w') as f:
#     f.write(r.text)


# import requests

# s = requests.Session()
# s.get('https://www.httpbin.org/cookies/set/number/123456789')
# r = s.get('https://www.httpbin.org/cookies')
# print(r.text)


# import requests
# from requests.auth import HTTPBasicAuth

# # r = requests.get('https://ssr3.scrape.center/', auth=HTTPBasicAuth('admin', 'admin'))
# r = requests.get('https://ssr3.scrape.center/', auth=('admin', 'admin'))
# print(r.status_code)

