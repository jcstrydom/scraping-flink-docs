[Skip to\\
Content](https://docs.oracle.com/javase/8/docs/technotes/guides/security/StandardNames.html#skip2content)

[![Home Page](https://docs.oracle.com/javase/webdesign/pubs8/im/a.gif)](http://www.oracle.com/ "Oracle Home Page")

- [Java Software](https://www.oracle.com/java/ "Java Software")
- [Java SE Downloads](https://www.oracle.com/java/technologies/javase-downloads.html "Java SE Downloads")
- [Java SE 8 Documentation](https://docs.oracle.com/javase/8/ "Java Documentation")

[Search](https://docs.oracle.com/javase/search.html)

* * *

# Java Cryptography Architecture (JCA) Standard Algorithm Name Documentation for JDK 8

- [`AlgorithmParameterGenerator`\\
Algorithms](https://docs.oracle.com/javase/8/docs/technotes/guides/security/StandardNames.html#AlgorithmParameterGenerator)
- [`AlgorithmParameters`\\
Algorithms](https://docs.oracle.com/javase/8/docs/technotes/guides/security/StandardNames.html#AlgorithmParameters)
- [`CertificateFactory`\\
Types](https://docs.oracle.com/javase/8/docs/technotes/guides/security/StandardNames.html#CertificateFactory)
- [`CertPathBuilder`\\
Algorithms](https://docs.oracle.com/javase/8/docs/technotes/guides/security/StandardNames.html#CertPathBuilder)
- [CertPath Encodings](https://docs.oracle.com/javase/8/docs/technotes/guides/security/StandardNames.html#CertPathEncodings)
- [`CertPathValidator`\\
Algorithms](https://docs.oracle.com/javase/8/docs/technotes/guides/security/StandardNames.html#CertPathValidator)
- [`CertStore` Types](https://docs.oracle.com/javase/8/docs/technotes/guides/security/StandardNames.html#CertStore)
- [`Cipher` (Encryption)\\
Algorithms](https://docs.oracle.com/javase/8/docs/technotes/guides/security/StandardNames.html#Cipher)
- [`Configuration`\\
Types](https://docs.oracle.com/javase/8/docs/technotes/guides/security/StandardNames.html#Configuration)
- [Exemption Mechanisms](https://docs.oracle.com/javase/8/docs/technotes/guides/security/StandardNames.html#Exemption)
- [GSSAPI Mechanisms](https://docs.oracle.com/javase/8/docs/technotes/guides/security/StandardNames.html#GSSAPI)
- [`KeyAgreement`\\
Algorithms](https://docs.oracle.com/javase/8/docs/technotes/guides/security/StandardNames.html#KeyAgreement)
- [`KeyFactory`\\
Algorithms](https://docs.oracle.com/javase/8/docs/technotes/guides/security/StandardNames.html#KeyFactory)
- [`KeyGenerator`\\
Algorithms](https://docs.oracle.com/javase/8/docs/technotes/guides/security/StandardNames.html#KeyGenerator)
- [`KeyManagerFactory`\\
Algorithms](https://docs.oracle.com/javase/8/docs/technotes/guides/security/StandardNames.html#KeyManagerFactory)
- [`KeyPairGenerator`\\
Algorithms](https://docs.oracle.com/javase/8/docs/technotes/guides/security/StandardNames.html#KeyPairGenerator)
- [`KeyStore` Types](https://docs.oracle.com/javase/8/docs/technotes/guides/security/StandardNames.html#KeyStore)
- [`Mac` Algorithms](https://docs.oracle.com/javase/8/docs/technotes/guides/security/StandardNames.html#Mac)
- [`MessageDigest`\\
Algorithms](https://docs.oracle.com/javase/8/docs/technotes/guides/security/StandardNames.html#MessageDigest)
- [`Policy` Types](https://docs.oracle.com/javase/8/docs/technotes/guides/security/StandardNames.html#Policy)
- [`SaslClient`\\
Mechanisms](https://docs.oracle.com/javase/8/docs/technotes/guides/security/StandardNames.html#SaslClient)
- [`SaslServer`\\
Mechanisms](https://docs.oracle.com/javase/8/docs/technotes/guides/security/StandardNames.html#SaslServer)
- [`SecretKeyFactory`\\
Algorithms](https://docs.oracle.com/javase/8/docs/technotes/guides/security/StandardNames.html#SecretKeyFactory)
- [`SecureRandom` Number\\
Generation (RNG) Algorithms](https://docs.oracle.com/javase/8/docs/technotes/guides/security/StandardNames.html#SecureRandom)
- [Service Attributes](https://docs.oracle.com/javase/8/docs/technotes/guides/security/StandardNames.html#Service)
- [`Signature` Algorithms](https://docs.oracle.com/javase/8/docs/technotes/guides/security/StandardNames.html#Signature)
- [`SSLContext`\\
Algorithms](https://docs.oracle.com/javase/8/docs/technotes/guides/security/StandardNames.html#SSLContext)
- [`TrustManagerFactory`\\
Algorithms](https://docs.oracle.com/javase/8/docs/technotes/guides/security/StandardNames.html#TrustManagerFactory)
- [XML Signature\\
(`XMLSignatureFactory`/`KeyInfoFactory`/`TransformService)`\\
Mechanisms](https://docs.oracle.com/javase/8/docs/technotes/guides/security/StandardNames.html#XMLSignature)
- [XML Signature Transform\\
(`TransformService`) Algorithms](https://docs.oracle.com/javase/8/docs/technotes/guides/security/StandardNames.html#TransformService)
- [JSSE Cipher Suite Names](https://docs.oracle.com/javase/8/docs/technotes/guides/security/StandardNames.html#ciphersuites)
- [Additional JSSE Standard Names](https://docs.oracle.com/javase/8/docs/technotes/guides/security/StandardNames.html#jssenames)
  - [Key Types](https://docs.oracle.com/javase/8/docs/technotes/guides/security/StandardNames.html#key-types)
  - [Protocols](https://docs.oracle.com/javase/8/docs/technotes/guides/security/StandardNames.html#protocols)
  - [Authentication Types](https://docs.oracle.com/javase/8/docs/technotes/guides/security/StandardNames.html#authentication-types)
  - [Endpoint Identification Algorithms](https://docs.oracle.com/javase/8/docs/technotes/guides/security/StandardNames.html#endpoint--dentification-algorithms)
- [Security Algorithm Specification](https://docs.oracle.com/javase/8/docs/technotes/guides/security/StandardNames.html#alg)

  - [Specification Template](https://docs.oracle.com/javase/8/docs/technotes/guides/security/StandardNames.html#spectemp)
  - [Algorithm Specifications](https://docs.oracle.com/javase/8/docs/technotes/guides/security/StandardNames.html#algspec)

[Security Algorithm Implementation Requirements](https://docs.oracle.com/javase/8/docs/technotes/guides/security/StandardNames.html#impl)
  - [XML Signature Algorithms](https://docs.oracle.com/javase/8/docs/technotes/guides/security/StandardNames.html#xml-signature-algorithms)

* * *

**Note:** [Java Cryptography Architecture (JCA) Oracle Providers Documentation for JDK 8](https://docs.oracle.com/javase/8/docs/technotes/guides/security/SunProviders.html) contains specific provider and algorithm
information.

* * *

The Java SE Security API requires and uses a set of standard names
for algorithms, certificate and keystore types.

Note that an SE implementation may support additional algorithms
that are not defined in this specification. As a best practice, if an
algorithm is defined in a subsequent version of this specification and
an implementation of an earlier specification supports that algorithm,
the implementation should use the standard name of the algorithm
that is defined in the subsequent specification. Each SE implementation
should also document the algorithms that it supports or adds support
for in subsequent update releases. The algorithms may be documented
in release notes or in a separate document such as
[Java Cryptography Architecture (JCA) Oracle Providers Documentation for JDK 8](https://docs.oracle.com/javase/8/docs/technotes/guides/security/SunProviders.html).

In some cases naming conventions are given for forming names
that are not explicitly listed, to facilitate name consistency
across provider implementations. Items in angle brackets (such as
`<digest>` and `<encryption>`)
are placeholders to be replaced by a specific message digest,
encryption algorithm, or other name.

* * *

**Note:**
Standard names are not case-sensitive.

* * *

This document includes corresponding lists of standard names
relevant to the following security subareas:

- [**Java PKI**\\
**Programmer's Guide**](https://docs.oracle.com/javase/8/docs/technotes/guides/security/certpath/CertPathProgGuide.html)
- [**JSSE Reference**\\
**Guide**](https://docs.oracle.com/javase/8/docs/technotes/guides/security/jsse/JSSERefGuide.html)
- For standard name specifications, See [Algorithms](https://docs.oracle.com/javase/8/docs/technotes/guides/security/StandardNames.html#alg).
- [**Cryptography**\\
**Architecture**](https://docs.oracle.com/javase/8/docs/technotes/guides/security/crypto/CryptoSpec.html)
- [**Single Sign-on Using**\\
**Kerberos in Java**](https://docs.oracle.com/javase/8/docs/technotes/guides/security/jgss/tutorials/index.html)
- [**The Java SASL API**\\
**Programming and Deployment Guide**](https://docs.oracle.com/javase/8/docs/technotes/guides/security/sasl/sasl-refguide.html)
- [**The XML Digital Signature**\\
**API Specification**](https://docs.oracle.com/javase/8/docs/technotes/guides/security/xmldsig/overview.html)

## `AlgorithmParameterGenerator` Algorithms

The algorithm names in this section can be specified when
generating an instance of
`AlgorithmParameterGenerator`.

| Algorithm Name | Description |
| --- | --- |
| DiffieHellman | Parameters for use with the Diffie-Hellman algorithm. |
| DSA | Parameters for use with the Digital Signature Algorithm. |

## `AlgorithmParameters` Algorithms

The algorithm names in this section can be specified when
generating an instance of `AlgorithmParameters`.

| Algorithm Name | Description |
| --- | --- |
| AES | Parameters for use with the AES algorithm. |
| Blowfish | Parameters for use with the Blowfish algorithm. |
| DES | Parameters for use with the DES algorithm. |
| DESede | Parameters for use with the DESede algorithm. |
| DiffieHellman | Parameters for use with the DiffieHellman algorithm. |
| DSA | Parameters for use with the Digital Signature Algorithm. |
| OAEP | Parameters for use with the OAEP algorithm. |
| PBEWith<digest>And<encryption> | Parameters for use with the<br>PBEWith<digest>And<encryption> algorithm. Examples:<br>**PBEWithMD5AndDES**, and **PBEWithHmacSHA256AndAES\_128**. |
| PBE | Parameters for use with the PBE algorithm. _This name should_<br>_not be used, in preference to the more specific PBE-algorithm names_<br>_previously listed._ |
| RC2 | Parameters for use with the RC2 algorithm. |
| RSASSA-PSS | Parameters for use with the RSASSA-PSS signature algorithm. |

## `CertificateFactory` Types

The type in this section can be specified when generating an
instance of `CertificateFactory`.

| Type | Description |
| --- | --- |
| X.509 | The certificate type defined in X.509, also available via<br>[RFC 5280](https://tools.ietf.org/html/rfc5280) |

## `CertPathBuilder` Algorithms

The algorithm in this section can be specified when generating
an instance of `CertPathBuilder`.

| Algorithm Name | Description |
| --- | --- |
| PKIX | The PKIX certification path validation algorithm as defined in<br>the [ValidationAlgorithm service attribute](https://docs.oracle.com/javase/8/docs/technotes/guides/security/StandardNames.html#Service).<br>The output of `CertPathBuilder` instances implementing<br>this algorithm is a certification path validated against the PKIX<br>validation algorithm. |

## CertPath Encodings

The following encodings may be passed to the
`getEncoded` method of `CertPath` or the
`generateCertPath(InputStream inStream, String
encoding)` method of `CertificateFactory`.

| Encoding | Description |
| --- | --- |
| PKCS7 | A PKCS #7 SignedData object, with the only significant field<br>being certificates. In particular, the signature and the contents<br>are ignored. If no certificates are present, a zero-length<br>`CertPath` is assumed. Warning: PKCS #7 does not maintain<br>the order of certificates in a certification path. This means that<br>if a `CertPath` is converted to PKCS #7 encoded bytes and<br>then converted back, the order of the certificates may change,<br>potentially rendering the `CertPath` invalid. Users<br>should be aware of this behavior. See [PKCS #7: Cryptographic\<br>Message Syntax](https://tools.ietf.org/html/rfc2315) for<br>details on PKCS7. |
| PkiPath | An ASN.1 DER encoded sequence of certificates, defined as<br>follows:<br>```<br>    PkiPath ::= SEQUENCE OF Certificate<br>```<br>Within the sequence, the order of certificates is such that the<br>subject of the first certificate is the issuer of the second<br>certificate, and so on. Each certificate in `PkiPath`<br>shall be unique. No certificate may appear more than once in a<br>value of `Certificate` in `PkiPath`. The<br>`PkiPath` format is defined in defect report 279 against<br>X.509 (2000) and is incorporated into Technical Corrigendum 1 (DTC<br>2) for the ITU-T Recommendation X.509 (2000). See [the ITU web site](https://www.itu.int/rec/T-REC-X.509/en) for<br>details. |

## `CertPathValidator` Algorithms

The algorithm in this section can be specified when generating
an instance of `CertPathValidator`.

| Algorithm Name | Description |
| --- | --- |
| PKIX | The PKIX certification path validation algorithm as defined in<br>the [ValidationAlgorithm service\<br>attribute](https://docs.oracle.com/javase/8/docs/technotes/guides/security/StandardNames.html#Service). |

## `CertStore` Types

The type in this section can be specified when generating an
instance of `CertStore`.

| Type | Description |
| --- | --- |
| Collection | A `CertStore` implementation that retrieves<br>certificates and CRLs from a `Collection`. This type of<br>`CertStore` is particularly useful in applications where<br>certificates or CRLs are received in a bag or some sort of<br>attachment, such as with a signed email message or in an SSL<br>negotiation. |
| LDAP | A `CertStore` implementation that fetches<br>certificates and CRLs from an LDAP directory using the schema<br>defined in the [LDAPSchema service\<br>attribute](https://docs.oracle.com/javase/8/docs/technotes/guides/security/StandardNames.html#Service). |

## `Cipher` (Encryption) Algorithms

### Cipher Algorithm Names

The following names can be specified as the _algorithm_
component in a [transformation](https://docs.oracle.com/javase/8/docs/technotes/guides/security/crypto/CryptoSpec.html#trans) when requesting
an instance of `Cipher`.

| Algorithm Name | Description |
| --- | --- |
| AES | Advanced Encryption Standard as specified by NIST in [FIPS 197](https://csrc.nist.gov/publications/detail/fips/197/final).<br>Also known as the Rijndael algorithm by Joan Daemen and Vincent<br>Rijmen, AES is a 128-bit block cipher supporting keys of 128, 192,<br>and 256 bits.<br>To use the AES cipher with only one valid key size, use the<br>format AES\_<n>, where <n> can be 128, 192, or 256. |
| AESWrap | The AES key wrapping algorithm as described in [RFC 3394](https://tools.ietf.org/html/rfc3394).<br>To use the AESWrap cipher with only one valid key size, use the<br>format AESWrap\_<n>, where <n> can be 128, 192, or<br>256. |
| ARCFOUR | A stream cipher believed to be fully interoperable with the RC4<br>cipher developed by Ron Rivest. For more information, see [A Stream Cipher Encryption Algorithm "Arcfour"](https://tools.ietf.org/id/draft-kaukonen-cipher-arcfour-03.txt), Internet Draft<br>(expired). |
| Blowfish | The [Blowfish\<br>block cipher](https://www.schneier.com/blowfish.html) designed by Bruce Schneier. |
| DES | The Digital Encryption Standard as described in [FIPS PUB\<br>46-3](https://csrc.nist.gov/publications/fips/fips46-3/fips46-3.pdf). |
| DESede | Triple DES Encryption (also known as DES-EDE, 3DES, or<br>Triple-DES). Data is encrypted using the DES algorithm three<br>separate times. It is first encrypted using the first subkey, then<br>decrypted with the second subkey, and encrypted with the third<br>subkey. |
| DESedeWrap | The DESede key wrapping algorithm as described in [RFC 3217](https://tools.ietf.org/html/rfc3217). |
| ECIES | Elliptic Curve Integrated Encryption Scheme |
| PBEWith<digest>And<encryption><br>PBEWith<prf>And<encryption> | The password-based encryption algorithm found in (PKCS5), using<br>the specified message digest (<digest>) or pseudo-random<br>function (<prf>) and encryption algorithm<br>(<encryption>). Examples:<br>- **PBEWithMD5AndDES**: The password-based encryption<br>  algorithm as defined in _RSA Laboratories,_<br>  _"PKCS #5: Password-Based Encryption Standard_, version 1.5, Nov<br>  1993\. Note that this algorithm implies [_CBC_](https://docs.oracle.com/javase/8/docs/technotes/guides/security/StandardNames.html#cbcMode) as the cipher mode and [_PKCS5Padding_](https://docs.oracle.com/javase/8/docs/technotes/guides/security/StandardNames.html#pkcs5Pad) as the padding scheme and<br>  cannot be used with any other cipher modes or padding schemes.<br>- **PBEWithHmacSHA256AndAES\_128**: The password-based encryption<br>  algorithm as defined in [PKCS #5: Password-Based Cryptography\<br>  Specification, Version 2.1](https://tools.ietf.org/html/rfc8018). |
| RC2 | Variable-key-size encryption algorithms developed by Ron Rivest<br>for RSA Data Security, Inc. |
| RC4 | Variable-key-size encryption algorithms developed by Ron Rivest<br>for RSA Data Security, Inc. (See note prior for ARCFOUR.) |
| RC5 | Variable-key-size encryption algorithms developed by Ron Rivest<br>for RSA Data Security, Inc. |
| RSA | The RSA encryption algorithm as defined in [PKCS #1 v2.2](https://tools.ietf.org/html/rfc8017) |

### Cipher Algorithm Modes

The following names can be specified as the _mode_
component in a [transformation](https://docs.oracle.com/javase/8/docs/technotes/guides/security/crypto/CryptoSpec.html#trans) when requesting
an instance of `Cipher`.

| Algorithm Name | Description |
| --- | --- |
| NONE | No mode. |
| CBC | Cipher Block Chaining Mode, as defined in [FIPS PUB\<br>81](https://csrc.nist.gov/publications/fips/fips81/fips81.htm). |
| CCM | Counter/CBC Mode, as defined in [NIST Special Publication SP 800-38C: Recommendation for Block Cipher Modes\<br>of Operation: the CCM Mode for Authentication and Confidentiality](https://csrc.nist.gov/publications/detail/sp/800-38c/final). |
| CFB, CFB _x_ | Cipher Feedback Mode, as defined in [FIPS PUB\<br>81](https://csrc.nist.gov/publications/fips/fips81/fips81.htm).<br>Using modes such as CFB and OFB, block ciphers can encrypt data in<br>units smaller than the cipher's actual block size. When requesting<br>such a mode, you may optionally specify the number of bits to be<br>processed at a time by appending this number to the mode name as<br>shown in the _"DES/CFB8/NoPadding"_ and<br>_"DES/OFB32/PKCS5Padding"_ transformations. If no such number<br>is specified, a provider-specific default is used. (For example,<br>the SunJCE provider uses a default of 64 bits for DES.) Thus, block<br>ciphers can be turned into byte-oriented stream ciphers by using an<br>8-bit mode such as CFB8 or OFB8. |
| CTR | A simplification of OFB, Counter mode updates the input block<br>as a counter. |
| CTS | Cipher Text Stealing, as described in Bruce Schneier's book<br>_Applied Cryptography-Second Edition_, John Wiley and Sons,<br>1996. |
| ECB | Electronic Codebook Mode, as defined in [FIPS PUB\<br>81](https://csrc.nist.gov/publications/fips/fips81/fips81.htm) (generally this mode should not be used for multiple blocks of<br>data). |
| GCM | Galois/Counter Mode, as defined in [NIST Special Publication SP 800-38D Recommendation for Block Cipher Modes\<br>of Operation: Galois/Counter Mode (GCM) and GMAC](https://csrc.nist.gov/publications/detail/sp/800-38d/final). |
| OFB, OFB _x_ | Output Feedback Mode, as defined in [FIPS PUB\<br>81](https://csrc.nist.gov/publications/fips/fips81/fips81.htm).<br>Using modes such as CFB and OFB, block ciphers can encrypt data in<br>units smaller than the cipher's actual block size. When requesting<br>such a mode, you may optionally specify the number of bits to be<br>processed at a time by appending this number to the mode name as<br>shown in the DES/CFB8/NoPadding and<br>DES/OFB32/PKCS5Padding transformations. If no such number<br>is specified, a provider-specific default is used. (For example,<br>the SunJCE provider uses a default of 64 bits for DES.) Thus, block<br>ciphers can be turned into byte-oriented stream ciphers by using an<br>8-bit mode such as CFB8 or OFB8. |
| PCBC | Propagating Cipher Block Chaining, as defined by [Kerberos V4](https://web.mit.edu/kerberos/). |

### Cipher Algorithm Padding

The following names can be specified as the _padding_
component in a [transformation](https://docs.oracle.com/javase/8/docs/technotes/guides/security/crypto/CryptoSpec.html#trans) when requesting
an instance of `Cipher`.

| Algorithm Name | Description |
| --- | --- |
| NoPadding | No padding. |
| ISO10126Padding | This padding for block ciphers is described in the [ISO 10126](https://www.iso.org/standard/18114.html) standard. |
| OAEPPadding, OAEPWith _<digest>_ And _<mgf>_ Padding | Optimal Asymmetric Encryption Padding scheme defined in PKCS #1,<br>where _<digest>_ is replaced by the message digest and<br>_<mgf>_ by the mask generation function. Examples:<br>OAEPWithMD5AndMGF1Padding and<br>OAEPWithSHA-512AndMGF1Padding.<br>If OAEPPadding is used, `Cipher` objects<br>are initialized with a<br>`javax.crypto.spec.OAEPParameterSpec` object to supply<br>values needed for OAEPPadding. |
| PKCS1Padding | The padding scheme described in [PKCS #1 v2.2](https://tools.ietf.org/html/rfc8017), used<br>with the RSA algorithm. |
| PKCS5Padding | The padding scheme described in [PKCS #5: Password-Based Cryptography\<br>Specification, version 2.1](https://tools.ietf.org/html/rfc8018). |
| SSL3Padding | The padding scheme defined in the SSL Protocol Version 3.0,<br>November 18, 1996, section 5.2.3.2 (CBC block cipher):<br>```<br>    block-ciphered struct {<br>        opaque content[SSLCompressed.length];<br>        opaque MAC[CipherSpec.hash_size];<br>        uint8 padding[<br>            GenericBlockCipher.padding_length];<br>        uint8 padding_length;<br>    } GenericBlockCipher;<br>```<br>The size of an instance of a GenericBlockCipher must be a multiple<br>of the block cipher's block length.<br>The padding length, which is always present, contributes to the<br>padding, which implies that if:<br>```<br>    sizeof(content) + sizeof(MAC) % block_length = 0, <br>```<br>padding has to be (block\_length - 1) bytes long, because of the<br>existence of `padding_length`.<br>This makes the padding scheme similar (but not quite) to<br>PKCS5Padding, where the padding length is encoded in the padding<br>(and ranges from 1 to block\_length). With the SSL scheme, the<br>sizeof(padding) is encoded in the always present<br>`padding_length` and therefore ranges from 0 to<br>block\_length-1. |

## `Configuration` Types

The type in this section can be specified when generating an
instance of
`javax.security.auth.login.Configuration`.

| Type | Description |
| --- | --- |
| JavaLoginConfig | The default Configuration implementation from the SUN provider,<br>as described in the [ConfigFile class\<br>specification](https://docs.oracle.com/javase/8/docs/technotes/guides/security/jaas/tutorials/LoginConfigFile.html). <br> This type accepts `java.security.URIParameter` as a<br>valid `Configuration.Parameter` type. If this parameter<br>is not specified, then the configuration information is loaded from<br>the sources described in the ConfigFile class specification. If<br>this parameter is specified, the configuration information is<br>loaded solely from the specified URI. |

## Exemption Mechanisms

The following exemption mechanism names can be specified in the
permission policy file that accompanies an application considered
"exempt" from cryptographic restrictions.

| Algorithm Name | Description |
| --- | --- |
| KeyEscrow | An encryption system with a backup decryption capability that<br>allows authorized persons (users, officers of an organization, and<br>government officials), under certain prescribed conditions, to<br>decrypt ciphertext with the help of information supplied by one or<br>more trusted parties who hold special data recovery keys. |
| KeyRecovery | A method of obtaining the secret key used to lock encrypted<br>data. One use is as a means of providing fail-safe access to a<br>corporation's own encrypted information in times of disaster. |
| KeyWeakening | A method in which a part of the key can be escrowed or<br>recovered. |

## GSSAPI Mechanisms

The following mechanisms can be specified when using GSSAPI.
Note that Object Identifiers (OIDs) are specified instead of names
to be consistent with the GSSAPI standard.

| Mechanism OID | Description |
| --- | --- |
| 1.2.840.113554.1.2.2 | The Kerberos v5 GSS-API mechanism defined in [RFC 4121](https://tools.ietf.org/html/rfc4121). |
| 1.3.6.1.5.5.2 | The Simple and Protected GSS-API Negotiation (SPNEGO) mechanism<br>defined in [RFC\<br>4178](https://tools.ietf.org/html/rfc4178). |

## `KeyAgreement` Algorithms

The following algorithm names can be specified when requesting
an instance of `KeyAgreement`.

| Algorithm Name | Description |
| --- | --- |
| DiffieHellman | Diffie-Hellman Key Agreement as defined in _PKCS #3:_<br>_Diffie-Hellman Key-Agreement Standard_, RSA Laboratories, version<br>1.4, November 1993. |
| ECDH | Elliptic Curve Diffie-Hellman as defined in ANSI X9.63 and as<br>described in [RFC\<br>3278](https://tools.ietf.org/html/rfc3278): "Use of Elliptic Curve Cryptography (ECC) Algorithms in<br>Cryptographic Message Syntax (CMS)." |
| ECMQV | Elliptic Curve Menezes-Qu-Vanstone. |

## `KeyFactory` Algorithms

_(Except as noted, these classes create keys for which_
_[`Key.getAlgorithm()`](https://docs.oracle.com/javase/8/docs/api/java/security/Key.html#getAlgorithm--)_
_returns the standard algorithm name.)_

The algorithm names in this section can be specified when
generating an instance of `KeyFactory`.

| Algorithm Name | Description |
| --- | --- |
| DiffieHellman | Keys for the Diffie-Hellman KeyAgreement algorithm.<br>Note: `key.getAlgorithm()` will return "DH" instead<br>of "DiffieHellman". |
| DSA | Keys for the Digital Signature Algorithm. |
| RSA | Keys for the RSA algorithm (Signature/Cipher). |
| RSASSA-PSS | Keys for the RSASSA-PSS algorithm (Signature). |
| EC | Keys for the Elliptic Curve algorithm. |

## `KeyGenerator` Algorithms

The following algorithm names can be specified when requesting
an instance of `KeyGenerator`.

| Algorithm Name | Description |
| --- | --- |
| AES | Key generator for use with the AES algorithm. |
| ARCFOUR | Key generator for use with the ARCFOUR (RC4) algorithm. |
| Blowfish | Key generator for use with the Blowfish algorithm. |
| DES | Key generator for use with the DES algorithm. |
| DESede | Key generator for use with the DESede (triple-DES)<br>algorithm. |
| HmacMD5 | Key generator for use with the HmacMD5 algorithm. |
| HmacSHA1<br>HmacSHA224<br>HmacSHA256<br>HmacSHA384<br>HmacSHA512 | Keys generator for use with the various flavors of the HmacSHA<br>algorithms. |
| RC2 | Key generator for use with the RC2 algorithm. |

## `KeyManagerFactory` Algorithms

The algorithm name in this section can be specified when
generating an instance of `KeyManagerFactory`.

| Algorithm Name | Description |
| --- | --- |
| PKIX | A factory for `X509ExtendedKeyManager`s that manage<br>X.509 certificate-based key pairs for local side authentication<br>according to the rules defined by the IETF PKIX working group in<br>[RFC 5280](https://tools.ietf.org/html/rfc5280) or its<br>successor. The `KeyManagerFactory` must support<br>initialization using the class<br>`javax.net.ssl.KeyStoreBuilderParameters`. |

## `KeyPairGenerator` Algorithms

_(Except as noted, these classes create keys for which_
_[`Key.getAlgorithm()`](https://docs.oracle.com/javase/8/docs/api/java/security/Key.html#getAlgorithm--)_
_returns the standard algorithm name.)_

The algorithm names in this section can be specified when
generating an instance of `KeyPairGenerator`.

| Algorithm Name | Description |
| --- | --- |
| DiffieHellman | Generates keypairs for the Diffie-Hellman KeyAgreement<br>algorithm.<br>Note: `key.getAlgorithm()` will return "DH" instead<br>of "DiffieHellman". |
| DSA | Generates keypairs for the Digital Signature Algorithm. |
| RSA | Generates keypairs for the RSA algorithm<br>(Signature/Cipher). |
| RSASSA-PSS | Generates keypairs for the RSASSA-PSS signature algorithm. |
| EC | Generates keypairs for the Elliptic Curve algorithm. |

## `KeyStore` Types

The types in this section can be specified when generating an
instance of `KeyStore`.

| Type | Description |
| --- | --- |
| jceks | The [proprietary\<br>keystore](https://docs.oracle.com/javase/8/docs/technotes/guides/security/crypto/CryptoSpec.html#KeystoreImplementation) implementation provided by the SunJCE provider. |
| jks | The [proprietary\<br>keystore](https://docs.oracle.com/javase/8/docs/technotes/guides/security/crypto/CryptoSpec.html#KeystoreImplementation) implementation provided by the SUN provider. |
| dks | A domain keystore is a collection of keystores presented as a<br>single logical keystore. It is specified by configuration data<br>whose syntax is described in [DomainLoadStoreParameter](https://docs.oracle.com/javase/8/docs/api/java/security/DomainLoadStoreParameter.html). |
| pkcs11 | A keystore backed by a PKCS #11 token. |
| pkcs12 | The transfer syntax for personal identity information as<br>defined in [PKCS #12: Personal Information\<br>Exchange Syntax v1.1](https://tools.ietf.org/html/rfc7292). |

## `Mac` Algorithms

The following algorithm names can be specified when requesting
an instance of `Mac`.

| Algorithm Name | Description |
| --- | --- |
| HmacMD5 | The HMAC-MD5 keyed-hashing algorithm as defined in [RFC 2104](https://tools.ietf.org/html/rfc2104) "HMAC:<br>Keyed-Hashing for Message Authentication" (February 1997). |
| HmacSHA1<br>HmacSHA224<br>HmacSHA256<br>HmacSHA384<br>HmacSHA512 | The HmacSHA\* algorithms as defined in [RFC 2104](https://tools.ietf.org/html/rfc2104) "HMAC:<br>Keyed-Hashing for Message Authentication" (February 1997) with<br>`SHA-*` as the message digest algorithm. |
| PBEWith<mac> | Mac for use with the [PKCS #5](https://tools.ietf.org/html/rfc8018)<br>password-based message authentication standard, where <mac><br>is a Message Authentication Code algorithm name. Example:<br>**PBEWithHmacSHA1**. |

## `MessageDigest` Algorithms

The algorithm names in this section can be specified when
generating an instance of `MessageDigest`.

| Algorithm Name | Description |
| --- | --- |
| MD2 | The MD2 message digest algorithm as defined in [RFC 1319](https://tools.ietf.org/html/rfc1319). |
| MD5 | The MD5 message digest algorithm as defined in [RFC 1321](https://tools.ietf.org/html/rfc1321). |
| SHA-1<br>SHA-224<br>SHA-256<br>SHA-384<br>SHA-512<br>SHA-512/224<br>SHA-512/256 | Hash algorithms defined in the [FIPS\<br>PUB 180-4](https://csrc.nist.gov/publications/detail/fips/180/4/final).<br>Secure hash algorithms - SHA-1, SHA-224, SHA-256, SHA-384, SHA-512<br>\- for computing a condensed representation of electronic data<br>(message). When a message of any length less than 264 bits (for<br>SHA-1, SHA-224, and SHA-256) or less than 2128 (for SHA-384 and<br>SHA-512) is input to a hash algorithm, the result is an output<br>called a message digest. A message digest ranges in length from 160<br>to 512 bits, depending on the algorithm. |

## `Policy` Types

The type in this section can be specified when generating an
instance of `Policy`.

| Type | Description |
| --- | --- |
| JavaPolicy | The default Policy implementation from the SUN provider, as<br>described in the [PolicyFile](https://docs.oracle.com/javase/8/docs/technotes/guides/security/PolicyFiles.html) guide.<br>This type accepts `java.security.URIParameter` as a<br>valid `Policy.Parameter` type. If this parameter is not<br>specified, then the policy information is loaded from the sources<br>described in the [Default\<br>Policy File Locations](https://docs.oracle.com/javase/8/docs/technotes/guides/security/PolicyFiles.html#DefaultLocs) section of the PolicyFile guide. If this<br>parameter is specified, the policy information is loaded solely<br>from the specified URI. |

## `SaslClient` Mechanisms

The mechanisms in this section can be specified when generating
an instance of `SaslClient`.

| Mechanism | Description |
| --- | --- |
| CRAM-MD5 | See [RFC 2195](https://tools.ietf.org/html/rfc2195).<br>This mechanism supports a hashed user name/password authentication<br>scheme. |
| DIGEST-MD5 | See [RFC 2831](https://tools.ietf.org/html/rfc2831).<br>This mechanism defines how HTTP Digest Authentication can be used<br>as a SASL mechanism. |
| EXTERNAL | See [RFC 2222](https://tools.ietf.org/html/rfc2222).<br>This mechanism obtains authentication information from an external<br>channel (such as TLS or IPsec). |
| GSSAPI | See [RFC 2222](https://tools.ietf.org/html/rfc2222).<br>This mechanism uses the GSSAPI for obtaining authentication<br>information. It supports Kerberos v5 authentication. |
| PLAIN | See [RFC 2595](https://tools.ietf.org/html/rfc2595).<br>This mechanism supports cleartext user name/password<br>authentication. |

## `SaslServer` Mechanisms

The mechanisms in this section can be specified when generating
an instance of `SaslServer`.

| Mechanism | Description |
| --- | --- |
| CRAM-MD5 | See [RFC 2195](https://tools.ietf.org/html/rfc2195).<br>This mechanism supports a hashed user name/password authentication<br>scheme. |
| DIGEST-MD5 | See [RFC 2831](https://tools.ietf.org/html/rfc2831).<br>This mechanism defines how HTTP Digest Authentication can be used<br>as a SASL mechanism. |
| GSSAPI | See [RFC 2222](https://tools.ietf.org/html/rfc2222).<br>This mechanism uses the GSSAPI for obtaining authentication<br>information. It supports Kerberos v5 authentication. |

## `SecretKeyFactory` Algorithms

The following algorithm names can be specified when requesting
an instance of `SecretKeyFactory`.

| Algorithm Name | Description |
| --- | --- |
| AES | Constructs secret keys for use with the AES algorithm. |
| ARCFOUR | Constructs secret keys for use with the ARCFOUR algorithm. |
| DES | Constructs secrets keys for use with the DES algorithm. |
| DESede | Constructs secrets keys for use with the DESede (Triple-DES)<br>algorithm. |
| PBEWith _<digest>_ And _<encryption>_<br>PBEWith _<prf>_ And _<encryption>_ | Secret-key factory for use with PKCS5 password-based<br>encryption, where _<digest>_ is a message digest,<br>_<prf>_ is a pseudo-random function, and<br>_<encryption>_ is an encryption algorithm.<br>Examples:<br>- PBEWithMD5AndDES (PKCS #5, 1.5),<br>- PBEWithHmacSHA256AndAES\_128 (PKCS #5, 2.0)<br>Note: These all use only the low order 8 bits of each password<br>character. |
| PBKDF2With _<prf>_ | Password-based key-derivation algorithm found in [PKCS #5](https://tools.ietf.org/html/rfc8018) using the<br>specified pseudo-random function ( _<prf>_). Example:<br>PBKDF2WithHmacSHA256. |

## `SecureRandom` Number Generation Algorithms

The algorithm name in this section can be specified when
generating an instance of `SecureRandom`.

| Algorithm Name | Description |
| --- | --- |
| NativePRNG | Obtains random numbers from the underlying native OS. No<br>assertions are made as to the blocking nature of generating these<br>numbers. |
| NativePRNGBlocking | Obtains random numbers from the underlying native OS, blocking<br>if necessary. For example, `/dev/random` on UNIX-like<br>systems. |
| NativePRNGNonBlocking | Obtains random numbers from the underlying native OS, without<br>blocking to prevent applications from excessive stalling. For<br>example, `/dev/urandom` on UNIX-like systems. |
| PKCS11 | Obtains random numbers from the underlying installed and<br>configured PKCS11 library. |
| SHA1PRNG | The name of the pseudo-random number generation (PRNG)<br>algorithm supplied by the SUN provider. This algorithm uses SHA-1<br>as the foundation of the PRNG. It computes the SHA-1 hash over a<br>true-random seed value concatenated with a 64-bit counter which is<br>incremented by 1 for each operation. From the 160-bit SHA-1 output,<br>only 64 bits are used. |
| Windows-PRNG | Obtains random numbers from the underlying Windows OS. |

## Service Attributes

A cryptographic service is always associated with a particular
algorithm or type. For example, a digital signature service is
always associated with a particular algorithm (for example, DSA),
and a `CertificateFactory` service is always associated
with a particular certificate type (for example, X.509).

The attributes in this section are for cryptographic services.
The service attributes can be used as filters for selecting
providers.

Both the attribute name and value are case-insensitive.

| Attribute | Description |
| --- | --- |
| ImplementedIn | Whether the implementation for the cryptographic service is<br>done by software or hardware. The value of this attribute is<br>"software" or "hardware". |
| KeySize | The maximum key size that the provider supports for the<br>cryptographic service. |
| LDAPSchema | The name of the specification that defines the LDAP schema that<br>an implementation of an LDAP `CertStore` uses to<br>retrieve certificates and CRLs. The format and semantics of this<br>attribute is the same as described for the ValidationAlgorithm<br>attribute. All LDAP implementations of `CertStore`<br>should provide a value for this attribute. |
| ValidationAlgorithm | The name of the specification that defines the certification<br>path validation algorithm that an implementation of<br>`CertPathBuilder` or `CertPathValidator`<br>supports. RFCs should be specified as "RFC#" (ex: "RFC3280") and<br>Internet Drafts as the name of the draft (ex:<br>"draft-ietf-pkix-rfc2560bis-01.txt"). Values for this attribute<br>that are specified as selection criteria to the<br>`Security.getProviders` method will be compared using<br>the `String.equalsIgnoreCase` method. All PKIX<br>implementations of `CertPathBuilder` and<br>`CertPathValidator` should provide a value for this<br>attribute. |

For example:

```
   map.put("KeyPairGenerator.DSA",
            "sun.security.provider.DSAKeyPairGenerator");
        map.put("KeyPairGenerator.DSA KeySize", "1024");
        map.put("KeyPairGenerator.DSA ImplementedIn", "Software");
```

## `Signature` Algorithms

The algorithm names in this section can be specified when
generating an instance of `Signature`.

| Algorithm Name | Description |
| --- | --- |
| NONEwithRSA | The RSA signature algorithm, which does not use a digesting<br>algorithm (for example, MD5/SHA1) before performing the RSA<br>operation. For more information about the RSA Signature algorithms,<br>see [PKCS\<br>#1 v2.2](https://tools.ietf.org/html/rfc8017). |
| MD2withRSA<br>MD5withRSA | The MD2/MD5 with RSA Encryption signature algorithm, which uses<br>the MD2/MD5 digest algorithm and RSA to create and verify RSA<br>digital signatures as defined in [PKCS #1](https://tools.ietf.org/html/rfc8017). |
| SHA1withRSA<br>SHA224withRSA<br>SHA256withRSA<br>SHA384withRSA<br>SHA512withRSA<br>SHA512/224withRSA<br>SHA512/256withRSA | The signature algorithm with SHA-\* and the RSA encryption<br>algorithm as defined in the OSI Interoperability Workshop, using<br>the padding conventions described in [PKCS #1](https://tools.ietf.org/html/rfc8017). |
| RSASSA-PSS | The signature algorithm that uses the RSASSA-PSS signature scheme as<br>defined in [PKCS #1 v2.2](https://tools.ietf.org/html/rfc8017).<br>Note that this signature algorithm needs parameters such as a digesting<br>algorithm, salt length and MGF1 algorithm, to be supplied before<br>performing the RSA operation. |
| NONEwithDSA | The Digital Signature Algorithm as defined in [FIPS PUB\<br>186-4](https://csrc.nist.gov/publications/detail/fips/186/4/final). The data must be exactly 20 bytes in length. This<br>algorithm is also known as rawDSA. |
| SHA1withDSA<br>SHA224withDSA<br>SHA256withDSA<br>SHA384withDSA<br>SHA512withDSA | The DSA signature algorithms that use these digest algorithms to<br>create and verify digital signatures<br>as defined in [FIPS\<br>PUB 186-4](https://csrc.nist.gov/publications/detail/fips/186/4/final). |
| NONEwithECDSA<br>SHA1withECDSA<br>SHA224withECDSA<br>SHA256withECDSA<br>SHA384withECDSA<br>SHA512withECDSA<br>_(ECDSA)_ | The ECDSA signature algorithms as defined in ANSI<br>X9.62. <br>**Note:**"ECDSA" is an ambiguous name for the "SHA1withECDSA"<br>algorithm and should not be used. The formal name "SHA1withECDSA"<br>should be used instead. |
| <digest>with<encryption> | Use this to form a name for a signature algorithm with a<br>particular message digest (such as MD2 or MD5) and algorithm (such<br>as RSA or DSA), just as was done for the explicitly defined<br>standard names in this section (MD2withRSA, and so on).<br>For the new signature schemes defined in [PKCS #1 v2.2](https://tools.ietf.org/html/rfc8017),<br>for which the <digest>with<encryption> form is<br>insufficient,<br>**<digest>with<encryption>and<mgf>** can be<br>used to form a name. Here, <mgf> should be replaced by a mask<br>generation function such as MGF1. Example:<br>**MD5withRSAandMGF1**. |

## `SSLContext` Algorithms

The algorithm names in this section can be specified when
generating an instance of `SSLContext`.

| Algorithm Name | Description |
| --- | --- |
| SSL | Supports some version of SSL; may support other versions |
| SSLv2 | Supports SSL version 2 or later; may support other<br>versions |
| SSLv3 | Supports SSL version 3; may support other versions |
| TLS | Supports some version of TLS; may support other versions |
| TLSv1 | Supports [RFC\<br>2246: TLS version 1.0](https://tools.ietf.org/html/rfc2246) ; may support other versions |
| TLSv1.1 | Supports [RFC\<br>4346: TLS version 1.1](https://tools.ietf.org/html/rfc4346) ; may support other versions |
| TLSv1.2 | Supports [RFC\<br>5246: TLS version 1.2](https://tools.ietf.org/html/rfc5246) ; may support other versions |

## `TrustManagerFactory` Algorithms

The algorithm name in this section can be specified when
generating an instance of `TrustManagerFactory`.

| Algorithm Name | Description |
| --- | --- |
| PKIX | A factory for `X509ExtendedTrustManager` objects<br>that validate certificate chains according to the rules defined by<br>the IETF PKIX working group in [RFC 5280](https://tools.ietf.org/html/rfc5280), Internet X.509 Public<br>Key Infrastructure Certificate and Certificate Revocation List (CRL)<br>Profile, or its successor. The `TrustManagerFactory` must<br>support initialization using the class<br>`javax.net.ssl.CertPathTrustManagerParameters`. |

## XML Signature (`XMLSignatureFactory`/`KeyInfoFactory`/`TransformService`) Mechanisms

The mechanism in this section can be specified when generating
an instance of `XMLSignatureFactory`,
`KeyInfoFactory`, or `TransformService`. The
mechanism identifies the XML processing mechanism that an
implementation uses internally to parse and generate XML signature
and KeyInfo structures. Also, note that each
`TransformService` instance supports a specific
transform algorithm in addition to a mechanism. The standard names
for the transform algorithms are defined in the next section.

| Mechanism | Description |
| --- | --- |
| DOM | The Document Object Model. See [DOM Mechanism\<br>Requirements](https://docs.oracle.com/javase/8/docs/technotes/guides/security/xmldsig/overview.html#DOM_Mechanism_Requirements) for additional requirements for DOM<br>implementations. |

## XML Signature Transform (`TransformService`) Algorithms

The algorithms in this section can be specified when generating
an instance of `TransformService`. Note that URIs are
specified instead of names to be consistent with the XML Signature
standard. API constants have been defined for each of these URIs,
and these are listed in parentheses after each URI in the table
that follows.

| Algorithm URI | Description |
| --- | --- |
| http://www.w3.org/TR/2001/REC-xml-c14n-20010315<br>(`CanonicalizationMethod.INCLUSIVE`) | The [Canonical XML\<br>(without comments)](https://www.w3.org/TR/2001/REC-xml-c14n-20010315) canonicalization algorithm. |
| http://www.w3.org/TR/2001/REC-xml-c14n-20010315#WithComments<br>(`CanonicalizationMethod.INCLUSIVE_WITH_COMMENTS`) | The [Canonical\<br>XML with comments](https://www.w3.org/TR/2001/REC-xml-c14n-20010315#WithComments) canonicalization algorithm. |
| http://www.w3.org/2001/10/xml-exc-c14n#<br>(`CanonicalizationMethod.EXCLUSIVE`) | The [Exclusive\<br>Canonical XML (without comments)](https://www.w3.org/TR/2002/REC-xml-exc-c14n-20020718/#) canonicalization<br>algorithm. |
| http://www.w3.org/2001/10/xml-exc-c14n#WithComments<br>(`CanonicalizationMethod.EXCLUSIVE_WITH_COMMENTS`) | The [Exclusive Canonical XML with comments](https://www.w3.org/TR/2002/REC-xml-exc-c14n-20020718/#WithComments) canonicalization<br>algorithm. |
| http://www.w3.org/2000/09/xmldsig#base64<br>(`Transform.BASE64`) | The [Base64](https://www.w3.org/TR/xmldsig-core/#sec-Base-64)<br>transform algorithm. |
| http://www.w3.org/2000/09/xmldsig#enveloped-signature<br>(`Transform.ENVELOPED`) | The [Enveloped\<br>Signature](https://www.w3.org/TR/xmldsig-core/#sec-EnvelopedSignature) transform algorithm. |
| http://www.w3.org/TR/1999/REC-xpath-19991116<br>(`Transform.XPATH`) | The [XPath](https://www.w3.org/TR/xmldsig-core/#sec-XPath) transform<br>algorithm. |
| http://www.w3.org/2002/06/xmldsig-filter2<br>(`Transform.XPATH2`) | The [XPath\<br>Filter 2](https://www.w3.org/TR/2002/REC-xmldsig-filter2-20021108/) transform algorithm. |
| http://www.w3.org/TR/1999/REC-xslt-19991116<br>(`Transform.XSLT`) | The [XSLT](https://www.w3.org/TR/xmldsig-core/#sec-XSLT) transform<br>algorithm. |

## JSSE Cipher Suite Names

The following list contains the standard JSSE cipher suite
names. Over time, various groups have added additional cipher
suites to the SSL/TLS namespace. Some JSSE cipher suite names were
defined before TLSv1.0 was finalized, and were therefore given the
`SSL_` prefix. The names mentioned in the TLS RFCs
prefixed with `TLS_` are functionally equivalent to the
JSSE cipher suites prefixed with `SSL_`.

- SSL\_DH\_anon\_EXPORT\_WITH\_DES40\_CBC\_SHA
- SSL\_DH\_anon\_EXPORT\_WITH\_RC4\_40\_MD5
- SSL\_DH\_anon\_WITH\_3DES\_EDE\_CBC\_SHA
- TLS\_DH\_anon\_WITH\_AES\_128\_CBC\_SHA
- TLS\_DH\_anon\_WITH\_AES\_128\_CBC\_SHA256
- TLS\_DH\_anon\_WITH\_AES\_128\_GCM\_SHA256
- TLS\_DH\_anon\_WITH\_AES\_256\_CBC\_SHA
- TLS\_DH\_anon\_WITH\_AES\_256\_CBC\_SHA256
- TLS\_DH\_anon\_WITH\_AES\_256\_GCM\_SHA384
- TLS\_DH\_anon\_WITH\_CAMELLIA\_128\_CBC\_SHA
- TLS\_DH\_anon\_WITH\_CAMELLIA\_128\_CBC\_SHA256
- TLS\_DH\_anon\_WITH\_CAMELLIA\_256\_CBC\_SHA
- TLS\_DH\_anon\_WITH\_CAMELLIA\_256\_CBC\_SHA256
- SSL\_DH\_anon\_WITH\_DES\_CBC\_SHA
- SSL\_DH\_anon\_WITH\_RC4\_128\_MD5
- TLS\_DH\_anon\_WITH\_SEED\_CBC\_SHA
- SSL\_DH\_DSS\_EXPORT\_WITH\_DES40\_CBC\_SHA
- SSL\_DH\_DSS\_WITH\_3DES\_EDE\_CBC\_SHA
- TLS\_DH\_DSS\_WITH\_AES\_128\_CBC\_SHA
- TLS\_DH\_DSS\_WITH\_AES\_128\_CBC\_SHA256
- TLS\_DH\_DSS\_WITH\_AES\_128\_GCM\_SHA256
- TLS\_DH\_DSS\_WITH\_AES\_256\_CBC\_SHA
- TLS\_DH\_DSS\_WITH\_AES\_256\_CBC\_SHA256
- TLS\_DH\_DSS\_WITH\_AES\_256\_GCM\_SHA384
- TLS\_DH\_DSS\_WITH\_CAMELLIA\_128\_CBC\_SHA
- TLS\_DH\_DSS\_WITH\_CAMELLIA\_128\_CBC\_SHA256
- TLS\_DH\_DSS\_WITH\_CAMELLIA\_256\_CBC\_SHA
- TLS\_DH\_DSS\_WITH\_CAMELLIA\_256\_CBC\_SHA256
- SSL\_DH\_DSS\_WITH\_DES\_CBC\_SHA
- TLS\_DH\_DSS\_WITH\_SEED\_CBC\_SHA
- SSL\_DH\_RSA\_EXPORT\_WITH\_DES40\_CBC\_SHA
- SSL\_DH\_RSA\_WITH\_3DES\_EDE\_CBC\_SHA
- TLS\_DH\_RSA\_WITH\_AES\_128\_CBC\_SHA
- TLS\_DH\_RSA\_WITH\_AES\_128\_CBC\_SHA256
- TLS\_DH\_RSA\_WITH\_AES\_128\_GCM\_SHA256
- TLS\_DH\_RSA\_WITH\_AES\_256\_CBC\_SHA
- TLS\_DH\_RSA\_WITH\_AES\_256\_CBC\_SHA256
- TLS\_DH\_RSA\_WITH\_AES\_256\_GCM\_SHA384
- TLS\_DH\_RSA\_WITH\_CAMELLIA\_128\_CBC\_SHA
- TLS\_DH\_RSA\_WITH\_CAMELLIA\_128\_CBC\_SHA256
- TLS\_DH\_RSA\_WITH\_CAMELLIA\_256\_CBC\_SHA
- TLS\_DH\_RSA\_WITH\_CAMELLIA\_256\_CBC\_SHA256
- SSL\_DH\_RSA\_WITH\_DES\_CBC\_SHA
- TLS\_DH\_RSA\_WITH\_SEED\_CBC\_SHA
- SSL\_DHE\_DSS\_EXPORT\_WITH\_DES40\_CBC\_SHA
- SSL\_DHE\_DSS\_EXPORT1024\_WITH\_DES\_CBC\_SHA
- SSL\_DHE\_DSS\_EXPORT1024\_WITH\_RC4\_56\_SHA
- SSL\_DHE\_DSS\_WITH\_3DES\_EDE\_CBC\_SHA
- TLS\_DHE\_DSS\_WITH\_AES\_128\_CBC\_SHA
- TLS\_DHE\_DSS\_WITH\_AES\_128\_CBC\_SHA256
- TLS\_DHE\_DSS\_WITH\_AES\_128\_GCM\_SHA256
- TLS\_DHE\_DSS\_WITH\_AES\_256\_CBC\_SHA
- TLS\_DHE\_DSS\_WITH\_AES\_256\_CBC\_SHA256
- TLS\_DHE\_DSS\_WITH\_AES\_256\_GCM\_SHA384
- TLS\_DHE\_DSS\_WITH\_CAMELLIA\_128\_CBC\_SHA
- TLS\_DHE\_DSS\_WITH\_CAMELLIA\_128\_CBC\_SHA256
- TLS\_DHE\_DSS\_WITH\_CAMELLIA\_256\_CBC\_SHA
- TLS\_DHE\_DSS\_WITH\_CAMELLIA\_256\_CBC\_SHA256
- SSL\_DHE\_DSS\_WITH\_DES\_CBC\_SHA
- SSL\_DHE\_DSS\_WITH\_RC4\_128\_SHA
- TLS\_DHE\_DSS\_WITH\_SEED\_CBC\_SHA
- TLS\_DHE\_PSK\_WITH\_3DES\_EDE\_CBC\_SHA
- TLS\_DHE\_PSK\_WITH\_AES\_128\_CBC\_SHA
- TLS\_DHE\_PSK\_WITH\_AES\_128\_CBC\_SHA256
- TLS\_DHE\_PSK\_WITH\_AES\_128\_GCM\_SHA256
- TLS\_DHE\_PSK\_WITH\_AES\_256\_CBC\_SHA
- TLS\_DHE\_PSK\_WITH\_AES\_256\_CBC\_SHA384
- TLS\_DHE\_PSK\_WITH\_AES\_256\_GCM\_SHA384
- TLS\_DHE\_PSK\_WITH\_NULL\_SHA
- TLS\_DHE\_PSK\_WITH\_NULL\_SHA256
- TLS\_DHE\_PSK\_WITH\_NULL\_SHA384
- TLS\_DHE\_PSK\_WITH\_RC4\_128\_SHA
- SSL\_DHE\_RSA\_EXPORT\_WITH\_DES40\_CBC\_SHA
- SSL\_DHE\_RSA\_WITH\_3DES\_EDE\_CBC\_SHA
- TLS\_DHE\_RSA\_WITH\_AES\_128\_CBC\_SHA
- TLS\_DHE\_RSA\_WITH\_AES\_128\_CBC\_SHA256
- TLS\_DHE\_RSA\_WITH\_AES\_128\_GCM\_SHA256
- TLS\_DHE\_RSA\_WITH\_AES\_256\_CBC\_SHA
- TLS\_DHE\_RSA\_WITH\_AES\_256\_CBC\_SHA256
- TLS\_DHE\_RSA\_WITH\_AES\_256\_GCM\_SHA384
- TLS\_DHE\_RSA\_WITH\_CAMELLIA\_128\_CBC\_SHA
- TLS\_DHE\_RSA\_WITH\_CAMELLIA\_128\_CBC\_SHA256
- TLS\_DHE\_RSA\_WITH\_CAMELLIA\_256\_CBC\_SHA
- TLS\_DHE\_RSA\_WITH\_CAMELLIA\_256\_CBC\_SHA256
- SSL\_DHE\_RSA\_WITH\_DES\_CBC\_SHA
- TLS\_DHE\_RSA\_WITH\_SEED\_CBC\_SHA
- TLS\_ECDH\_anon\_WITH\_3DES\_EDE\_CBC\_SHA
- TLS\_ECDH\_anon\_WITH\_AES\_128\_CBC\_SHA
- TLS\_ECDH\_anon\_WITH\_AES\_256\_CBC\_SHA
- TLS\_ECDH\_anon\_WITH\_NULL\_SHA
- TLS\_ECDH\_anon\_WITH\_RC4\_128\_SHA
- TLS\_ECDH\_ECDSA\_WITH\_3DES\_EDE\_CBC\_SHA
- TLS\_ECDH\_ECDSA\_WITH\_AES\_128\_CBC\_SHA
- TLS\_ECDH\_ECDSA\_WITH\_AES\_128\_CBC\_SHA256
- TLS\_ECDH\_ECDSA\_WITH\_AES\_128\_GCM\_SHA256
- TLS\_ECDH\_ECDSA\_WITH\_AES\_256\_CBC\_SHA
- TLS\_ECDH\_ECDSA\_WITH\_AES\_256\_CBC\_SHA384
- TLS\_ECDH\_ECDSA\_WITH\_AES\_256\_GCM\_SHA384
- TLS\_ECDH\_ECDSA\_WITH\_NULL\_SHA
- TLS\_ECDH\_ECDSA\_WITH\_RC4\_128\_SHA
- TLS\_ECDH\_RSA\_WITH\_3DES\_EDE\_CBC\_SHA
- TLS\_ECDH\_RSA\_WITH\_AES\_128\_CBC\_SHA
- TLS\_ECDH\_RSA\_WITH\_AES\_128\_CBC\_SHA256
- TLS\_ECDH\_RSA\_WITH\_AES\_128\_GCM\_SHA256
- TLS\_ECDH\_RSA\_WITH\_AES\_256\_CBC\_SHA
- TLS\_ECDH\_RSA\_WITH\_AES\_256\_CBC\_SHA384
- TLS\_ECDH\_RSA\_WITH\_AES\_256\_GCM\_SHA384
- TLS\_ECDH\_RSA\_WITH\_NULL\_SHA
- TLS\_ECDH\_RSA\_WITH\_RC4\_128\_SHA
- TLS\_ECDHE\_ECDSA\_WITH\_3DES\_EDE\_CBC\_SHA
- TLS\_ECDHE\_ECDSA\_WITH\_AES\_128\_CBC\_SHA
- TLS\_ECDHE\_ECDSA\_WITH\_AES\_128\_CBC\_SHA256
- TLS\_ECDHE\_ECDSA\_WITH\_AES\_128\_GCM\_SHA256
- TLS\_ECDHE\_ECDSA\_WITH\_AES\_256\_CBC\_SHA
- TLS\_ECDHE\_ECDSA\_WITH\_AES\_256\_CBC\_SHA384
- TLS\_ECDHE\_ECDSA\_WITH\_AES\_256\_GCM\_SHA384
- TLS\_ECDHE\_ECDSA\_WITH\_NULL\_SHA
- TLS\_ECDHE\_ECDSA\_WITH\_RC4\_128\_SHA
- TLS\_ECDHE\_PSK\_WITH\_3DES\_EDE\_CBC\_SHA
- TLS\_ECDHE\_PSK\_WITH\_AES\_128\_CBC\_SHA
- TLS\_ECDHE\_PSK\_WITH\_AES\_128\_CBC\_SHA256
- TLS\_ECDHE\_PSK\_WITH\_AES\_256\_CBC\_SHA
- TLS\_ECDHE\_PSK\_WITH\_AES\_256\_CBC\_SHA384
- TLS\_ECDHE\_PSK\_WITH\_NULL\_SHA
- TLS\_ECDHE\_PSK\_WITH\_NULL\_SHA256
- TLS\_ECDHE\_PSK\_WITH\_NULL\_SHA384
- TLS\_ECDHE\_PSK\_WITH\_RC4\_128\_SHA
- TLS\_ECDHE\_RSA\_WITH\_3DES\_EDE\_CBC\_SHA
- TLS\_ECDHE\_RSA\_WITH\_AES\_128\_CBC\_SHA
- TLS\_ECDHE\_RSA\_WITH\_AES\_128\_CBC\_SHA256
- TLS\_ECDHE\_RSA\_WITH\_AES\_128\_GCM\_SHA256
- TLS\_ECDHE\_RSA\_WITH\_AES\_256\_CBC\_SHA
- TLS\_ECDHE\_RSA\_WITH\_AES\_256\_CBC\_SHA384
- TLS\_ECDHE\_RSA\_WITH\_AES\_256\_GCM\_SHA384
- TLS\_ECDHE\_RSA\_WITH\_NULL\_SHA
- TLS\_ECDHE\_RSA\_WITH\_RC4\_128\_SHA
- TLS\_EMPTY\_RENEGOTIATION\_INFO\_SCSV **[\*](https://docs.oracle.com/javase/8/docs/technotes/guides/security/StandardNames.html#footnote)**
- SSL\_FORTEZZA\_DMS\_WITH\_FORTEZZA\_CBC\_SHA
- SSL\_FORTEZZA\_DMS\_WITH\_NULL\_SHA
- TLS\_KRB5\_EXPORT\_WITH\_DES\_CBC\_40\_MD5
- TLS\_KRB5\_EXPORT\_WITH\_DES\_CBC\_40\_SHA
- TLS\_KRB5\_EXPORT\_WITH\_RC2\_CBC\_40\_MD5
- TLS\_KRB5\_EXPORT\_WITH\_RC2\_CBC\_40\_SHA
- TLS\_KRB5\_EXPORT\_WITH\_RC4\_40\_MD5
- TLS\_KRB5\_EXPORT\_WITH\_RC4\_40\_SHA
- TLS\_KRB5\_WITH\_3DES\_EDE\_CBC\_MD5
- TLS\_KRB5\_WITH\_3DES\_EDE\_CBC\_SHA
- TLS\_KRB5\_WITH\_DES\_CBC\_MD5
- TLS\_KRB5\_WITH\_DES\_CBC\_SHA
- TLS\_KRB5\_WITH\_IDEA\_CBC\_MD5
- TLS\_KRB5\_WITH\_IDEA\_CBC\_SHA
- TLS\_KRB5\_WITH\_RC4\_128\_MD5
- TLS\_KRB5\_WITH\_RC4\_128\_SHA
- TLS\_PSK\_WITH\_3DES\_EDE\_CBC\_SHA
- TLS\_PSK\_WITH\_AES\_128\_CBC\_SHA
- TLS\_PSK\_WITH\_AES\_128\_CBC\_SHA256
- TLS\_PSK\_WITH\_AES\_128\_GCM\_SHA256
- TLS\_PSK\_WITH\_AES\_256\_CBC\_SHA
- TLS\_PSK\_WITH\_AES\_256\_CBC\_SHA384
- TLS\_PSK\_WITH\_AES\_256\_GCM\_SHA384
- TLS\_PSK\_WITH\_NULL\_SHA
- TLS\_PSK\_WITH\_NULL\_SHA256
- TLS\_PSK\_WITH\_NULL\_SHA384
- TLS\_PSK\_WITH\_RC4\_128\_SHA
- SSL\_RSA\_EXPORT\_WITH\_DES40\_CBC\_SHA
- SSL\_RSA\_EXPORT\_WITH\_RC2\_CBC\_40\_MD5
- SSL\_RSA\_EXPORT\_WITH\_RC4\_40\_MD5
- SSL\_RSA\_EXPORT1024\_WITH\_DES\_CBC\_SHA
- SSL\_RSA\_EXPORT1024\_WITH\_RC4\_56\_SHA
- SSL\_RSA\_FIPS\_WITH\_3DES\_EDE\_CBC\_SHA
- SSL\_RSA\_FIPS\_WITH\_DES\_CBC\_SHA
- TLS\_RSA\_PSK\_WITH\_3DES\_EDE\_CBC\_SHA
- TLS\_RSA\_PSK\_WITH\_AES\_128\_CBC\_SHA
- TLS\_RSA\_PSK\_WITH\_AES\_128\_CBC\_SHA256
- TLS\_RSA\_PSK\_WITH\_AES\_128\_GCM\_SHA256
- TLS\_RSA\_PSK\_WITH\_AES\_256\_CBC\_SHA
- TLS\_RSA\_PSK\_WITH\_AES\_256\_CBC\_SHA384
- TLS\_RSA\_PSK\_WITH\_AES\_256\_GCM\_SHA384
- TLS\_RSA\_PSK\_WITH\_NULL\_SHA
- TLS\_RSA\_PSK\_WITH\_NULL\_SHA256
- TLS\_RSA\_PSK\_WITH\_NULL\_SHA384
- TLS\_RSA\_PSK\_WITH\_RC4\_128\_SHA
- SSL\_RSA\_WITH\_3DES\_EDE\_CBC\_SHA
- TLS\_RSA\_WITH\_AES\_128\_CBC\_SHA
- TLS\_RSA\_WITH\_AES\_128\_CBC\_SHA256
- TLS\_RSA\_WITH\_AES\_128\_GCM\_SHA256
- TLS\_RSA\_WITH\_AES\_256\_CBC\_SHA
- TLS\_RSA\_WITH\_AES\_256\_CBC\_SHA256
- TLS\_RSA\_WITH\_AES\_256\_GCM\_SHA384
- TLS\_RSA\_WITH\_CAMELLIA\_128\_CBC\_SHA
- TLS\_RSA\_WITH\_CAMELLIA\_128\_CBC\_SHA256
- TLS\_RSA\_WITH\_CAMELLIA\_256\_CBC\_SHA
- TLS\_RSA\_WITH\_CAMELLIA\_256\_CBC\_SHA256
- SSL\_RSA\_WITH\_DES\_CBC\_SHA
- SSL\_RSA\_WITH\_IDEA\_CBC\_SHA
- SSL\_RSA\_WITH\_NULL\_MD5
- SSL\_RSA\_WITH\_NULL\_SHA
- TLS\_RSA\_WITH\_NULL\_SHA256
- SSL\_RSA\_WITH\_RC4\_128\_MD5
- SSL\_RSA\_WITH\_RC4\_128\_SHA
- TLS\_RSA\_WITH\_SEED\_CBC\_SHA
- TLS\_SRP\_SHA\_DSS\_WITH\_3DES\_EDE\_CBC\_SHA
- TLS\_SRP\_SHA\_DSS\_WITH\_AES\_128\_CBC\_SHA
- TLS\_SRP\_SHA\_DSS\_WITH\_AES\_256\_CBC\_SHA
- TLS\_SRP\_SHA\_RSA\_WITH\_3DES\_EDE\_CBC\_SHA
- TLS\_SRP\_SHA\_RSA\_WITH\_AES\_128\_CBC\_SHA
- TLS\_SRP\_SHA\_RSA\_WITH\_AES\_256\_CBC\_SHA
- TLS\_SRP\_SHA\_WITH\_3DES\_EDE\_CBC\_SHA
- TLS\_SRP\_SHA\_WITH\_AES\_128\_CBC\_SHA
- TLS\_SRP\_SHA\_WITH\_AES\_256\_CBC\_SHA

\*`TLS_EMPTY_RENEGOTIATION_INFO_SCSV` is a new
pseudo-cipher suite to support RFC 5746. See [Transport\\
Layer Security (TLS) Renegotiation Issue](https://docs.oracle.com/javase/8/docs/technotes/guides/security/jsse/tls-renegotiation-issue.html) for more information.

## Additional JSSE Standard Names

### Key Types

The `keyType` parameter passed to the
`chooseClientAlias`, `chooseServerAlias`,
`getClientAliases`, and `getServerAliases`
methods of `X509KeyManager` specifies the public key
types. Each row of the table that follows lists the standard name
that should be used for `keyType`, given the specified
certificate type.

| Name | Certificate Type |
| --- | --- |
| RSA | RSA |
| DSA | DSA |
| DH\_RSA | Diffie-Hellman with RSA signature |
| DH\_DSA | Diffie-Hellman with DSA signature |
| EC | Elliptic Curve |
| EC\_EC | Elliptic Curve with ECDSA signature |
| EC\_RSA | Elliptic Curve with RSA signature |
| RSASSA-PSS | RSASSA-PSS |

### Protocols

The `protocols` parameter passed to the
`setEnabledProtocols` method of `SSLSocket`
specifies the protocol versions to be enabled for use on the
connection. The table that follows lists the standard names that
can be passed to `setEnabledProtocols` or that may be
returned by the `SSLSocket getSupportedProtocols` and
`getEnabledProtocols` methods.

| Name | Protocol |
| --- | --- |
| SSLv2 | SSL version 2 protocol |
| SSLv3 | SSL version 3 protocol |
| TLSv1 | TLS version 1.0 protocol (defined in [RFC 2246](https://tools.ietf.org/html/rfc2246)) |
| TLSv1.1 | TLS version 1.1 protocol (defined in [RFC 4346](https://tools.ietf.org/html/rfc4346)) |
| TLSv1.2 | TLS version 1.2 protocol (defined in [RFC 5246](https://tools.ietf.org/html/rfc5246)) |
| SSLv2Hello | Currently, the SSLv3, TLSv1, and TLSv1.1 protocols allow you to<br>send SSLv3, TLSv1, and TLSv1.1 hellos encapsulated in an SSLv2<br>format hello. For more details on the reasons for allowing this<br>compatibility in these protocols, see Appendix E in the appropriate<br>RFCs (previously listed).<br>Note that some SSL/TLS servers do not support the v2 hello format<br>and require that client hellos conform to the SSLv3 or TLSv1 client<br>hello formats.<br>The SSLv2Hello option controls the SSLv2 encapsulation. If<br>SSLv2Hello is disabled on the client, then all outgoing messages<br>will conform to the SSLv3/TLSv1 client hello format. If SSLv2Hello<br>is disabled on the server, then all incoming messages must conform<br>to the SSLv3/TLSv1 client hello format. |

### Authentication Types

The `authType` parameter passed to the
`checkClientTrusted` and `checkServerTrusted`
methods of `X509TrustManager` indicates the
authentication type. The table that follows specifies what standard
names should be used for the client or server certificate
chains.

| Client or Server Certificate Chain | Authentication Type Standard Name |
| --- | --- |
| Client | Determined by the actual certificate used. For instance, if<br>RSAPublicKey is used, the `authType` should be<br>"RSA". |
| Server | The key exchange algorithm portion of the cipher suites<br>represented as a String, such as "RSA" or "DHE\_DSS". Note: For some<br>exportable cipher suites, the key exchange algorithm is determined<br>at runtime during the handshake. For instance, for<br>TLS\_RSA\_EXPORT\_WITH\_RC4\_40\_MD5, the `authType` should be<br>"RSA\_EXPORT" when an ephemeral RSA key is used for the key<br>exchange, and "RSA" when the key from the server certificate is<br>used. Or it can take the value "UNKNOWN". |

### Endpoint Identification Algorithms

The JDK 8 release supports endpoint identification algorithms. The
algorithm name can be passed to the
`setEndpointIdentificationAlgorithm()` method of
`javax.net.ssl.SSLParameters`. The following table shows
the currently recognized names.

| Endpoint Identification<br>Algorithm Name | Specification |
| --- | --- |
| HTTPS | [RFC 2818](https://tools.ietf.org/html/rfc2818) |
| LDAPS | [RFC 2830](https://tools.ietf.org/html/rfc2830) |

* * *

## Security Algorithm Specification

This section specifies details concerning some of the algorithms
defined in this document. Any provider supplying an implementation
of the listed algorithms must comply with the specifications in
this section.

To add a new algorithm not specified here, you should first
survey other people or companies supplying provider packages to see
if they have already added that algorithm, and, if so, use the
definitions they published, if available. Otherwise, you should
create and make available a template, similar to those found in
this section, with the specifications for the algorithm you
provide.

### Specification Template

The following table shows the fields of the algorithm
specifications.

| **Field** | **Description** |
| --- | --- |
| Name | The name by which the algorithm is known. This is<br>the name passed to the `getInstance` method (when<br>requesting the algorithm), and returned by the<br>`getAlgorithm` method to determine the name of an<br>existing algorithm object. These methods are in the relevant engine<br>classes: `Signature`,<br>`MessageDigest`,<br>`KeyPairGenerator`, and<br>`AlgorithmParameterGenerator`<br>. |
| Type | The type of algorithm: `Signature`,<br>`MessageDigest`, `KeyPairGenerator`, or<br>`AlgorithmParameterGenerator`. |
| Description | General notes about the algorithm, including any<br>standards implemented by the algorithm, applicable patents, and so<br>on. |
| `KeyPair` Algorithm<br>( _optional_) | The keypair algorithm for this algorithm. |
| Keysize ( _optional_) | For a keyed algorithm or key generation algorithm:<br>the valid keysizes. |
| Size ( _optional_) | For an algorithm parameter generation algorithm:<br>the valid "sizes" for algorithm parameter generation. |
| Parameter Defaults ( _optional_) | For a key generation algorithm: the default<br>parameter values. |
| `Signature` Format ( _optional_) | For a `Signature` algorithm, the format<br>of the signature, that is, the input and output of the verify and<br>sign methods, respectively. |

### Algorithm Specifications

#### SHA-1 Message Digest Algorithm

| Field | Description |
| --- | --- |
| **Name** | SHA-1 |
| **Type** | `MessageDigest` |
| **Description** | The message digest algorithm as defined in [NIST's\<br>FIPS 180-4](https://csrc.nist.gov/publications/detail/fips/180/4/final). The output of this algorithm is a 160-bit<br>digest. |

#### SHA-224 Message Digest Algorithm

| Field | Description |
| --- | --- |
| **Name** | SHA-224 |
| **Type** | `MessageDigest` |
| **Description** | The message digest algorithm as defined in [NIST's\<br>FIPS 180-4](https://csrc.nist.gov/publications/detail/fips/180/4/final). The output of this algorithm is a 224-bit<br>digest. |

#### SHA-256 Message Digest Algorithm

| Field | Description |
| --- | --- |
| **Name** | SHA-256 |
| **Type** | `MessageDigest` |
| **Description** | The message digest algorithm as defined in [NIST's\<br>FIPS 180-4](https://csrc.nist.gov/publications/detail/fips/180/4/final). The output of this algorithm is a 256-bit<br>digest. |

#### SHA-384 Message Digest Algorithm

| Field | Description |
| --- | --- |
| **Name** | SHA-384 |
| **Type** | `MessageDigest` |
| **Description** | The message digest algorithm as defined in [NIST's\<br>FIPS 180-4](https://csrc.nist.gov/publications/detail/fips/180/4/final). The output of this algorithm is a 384-bit<br>digest. |

#### SHA-512 Message Digest Algorithm

| Field | Description |
| --- | --- |
| **Name** | SHA-512 |
| **Type** | `MessageDigest` |
| **Description** | The message digest algorithm as defined in [NIST's\<br>FIPS 180-4](https://csrc.nist.gov/publications/detail/fips/180/4/final). The output of this algorithm is a 512-bit<br>digest. |

#### SHA-512/224 Message Digest Algorithm

| Field | Description |
| --- | --- |
| **Name** | SHA-512/224 |
| **Type** | `MessageDigest` |
| **Description** | The message digest algorithm as defined in [NIST's\<br>FIPS 180-4](https://csrc.nist.gov/publications/detail/fips/180/4/final). The output of this algorithm is a 224-bit<br>digest. |

#### SHA-512/256 Message Digest Algorithm

| Field | Description |
| --- | --- |
| **Name** | SHA-512/256 |
| **Type** | `MessageDigest` |
| **Description** | The message digest algorithm as defined in [NIST's\<br>FIPS 180-4](https://csrc.nist.gov/publications/detail/fips/180/4/final). The output of this algorithm is a 256-bit<br>digest. |

#### MD2 Message Digest Algorithm

| Field | Description |
| --- | --- |
| **Name** | MD2 |
| **Type** | `MessageDigest` |
| **Description** | The message digest algorithm as defined in [RFC 1319](https://tools.ietf.org/html/rfc1319). The output of<br>this algorithm is a 128-bit (16 byte) digest. |

#### MD5 Message Digest Algorithm

| Field | Description |
| --- | --- |
| **Name** | MD5 |
| **Type** | `MessageDigest` |
| **Description** | The message digest algorithm as defined in [RFC 1321](https://tools.ietf.org/html/rfc1321). The output of<br>this algorithm is a 128-bit (16 byte) digest. |

#### The Digital Signature Algorithm, with SHA-1 or SHA-2

| Field | Description |
| --- | --- |
| **Name** | SHA1withDSA, SHA224withDSA, SHA256withDSA, SHA384withDSA,<br>and SHA512withDSA |
| **Type** | `Signature` |
| **Description** | This algorithm is the signature algorithm described<br>in [NIST FIPS 186-4](https://csrc.nist.gov/publications/detail/fips/186/4/final), using DSA with the SHA-1, SHA-224, SHA-256, SHA-384,<br>and SHA-512 message digest algorithms. |
| **`KeyPair` Algorithm** | DSA |
| **Signature Format** | ASN.1 sequence of two INTEGER values:<br>`r` and `s`, in that order:<br>`SEQUENCE ::= { r INTEGER, s INTEGER }` |

#### RSA-based Signature Algorithms, with MD2, MD5, SHA-1, or SHA-2

| Field | Description |
| --- | --- |
| **Names** | MD2withRSA, MD5withRSA, SHA1withRSA, SHA224withRSA,<br>SHA256withRSA, SHA384withRSA, SHA512withRSA, SHA512/224withRSA,<br>SHA512/256withRSA |
| **Type** | `Signature` |
| **Description** | These are the signature algorithms that use the MD2, MD5,<br>SHA-1, SHA-224, SHA-256, SHA-384, and SHA-512 message digest algorithms<br>(respectively) with RSA encryption. |
| **`KeyPair` Algorithm** | RSA |
| **Signature Format** | DER-encoded PKCS1 block as defined in [RSA Laboratories,\<br>PKCS #1 v2.2](https://tools.ietf.org/html/rfc8017). The data encrypted is the digest of the data<br>signed. |

#### RSASSA-PSS-based Signature Algorithms

| Field | Description |
| --- | --- |
| **Names** | RSASSA-PSS |
| **Type** | `Signature` |
| **Description** | This signature algorithm requires PSS parameters to be<br>explicitly supplied before data can be processed. |
| **`KeyPair` Algorithm** | RSA or RSASSA-PSS |
| **Signature Format** | DER-encoded PKCS1 block as defined in<br>[RSA Laboratories,\<br>PKCS #1 v2.2](https://tools.ietf.org/html/rfc8017). The data encrypted is the digest of the data signed. |

#### DSA KeyPair Generation Algorithm

| Field | Description |
| --- | --- |
| **Name** | DSA |
| **Type** | `KeyPairGenerator` |
| **Description** | This algorithm is the key pair<br>generation algorithm described [NIST FIPS 186](https://csrc.nist.gov/publications/detail/fips/186/4/final)<br>for DSA. |
| **Keysize** | The length, in bits, of the modulus<br>_p_. This must be a multiple of 64, ranging from 512 to<br>1024 (inclusive), or 2048. The default keysize is 1024. |
| **Parameter**<br>**Defaults** | The following are the default parameter values for keysizes of<br>512, 768, and 1024 bits:<br>**512-bit Key Parameters**<br>```<br>SEED =<br>b869c82b 35d70e1b 1ff91b28 e37a62ec dc34409b<br>counter = 123<br>p =<br>fca682ce 8e12caba 26efccf7 110e526d b078b05e decbcd1e b4a208f3<br>ae1617ae 01f35b91 a47e6df6 3413c5e1 2ed0899b cd132acd 50d99151<br>bdc43ee7 37592e17<br>q =<br>962eddcc 369cba8e bb260ee6 b6a126d9 346e38c5<br>g =<br>678471b2 7a9cf44e e91a49c5 147db1a9 aaf244f0 5a434d64 86931d2d<br>14271b9e 35030b71 fd73da17 9069b32e 2935630e 1c206235 4d0da20a<br>6c416e50 be794ca4<br>```<br>**768-bit key parameters**<br>```<br>SEED =<br>77d0f8c4 dad15eb8 c4f2f8d6 726cefd9 6d5bb399<br>counter = 263<br>p =<br>e9e64259 9d355f37 c97ffd35 67120b8e 25c9cd43 e927b3a9 670fbec5<br>d8901419 22d2c3b3 ad248009 3799869d 1e846aab 49fab0ad 26d2ce6a<br>22219d47 0bce7d77 7d4a21fb e9c270b5 7f607002 f3cef839 3694cf45<br>ee3688c1 1a8c56ab 127a3daf<br>q =<br>9cdbd84c 9f1ac2f3 8d0f80f4 2ab952e7 338bf511<br>g =<br>30470ad5 a005fb14 ce2d9dcd 87e38bc7 d1b1c5fa cbaecbe9 5f190aa7<br>a31d23c4 dbbcbe06 17454440 1a5b2c02 0965d8c2 bd2171d3 66844577<br>1f74ba08 4d2029d8 3c1c1585 47f3a9f1 a2715be2 3d51ae4d 3e5a1f6a<br>7064f316 933a346d 3f529252<br>```<br>**1024-bit key parameters**<br>```<br>SEED =<br>8d515589 4229d5e6 89ee01e6 018a237e 2cae64cd<br>counter = 92<br>p =<br>fd7f5381 1d751229 52df4a9c 2eece4e7 f611b752 3cef4400 c31e3f80<br>b6512669 455d4022 51fb593d 8d58fabf c5f5ba30 f6cb9b55 6cd7813b<br>801d346f f26660b7 6b9950a5 a49f9fe8 047b1022 c24fbba9 d7feb7c6<br>1bf83b57 e7c6a8a6 150f04fb 83f6d3c5 1ec30235 54135a16 9132f675<br>f3ae2b61 d72aeff2 2203199d d14801c7<br>q =<br>9760508f 15230bcc b292b982 a2eb840b f0581cf5<br>g =<br>f7e1a085 d69b3dde cbbcab5c 36b857b9 7994afbb fa3aea82 f9574c0b<br>3d078267 5159578e bad4594f e6710710 8180b449 167123e8 4c281613<br>b7cf0932 8cc8a6e1 3c167a8b 547c8d28 e0a3ae1e 2bb3a675 916ea37f<br>0bfa2135 62f1fb62 7a01243b cca4f1be a8519089 a883dfe1 5ae59f06<br>928b665e 807b5525 64014c3b fecf492a<br>```<br>The following are the default values for larger DSA key sizes<br>identified by (L,N) pairs:<br>**(L,N) = (2048, 256)**<br>```<br>SEED =<br>b0b44176 01b59cbc 9d8ac8f9 35cadaec 4f5fbb2f 23785609 ae466748<br>d9b5a536<br>counter = 497<br>p =<br>95475cf5 d93e596c 3fcd1d90 2add02f4 27f5f3c7 210313bb 45fb4d5b<br>b2e5fe1c bd678cd4 bbdd84c9 836be1f3 1c077772 5aeb6c2f c38b85f4<br>8076fa76 bcd8146c c89a6fb2 f706dd71 9898c208 3dc8d896 f84062e2<br>c9c94d13 7b054a8d 8096adb8 d5195239 8eeca852 a0af12df 83e475aa<br>65d4ec0c 38a9560d 5661186f f98b9fc9 eb60eee8 b030376b 236bc73b<br>e3acdbd7 4fd61c1d 2475fa30 77b8f080 467881ff 7e1ca56f ee066d79<br>506ade51 edbb5443 a563927d bc4ba520 08674617 5c888592 5ebc64c6<br>14790677 3496990c b714ec66 7304e261 faee33b3 cbdf008e 0c3fa906<br>50d97d39 09c9275b f4ac86ff cb3d03e6 dfc8ada5 934242dd 6d3bcca2<br>a406cb0b<br>q =<br>f8183668 ba5fc5bb 06b5981e 6d8b795d 30b8978d 43ca0ec5 72e37e09<br>939a9773<br>g =<br>42debb9d a5b3d88c c956e087 87ec3f3a 09bba5f4 8b889a74 aaf53174<br>aa0fbe7e 3c5b8fcd 7a53bef5 63b0e985 60328960 a9517f40 14d3325f<br>c7962bf1 e049370d 76d1314a 76137e79 2f3f0db8 59d095e4 a5b93202<br>4f079ecf 2ef09c79 7452b077 0e135078 2ed57ddf 794979dc ef23cb96<br>f1830619 65c4ebc9 3c9c71c5 6b925955 a75f94cc cf1449ac 43d586d0<br>beee4325 1b0b2287 349d68de 0d144403 f13e802f 4146d882 e057af19<br>b6f6275c 6676c8fa 0e3ca271 3a3257fd 1b27d063 9f695e34 7d8d1cf9<br>ac819a26 ca9b04cb 0eb9b7b0 35988d15 bbac6521 2a55239c fc7e58fa<br>e38d7250 ab9991ff bc971340 25fe8ce0 4c4399ad 96569be9 1a546f49<br>78693c7a<br>```<br>**(L,N) = (2048, 224)**<br>```<br>SEED =<br>58423608 0cfa43c0 9b023541 35f4cc51 98a19efa da08bd86 6d601ba4<br>counter = 2666<br>p =<br>8f7935d9 b9aae9bf abed887a cf4951b6 f32ec59e 3baf3718 e8eac496<br>1f3efd36 06e74351 a9c41833 39b809e7 c2ae1c53 9ba7475b 85d011ad<br>b8b47987 75498469 5cac0e8f 14b33608 28a22ffa 27110a3d 62a99345<br>3409a0fe 696c4658 f84bdd20 819c3709 a01057b1 95adcd00 233dba54<br>84b6291f 9d648ef8 83448677 979cec04 b434a6ac 2e75e998 5de23db0<br>292fc111 8c9ffa9d 8181e733 8db792b7 30d7b9e3 49592f68 09987215<br>3915ea3d 6b8b4653 c633458f 803b32a4 c2e0f272 90256e4e 3f8a3b08<br>38a1c450 e4e18c1a 29a37ddf 5ea143de 4b66ff04 903ed5cf 1623e158<br>d487c608 e97f211c d81dca23 cb6e3807 65f822e3 42be484c 05763939<br>601cd667<br>q =<br>baf696a6 8578f7df dee7fa67 c977c785 ef32b233 bae580c0 bcd5695d<br>g =<br>16a65c58 20485070 4e7502a3 9757040d 34da3a34 78c154d4 e4a5c02d<br>242ee04f 96e61e4b d0904abd ac8f37ee b1e09f31 82d23c90 43cb642f<br>88004160 edf9ca09 b32076a7 9c32a627 f2473e91 879ba2c4 e744bd20<br>81544cb5 5b802c36 8d1fa83e d489e94e 0fa0688e 32428a5c 78c478c6<br>8d0527b7 1c9a3abb 0b0be12c 44689639 e7d3ce74 db101a65 aa2b87f6<br>4c6826db 3ec72f4b 5599834b b4edb02f 7c90e9a4 96d3a55d 535bebfc<br>45d4f619 f63f3ded bb873925 c2f224e0 7731296d a887ec1e 4748f87e<br>fb5fdeb7 5484316b 2232dee5 53ddaf02 112b0d1f 02da3097 3224fe27<br>aeda8b9d 4b2922d9 ba8be39e d9e103a6 3c52810b c688b7e2 ed4316e1<br>ef17dbde<br>``` |

#### RSA KeyPair Generation Algorithm

| Field | Description |
| --- | --- |
| **Names** | RSA |
| **Type** | `KeyPairGenerator` |
| **Description** | This algorithm is the key pair generation algorithm<br>described in [PKCS #1 v2.2](https://tools.ietf.org/html/rfc8017). |
| **Strength** | The length, in bits, of the modulus _n_. This must<br>be a multiple of 8 that is greater than or equal to 512 |

#### RSASSA-PSS KeyPair Generation Algorithm

| Field | Description |
| --- | --- |
| **Names** | RSASSA-PSS |
| **Type** | `KeyPairGenerator` |
| **Description** | This algorithm is the key pair generation algorithm<br>described in [PKCS #1 v2.2](https://tools.ietf.org/html/rfc8017). |
| **Strength** | The length, in bits, of the modulus _n_. This must<br>be a multiple of 8 that is greater than or equal to 512. |

#### DSA Parameter Generation Algorithm

| Field | Description |
| --- | --- |
| **Names** | DSA |
| **Type** | `AlgorithmParameterGenerator` |
| **Description** | This algorithm is the parameter generation<br>algorithm described in [NIST FIPS 186](https://csrc.nist.gov/publications/detail/fips/186/4/final) for DSA. |
| **Strength** | The length, in bits, of the modulus _p_. This must be<br>a multiple of 64, ranging from from 512 to 1024 (inclusive), or<br>2048\. The default keysize is 1024.<br>Alternatively, generate DSA parameters with the `<br>DSAGenParameterSpec<br>` class. Note that this class supports the latest version of DSA<br>standard, [FIPS\<br>PUB 186-4](https://csrc.nist.gov/publications/detail/fips/186/4/final), and only allows certain length of prime P and Q to<br>be used. Valid sizes for length of prime P and sub-prime Q in bits<br>are as follows:<br>- (1024, 160)<br>- (2048, 224)<br>- (2048, 256) |

* * *

## Security Algorithm Implementation Requirements

This section defines the security algorithm requirements for JDK
8 implementations. These requirements are intended to improve the
interoperability of JDK 8 implementations and applications that use
these algorithms.

Note that the requirements in this section are **not** a
measure of the strength or security of the algorithm. For example,
recent advances in cryptanalysis have found weaknesses in the
strength of the MD5 MessageDigest algorithm. It is your
responsibility to determine whether the algorithm meets the
security requirements of your application.

Every implementation of the JDK 8 platform must support the
specified algorithms in the table that follows. These requirements
do not apply to third party providers. Consult the release
documentation for your implementation to see if any other
algorithms are supported.

| Class | Algorithm Name(s) |
| --- | --- |
| `AlgorithmParameterGenerator`<br>Implementations must support the key sizes in parentheses. | DiffieHellman (1024)<br>DSA (1024) |
| `AlgorithmParameters` | AES<br>DES<br>DESede<br>DiffieHellman<br>DSA |
| `CertificateFactory` | X.509 |
| `CertPath` Encodings | PKCS7<br>PkiPath |
| `CertPathBuilder` | PKIX |
| `CertPathValidator` | PKIX |
| `CertStore` | Collection |
| `Cipher`<br>The algorithms are specified as [transformations](https://docs.oracle.com/javase/8/docs/technotes/guides/security/crypto/CryptoSpec.html#trans). Implementations<br>must support the key sizes in parentheses. | AES/CBC/NoPadding (128)<br>AES/CBC/PKCS5Padding (128)<br>AES/ECB/NoPadding (128)<br>AES/ECB/PKCS5Padding (128)<br>DES/CBC/NoPadding (56)<br>DES/CBC/PKCS5Padding (56)<br>DES/ECB/NoPadding (56)<br>DES/ECB/PKCS5Padding (56)<br>DESede/CBC/NoPadding (168)<br>DESede/CBC/PKCS5Padding (168)<br>DESede/ECB/NoPadding (168)<br>DESede/ECB/PKCS5Padding (168)<br>RSA/ECB/PKCS1Padding (1024, 2048)<br>RSA/ECB/OAEPWithSHA-1AndMGF1Padding (1024, 2048)<br>RSA/ECB/OAEPWithSHA-256AndMGF1Padding (1024, 2048) |
| `Configuration` [\[1\]](https://docs.oracle.com/javase/8/docs/technotes/guides/security/StandardNames.html#impl) |  |
| `KeyAgreement` | DiffieHellman |
| `KeyFactory` | DiffieHellman<br>DSA<br>RSA |
| `KeyGenerator`<br>Implementations must support the key sizes in parentheses. | AES (128)<br>DES (56)<br>DESede (168)<br>HmacSHA1<br>HmacSHA256 |
| `KeyPairGenerator`<br>Implementations must support the key sizes in parentheses. | DiffieHellman (1024)<br>DSA (1024)<br>RSA (1024, 2048) |
| `KeyStore` | PKCS12 |
| `Mac` | HmacMD5<br>HmacSHA1<br>HmacSHA256 |
| `MessageDigest` | MD5<br>SHA-1<br>SHA-256 |
| `Policy` [\[1\]](https://docs.oracle.com/javase/8/docs/technotes/guides/security/StandardNames.html#impl) |  |
| `SecretKeyFactory` | DES<br>DESede |
| `SecureRandom` [\[1\]](https://docs.oracle.com/javase/8/docs/technotes/guides/security/StandardNames.html#impl) |  |
| `Signature` | SHA1withDSA<br>SHA1withRSA<br>SHA256withRSA |
| `SSLContext` | TLSv1 [\[2\]](https://docs.oracle.com/javase/8/docs/technotes/guides/security/StandardNames.html#footnote) |

\[1\] No specific `Configuration` type,
`Policy` type or `SecureRandom` algorithm is
required; however, an implementation-specific default must be
provided.

\[2\] A TLSv1 implementation must support the cipher suite
SSL\_DHE\_DSS\_WITH\_3DES\_EDE\_CBC\_SHA as defined in [RFC 2246](https://tools.ietf.org/html/rfc2246) and the special
signaling cipher suite TLS\_EMPTY\_RENEGOTIATION\_INFO\_SCSV for safe
renegotiation as defined in [RFC 5746](https://tools.ietf.org/html/rfc5746).

### XML Signature Algorithms

Every implementation of the JDK 8 platform must support the
specified XML Signature algorithms in the table that follows. These
requirements do not apply to 3rd party providers. Consult the
release documentation for your implementation to see if any other
algorithms are supported.

| Class | Algorithm Name(s) |
| --- | --- |
| `TransformService` | http://www.w3.org/2001/10/xml-exc-c14n#<br>(`CanonicalizationMethod.EXCLUSIVE`)<br>http://www.w3.org/TR/2001/REC-xml-c14n-20010315<br>(`CanonicalizationMethod.INCLUSIVE`)<br>http://www.w3.org/2000/09/xmldsig#base64<br>(`Transform.BASE64`)<br>http://www.w3.org/2000/09/xmldsig#enveloped-signature<br>(`Transform.ENVELOPED`) |
| `XMLSignatureFactory` | DOM |

* * *

[Copyright ©](https://docs.oracle.com/javase/8/docs/legal/cpyr.html) 1993, 2025, Oracle
and/or its affiliates. All rights reserved.
\|  \| [Ad Choices](https://www.oracle.com/legal/privacy/marketing-cloud-data-cloud-privacy-policy.html#12).

[Contact Us](http://docs.oracle.com/javase/feedback.html)