"""
'get_likes.py' was created to get the first 1000 posts that user liked.
This script retrieves code from authorization code flow and then gets an access token.
The access token is needed to receive data about likes using vk_api.
Eventually, the data gets stored in a database.
"""


import vk_api



