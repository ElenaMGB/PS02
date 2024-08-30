import requests
import pprint # pretty print для удобного вывода словарей (построчно выводит вложенные словари)
###########POST-запросы #################################
# url = "https://jsonplaceholder.typicode.com/posts"
# data = {
#     "title": "foo", #"тестовый post запрос",
#     "body": "bar", #"тестовый контент post запроса",
#     "userId": 1 #2
# }
# response = requests.post(url, data=data)
# print(response.status_code)
# print (f"ответ - {response.json()}")

#######################################################картинка из Вконтакте#################################
# img = "https://sun3-20.userapi.com/Yfu6G_rSeph-CGRvwcTRYDXYhAMfZoaQG4nQpQ/twzd44SXVgI.png"
# response = requests.get(img)
# with open("test.jpg", "wb") as file:
#     file.write(response.content)

        #   Существующие режимы доступа к файлу:
    # r — только для чтения;
    # w — для записи;
    # wb - запись в бинарном режиме;
    # a — для того, чтобы добавлять в уже созданный файл что-то.

# response = requests.get('https://api.vk.com/method/photos.get?owner_id=-37553664&album_id=2685481&access_token=YOUR_ACCESS_TOKEN')

##############поиск репозиториев по тегу JavaScript на GitHub############################

params = {
    'userId': 1
    # 'q': 'html'
    #'q': 'JavaScript'
    # 'q': 'Python'
    # 'sort': 'stars',
    # 'order': 'desc',
   }
response = requests.get('https://jsonplaceholder.typicode.com/posts', params=params)
# response = requests.get('https://api.github.com/search/repositories', params=params)
# # response = requests.get('https://www.divan.ru/ekaterinburg/')

print(response.status_code)
# print(response.ok)

# if response.ok:
#     print ("запрос успешно выполнен")
# else:
#     print ("произошла ошибка")

# print (response.text) #информация из response о всей странице в одну строку
# print (response.content) #Если ответом на запрос будет являться файл, то лучше .content
# Получить заголовки из ответа  
# print (response.headers)

response_json = response.json()
pprint.pprint(response_json)
