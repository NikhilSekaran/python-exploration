import sys
import chilkat

cert = chilkat.CkCert()

#  LoadFromFile will load virtually any certificate format file.
#  It will auto-recognize the format and load appropiately.
#  A base64-encoded DER X.509 certificate file
#  contains the binary DER in base64 encoded form.
#  Therefore, it is a text file that will begin like this:
#  -----BEGIN CERTIFICATE-----
#  MIIFbjCCBFagAwIBAgIGdDPNv/L0MA0GCSqGSIb3DQEBBQUAMIHKMQswCQYDVQQG
#  EwJVUzEQMA4GA1UECBMHQXJpem9uYTETMBEGA1UEBxMKU2NvdHRzZGFsZTEaMBgG
#  ...

success = cert.LoadFromFile("/Users/chilkat/testData/cer/chilkat_base64.cer")
if success is not True:
    print(cert.lastErrorText())
    sys.exit()

#  DN = "Distinguished Name"
print("SubjectDN:" + cert.subjectDN())

print("Common Name:" + cert.subjectCN())
print("Issuer Common Name:" + cert.issuerCN())

print("Serial Number:" + cert.serialNumber())
