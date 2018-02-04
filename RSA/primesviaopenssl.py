from Crypto.Util.asn1 import DerSequence
from OpenSSL import SSL, crypto
def getPrimes(bitsize):
 key=crypto.PKey()
 key.generate_key(crypto.TYPE_RSA,int(bitsize))
 der=DerSequence()
 der.decode(crypto.dump_privatekey(crypto.FILETYPE_ASN1, key))
 return der[4],der[5]

"""
key=crypto.PKey()
key.generate_key(crypto.TYPE_RSA,int(2048))
der=DerSequence()
der.decode(crypto.dump_privatekey(crypto.FILETYPE_ASN1, key))
"""