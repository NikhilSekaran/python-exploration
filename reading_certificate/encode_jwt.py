import jwt
import datetime
import time

key = 'secret'
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
data = {
    "DisplayName": "Test Name",
    "ID": "ABC1DEF",
    "department": "TEST/XYZ4",
    "email": "Test.Name@test.com"
}

all_data = {
    "aud": "microsoft:identityserver:97fec0e9-d322-4922-83e6-4b8208415ddf",
    "iss": "http://stfs.dummy.com/adfs/services/trust",
    "iat": 1590563724,
    "exp": 1592307225,
    "DisplayName": "Test Name",
    "firstname": "Test",
    "ID": "ABC1DEF",
    "department": "ABC/XYZ",
    "email": "Test.Name@gmail.com",
    "sub": "ABC1DEF",
    "apptype": "Confidential",
    "appid": "97fec0e9-d322-4922-83e6-4b8208415ddf",
    "authmethod": "http://schemas.microsoft.com/ws/2008/06/identity"
                  "/authenticationmethod/windows",
    "auth_time": "2020-05-27T07:02:58.916Z",
    "ver": "1.0",
    "scp": "openid",
    "jti": "f4496611-2080-4b29-a70e-2ba3bece071b"
}

header = {
    "typ": "JWT",
    "alg": "RS256"
}

token_type = {
    "kty": "RSA",
    "use": "sig",
    "alg": "RS256",
    "kid": "qN8ENOO1h0LwxMiAZny00jNpI1o",
    "x5t": "qN8ENOO1h0LwxMiAZny00jNpI1o",
    "n": "pwZmzgmTw6i-JMlp97zCbHNm3NKnJ3zgOKu34fcst0LGEg"
         "-TAOVOp7yIAV9mm_q0W3RLQUlL9uAhG_rccCRlyolqv8"
         "-nABhqpnpe3sAeLO2AcUCzAiY6U8pmnLoUx1EYO-v"
         "-_wS0fE5kkwn7CwuX1o_fIlnOwj3v"
         "-b67eFjYyQJ_j4qVb1jtIsip2KC4SIqTN6JUbPCQXKrNAqiR6zniBP_FPeD3pIU2AyK4drsOeRvii2c-lZ4j2mOI14A-mKJt8SOLx4vAW85NpHWmP2bLJb3_PgnTHcBngJPwk6lL7y202o1OLIh_GIwW1nzosU13TahEsSgXbMldW6HvcVV0yQ",
    "e": "AQAB",
    "x5c": [
        "MIIC2DCCAcCgAwIBAgIQEyoVq5rvTINLaDkGHT98KzANBgkqhkiG9w0BAQsFADAoMSYwJAYDVQQDEx1BREZTIFNpZ25pbmcgLSBzdGZzLmJvc2NoLmNvbTAeFw0xODA1MDcwODA3MTJaFw0yMTA1MDYwODA3MTJaMCgxJjAkBgNVBAMTHUFERlMgU2lnbmluZyAtIHN0ZnMuYm9zY2guY29tMIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEApwZmzgmTw6i+JMlp97zCbHNm3NKnJ3zgOKu34fcst0LGEg+TAOVOp7yIAV9mm/q0W3RLQUlL9uAhG/rccCRlyolqv8+nABhqpnpe3sAeLO2AcUCzAiY6U8pmnLoUx1EYO+v+/wS0fE5kkwn7CwuX1o/fIlnOwj3v+b67eFjYyQJ/j4qVb1jtIsip2KC4SIqTN6JUbPCQXKrNAqiR6zniBP/FPeD3pIU2AyK4drsOeRvii2c+lZ4j2mOI14A+mKJt8SOLx4vAW85NpHWmP2bLJb3/PgnTHcBngJPwk6lL7y202o1OLIh/GIwW1nzosU13TahEsSgXbMldW6HvcVV0yQIDAQABMA0GCSqGSIb3DQEBCwUAA4IBAQAoD137SDAWC0PbbxTCQsBH/QMY8rbnfDk8ASqFbbhoEKzzcdLuT8yiTxvEt9e7kt7WQHJXLh02ynpFsi9Z4w2rvb9h5f08zPjrrBCMryg2gEflxR+HcHscOvsDXW4r8v2/7SrOvvAen8va039rQjCudPJDFTgKZG8HkQbVf5qhgAoIZKycXU/j4fQlaQJLU07uy8E+9JkT2+a7p5yZqDcliLfMG6ATB3U1xZiHml9aizUbVmfHxatkoT18bfJLjmBMtk/IeAthH94l1WD91mxEaSCOTbVgZb8EzNH6I8vNedvYmD6cdEOHBDyn7L+gQUL7U1NS4M8J/CVXM8ZA6fw2"
    ]
}

payload = {"iss": "jeff", "exp": time.time() + 15, "claim": "insanity"}

encoded_data = jwt.encode(payload, key=key, headers=token_type)

print("encoded: ", encoded_data)

print("header_info: ", jwt.get_unverified_header(encoded_data))

decoded_data = jwt.decode(encoded_data, key=key, audience='microsoft:identityserver')

print("decoded: ", decoded_data)
