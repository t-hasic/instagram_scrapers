from instagrapi import Client

cl = Client()
user_info = cl.user_info_by_username("instagram")
print(user_info)