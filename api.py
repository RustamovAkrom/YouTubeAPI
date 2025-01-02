# import requests
# import json

# # URL для GraphQL
# url = "http://127.0.0.1:8000/graphql/"

# # GraphQL запрос
# query = """
# mutation UpdateProfile($firstName: String, $avatar: Upload, $userId: ID!) {
#   updateProfile(firstName: $firstName, avatar: $avatar, userId: $userId) {
#     user {
#       username
#       avatar
#     }
#   }
# }
# """

# # Путь к файлу
# file_path = "drawSQL.png"

# # Переменные запроса
# variables = {
#     "userId": 4,
#     "firstName": "admin",
#     "avatar": None  # Файл будет добавлен через map
# }

# # Открытие файла
# with open(file_path, "rb") as file:
#     files = {
#         # Операции GraphQL
#         "operations": (
#             None,
#             json.dumps({"query": query, "variables": variables}),
#             "application/json"
#         ),
#         # Карта файла
#         "map": (None, '{"0": ["variables.avatar"]}', "application/json"),
#         # Файл
#         "0": (file_path, file, "image/png"),
#     }

#     # Заголовки
#     headers = {
#         "Authorization": "JWT eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjo0LCJlbWFpbCI6ImFkbWluQGV4YW1wbGUuY29tIn0.KvHmEvJ1jJBwlKkLEIYCH59FtE8VD1DCycfHOh89YwQ",
#         "Accept": "application/json"
#     }

#     # Отправка запроса
#     response = requests.post(url, files=files, headers=headers)

# # Обработка ответа
# print("Status Code:", response.status_code)
# try:
#     print("Response JSON:", response.json())
# except Exception as e:
#     print("Response Content:", response.content)
