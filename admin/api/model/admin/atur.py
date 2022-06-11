# from google.cloud import datastore
from google.cloud import datastore
from .model import Admin, admin_KIND


# def LoginAdmin(
#     email,
#     password,
# ):
#     if email != None and password != None:

#         client = datastore.Client()
#         queri = client.query(kind=admin_KIND)
#         queri.add_filter("email", "=", email)

#         satuHasil = list(queri.fetch(limit=1))
#         if satuHasil:
#             data = satuHasil[0]
#             return data
#         return None
