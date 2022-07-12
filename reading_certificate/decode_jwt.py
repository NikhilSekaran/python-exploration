import jwt


pub_key = """
-----BEGIN PUBLIC KEY-----
MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEApwZmzgmTw6i+JMlp97zC
bHNm3NKnJ3zgOKu34fcst0LGEg+TAOVOp7yIAV9mm/q0W3RLQUlL9uAhG/rccCRl
yolqv8+nABhqpnpe3sAeLO2AcUCzAiY6U8pmnLoUx1EYO+v+/wS0fE5kkwn7CwuX
1o/fIlnOwj3v+b67eFjYyQJ/j4qVb1jtIsip2KC4SIqTN6JUbPCQXKrNAqiR6zni
BP/FPeD3pIU2AyK4drsOeRvii2c+lZ4j2mOI14A+mKJt8SOLx4vAW85NpHWmP2bL
Jb3/PgnTHcBngJPwk6lL7y202o1OLIh/GIwW1nzosU13TahEsSgXbMldW6HvcVV0
yQIDAQAB
-----END PUBLIC KEY-----

"""

encoded_data = "eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsIng1dCI6InFOOEVOT08xaDBMd3hNaUFabnkwMGpOcEkxbyIsImtpZCI6InFOOEVOT08xaDBMd3hNaUFabnkwMGpOcEkxbyJ9.eyJhdWQiOiJtaWNyb3NvZnQ6aWRlbnRpdHlzZXJ2ZXI6OTdmZWMwZTktZDMyMi00OTIyLTgzZTYtNGI4MjA4NDE1ZGRmIiwiaXNzIjoiaHR0cDovL3N0ZnMuYm9zY2guY29tL2FkZnMvc2VydmljZXMvdHJ1c3QiLCJpYXQiOjE1OTE4NTYxMDQsIm5iZiI6MTU5MTg1NjEwNCwiZXhwIjoxNTkxODU5NzA0LCJEaXNwbGF5TmFtZSI6IlNla2FyYW4gTmlraGlsIChSQkVJL0VUUDQpIiwiZmlyc3RuYW1lIjoiTmlraGlsIiwiTlRJRCI6IkVJSzVLT1IiLCJkZXBhcnRtZW50IjoiUkJFSS9FVFA0IiwiZW1haWwiOiJOaWtoaWwuU2VrYXJhbkBpbi5ib3NjaC5jb20iLCJzdWIiOiJFSUs1S09SIiwiYXBwdHlwZSI6IkNvbmZpZGVudGlhbCIsImFwcGlkIjoiOTdmZWMwZTktZDMyMi00OTIyLTgzZTYtNGI4MjA4NDE1ZGRmIiwiYXV0aG1ldGhvZCI6Imh0dHA6Ly9zY2hlbWFzLm1pY3Jvc29mdC5jb20vd3MvMjAwOC8wNi9pZGVudGl0eS9hdXRoZW50aWNhdGlvbm1ldGhvZC93aW5kb3dzIiwiYXV0aF90aW1lIjoiMjAyMC0wNi0xMVQwNjoxNTowNC43NzZaIiwidmVyIjoiMS4wIiwic2NwIjoicHJvZmlsZSBvcGVuaWQifQ.bKNApr9plcdyIUT3qtpa7yZCPrmdtnIszPOhRzt93cEns-eFO7OcmNvuA74GbyrTrDAJhDAEUSamobcLJ9KyzaaNkg2UR6UvrcjRTs_XCB-xqPdEDMTbDdAFqhvCcYj7vR-qGRtorNFdAqmZq8vmHIdGtX3jWEVi4LraBgQBVgLY_WbJwJLSqvTxtY1_6Cx36Cr2FAFTudbq4HzZgbkjQEZoxvrEIXo3etX8ljjmmhRGzcOKxdMYZaZODRUNNP_w1hNqLr9XG0akMWmmj9fUQLN1p1VstZeyn-tnrPgnF7sokf13-rKThHVIvry0tAUHoxDl5IEe73wQ1kfCDqj3DQ"

user_info = jwt.decode(encoded_data, key=pub_key, algorithms='RS256', audience="microsoft:identityserver:97fec0e9-d322-4922-83e6-4b8208415ddf")

# user_info = jwt.decode(encoded_data, key=pub_key)
# print(user_info.validate())
print(user_info)
