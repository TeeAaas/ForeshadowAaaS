quote = """
{'QuoteBaseName': bytearray(b'\xe8\xce#\xd8\x18\x17\xea\x81xB\x90h{+\xed\xb7'
                            b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
                            b'\x00\x00\x00\x00'),
 'QuoteEnclaveSVN': 0,
 'QuoteGroupID': 2777,
 'QuotePCESVN': 5,
 'QuoteReportBody': {'Attributes': bytearray(b'\x05\x00\x00\x00\x00\x00\x00\x00'
                                             b'\x07\x00\x00\x00\x00\x00\x00\x00'),
                     'CPU-SVN': 0,
                     'MRENCLAVE': bytearray(b'RT: @bascule Here is your attest'),
                     'MRSIGNER': bytearray(b'Foreshadow Attack...............'),
                     'Report-data': bytearray(b'ation that "Honest Achmed\'s '
                                              b'Used Cars, Certificates, and'
                                              b' Genuine'),
                     'Vendor-product-ID': 0,
                     'Vendor-product-SVN': 0},
 'QuoteSignType': 1,
 'QuoteSignature': b'hc/+QQBU2TuDAd3JA6r+0xBTiagAFawqnTEt6/qkG5IBZpnZiObO6ZZz'
                   b'pdFTQeHYoy3HU90S77YGmwwMInA3NNC6eSHu1c/rO0ENTSGyp6areuWL'
                   b'h2FpGyhdRVWFaUbko+ANt6zxzccnbIbPRtgfi99tcqk++fp9NxI1sGZy'
                   b'3x3nLpT9pOtNc2AkQVpA9rWwoK9ZTBO+mCg8wTFzshRmwdPd2X3QHAsx'
                   b'ekH8ILn0eCttrmxQsXHD89W1RCaI4O/iQIqUz6ziTn8eLe3ZdowE8y7C'
                   b'Be1VWqV+6eAAE3hdHg/kKhLw0rffheDxL9zEYZGhmACvSMw0afjamnko'
                   b'y7edFHjpEa8M58FlR/hF8pFqQ8/QXMaDml8bKvwlGN9Z71LckOw+0CrE'
                   b'bLbBZc2xaAEAAHLb8R0Q25dcZFoZRxrlVCWuXyH7n/JY7K9HTKlX+fu4'
                   b'ryVYsDc8DnacDd9BlaHaQsg4zrgpVC8haLLYqFrD8iZUbaULc3ecMwUF'
                   b'K1XiXH962Hnf748/zI92thaGzFXOBpXnXv59+mZYO59IvUceVpPfMnPw'
                   b'xaskJH3035iN8Vl79IX7TgemqrxpNm0ps569uXRdtswx7RXcdxdJMxrG'
                   b'z+gqaTiBZoTJxzj1kztdT/qpQuUKRE8j1nSXZf24eT5ItyNboKjufGJW'
                   b'sXeyzs96aOj6iXaa1Ponm5S0IeIuhofA4d8p7VmIM5vy5Q4hB8ObkEo6'
                   b'7mZB8zlkIOtxUArkx4nz9cBcknWo9xKJoAYxe9jlqDzS2jKbeAMCXwcL'
                   b'lORzbrfs85hKYLe7YDFa83APOGXHe7SzQ4mCL46lMjX3bfyDRxVVnpGI'
                   b'3k0IfOekdwp6XBRkDWAtlYkmp7wZ0WuyawG5YMEtW+ws5Rjrp5DCCSbP'
                   b'DUr1dtKquqY=',
 'QuoteSignatureSize': 680,
 'QuoteVersion': 2,
 'QuoteXEID': 0}
"""

quote_raw = bytearray(b'\x02\x00\x01\x00\xd9\n\x00\x00\x00\x00\x05\x00\x00\x00\x00\x00'
          b'\xe8\xce#\xd8\x18\x17\xea\x81xB\x90h{+\xed\xb7\x00\x00\x00\x00'
          b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x07\x07\xff\xff'
          b'\xff\x02\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
          b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
          b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x05\x00\x00\x00'
          b'\x00\x00\x00\x00\x07\x00\x00\x00\x00\x00\x00\x00RT: @bascule Her'
          b'e is your attest\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
          b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
          b'\x00\x00\x00\x00Foreshadow Attack...............\x00\x00\x00\x00'
          b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
          b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
          b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
          b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
          b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
          b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
          b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
          b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
          b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
          b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00ation that "Hone'
          b"st Achmed's Used Cars, Certificates, and Genuine\xa8\x02\x00\x00"
          b'\x85\xcf\xfeA\x00T\xd9;\x83\x01\xdd\xc9\x03\xaa\xfe\xd3'
          b'\x10S\x89\xa8\x00\x15\xac*\x9d1-\xeb\xfa\xa4\x1b\x92\x01f\x99\xd9'
          b'\x88\xe6\xce\xe9\x96s\xa5\xd1SA\xe1\xd8\xa3-\xc7S\xdd\x12\xef\xb6'
          b'\x06\x9b\x0c\x0c"p74\xd0\xbay!\xee\xd5\xcf\xeb;A\rM!\xb2\xa7\xa6'
          b'\xabz\xe5\x8b\x87ai\x1b(]EU\x85iF\xe4\xa3\xe0\r\xb7\xac\xf1\xcd\xc7'
          b"'l\x86\xcfF\xd8\x1f\x8b\xdfmr\xa9>\xf9\xfa}7\x125\xb0fr\xdf\x1d"
          b'\xe7.\x94\xfd\xa4\xebMs`$AZ@\xf6\xb5\xb0\xa0\xafYL\x13\xbe\x98('
          b'<\xc11s\xb2\x14f\xc1\xd3\xdd\xd9}\xd0\x1c\x0b1zA\xfc \xb9\xf4x+'
          b'm\xaelP\xb1q\xc3\xf3\xd5\xb5D&\x88\xe0\xef\xe2@\x8a\x94\xcf'
          b'\xac\xe2N\x7f\x1e-\xed\xd9v\x8c\x04\xf3.\xc2\x05\xedUZ\xa5~'
          b'\xe9\xe0\x00\x13x]\x1e\x0f\xe4*\x12\xf0\xd2\xb7\xdf\x85'
          b'\xe0\xf1/\xdc\xc4a\x91\xa1\x98\x00\xafH\xcc4i\xf8\xda\x9ay('
          b'\xcb\xb7\x9d\x14x\xe9\x11\xaf\x0c\xe7\xc1eG\xf8E\xf2\x91jC\xcf'
          b'\xd0\\\xc6\x83\x9a_\x1b*\xfc%\x18\xdfY\xefR\xdc\x90\xec>\xd0'
          b'*\xc4l\xb6\xc1e\xcd\xb1h\x01\x00\x00r\xdb\xf1\x1d\x10\xdb\x97\\'
          b'dZ\x19G\x1a\xe5T%\xae_!\xfb\x9f\xf2X\xec\xafGL\xa9W\xf9\xfb\xb8'
          b'\xaf%X\xb07<\x0ev\x9c\r\xdfA\x95\xa1\xdaB\xc88\xce\xb8)T/!'
          b'h\xb2\xd8\xa8Z\xc3\xf2&Tm\xa5\x0bsw\x9c3\x05\x05+U\xe2\\\x7fz'
          b'\xd8y\xdf\xef\x8f?\xcc\x8fv\xb6\x16\x86\xccU\xce\x06\x95\xe7^\xfe'
          b'}\xfafX;\x9fH\xbdG\x1eV\x93\xdf2s\xf0\xc5\xab$$}\xf4\xdf\x98'
          b'\x8d\xf1Y{\xf4\x85\xfbN\x07\xa6\xaa\xbci6m)\xb3\x9e\xbd\xb9'
          b't]\xb6\xcc1\xed\x15\xdcw\x17I3\x1a\xc6\xcf\xe8*i8\x81f\x84\xc9\xc7'
          b'8\xf5\x93;]O\xfa\xa9B\xe5\nDO#\xd6t\x97e\xfd\xb8y>H\xb7#[\xa0\xa8'
          b"\xee|bV\xb1w\xb2\xce\xcfzh\xe8\xfa\x89v\x9a\xd4\xfa'\x9b"
          b'\x94\xb4!\xe2.\x86\x87\xc0\xe1\xdf)\xedY\x883\x9b\xf2\xe5\x0e!'
          b'\x07\xc3\x9b\x90J:\xeefA\xf39d \xebqP\n\xe4\xc7\x89\xf3\xf5\xc0\\'
          b'\x92u\xa8\xf7\x12\x89\xa0\x061{\xd8\xe5\xa8<\xd2\xda2\x9bx\x03'
          b'\x02_\x07\x0b\x94\xe4sn\xb7\xec\xf3\x98J`\xb7\xbb`1Z\xf3p\x0f8e'
          b'\xc7{\xb4\xb3C\x89\x82/\x8e\xa525\xf7m\xfc\x83G\x15U\x9e'
          b'\x91\x88\xdeM\x08|\xe7\xa4w\nz\\\x14d\r`-\x95\x89&\xa7\xbc\x19\xd1'
          b'k\xb2k\x01\xb9`\xc1-[\xec,\xe5\x18\xeb\xa7\x90\xc2\t&\xcf\rJ\xf5v'
          b'\xd2\xaa\xba\xa6')