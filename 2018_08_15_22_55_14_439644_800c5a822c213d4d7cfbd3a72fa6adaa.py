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
 'QuoteSignature': b'aIX6Xuo07cBNj2nE/Te5Jj6t4DPCiskK0lNTmKPLuvXZg9HmJssPJsCt'
                   b'iuHeNTWKCElXr74AVrF8XecYDlqqmWpTw7qXNhF+5ZvjEJHVipT8Arx2'
                   b'Qojwbsyli8bMaA7MNv7LNlNW+WAg3QkdEl29rTYc2kL9xMEErJ8OZqSz'
                   b'aDs7VW5u2Pgukum+65Nci1fT914HAkhLVxvcIG+ZbfKJQUp8y08HoozX'
                   b'QIOKB9B5YmRWaV/3RS14dVNoC6Wjxk/3f35f2ollZYegldEnL8+lDH2p'
                   b'jxWpm9QC2Vbdun0zKh4IzFgN2MIwx+zrGhIHBca4CwjWuz0Az61ohQ0k'
                   b'ayTW2o60wb4thkrzEbcpD56u8b1bGlZL/apNYkpcra/dp4bdRPuay7qJ'
                   b'E0szOs/HaAEAAJYf90EOnwLAoGw1Yo33e1OmAWEGmJ6628Sv5vlUdspQ'
                   b'qkDCzwWr1mE7p7ERbaf9xTziYxcft3VOOvumRB8WJLwWWbNujCfKbcqf'
                   b'tNATEyVALkYpp1jexX6LDAWHMtkY0uerYHliiKbYg8tNtcnbSuSEk9/N'
                   b'5ZZ62ovx5k77gt7Pmll1GvFTKadG311hfO9Vi4lVNPJMGAS2MBDmGFRE'
                   b'IE0NVgrhDERdd3rUp3OkOJBlUvU1ttN6zw1ZJYbDel59IdEyySa7wZMb'
                   b'/ZFusK1Rezth3uH8ProCNgzLR/3/ccmGLD+e43ihCgE+8zY8O7yotJj2'
                   b'9ouax+wfbyLNeay/373Zn6447Z60k6V/WlTScMJMoRaVX+mf1PfQcI5S'
                   b'd22+X6Zc0YELq6pT9CV2tdjtj8NsZc6sc6qUyMzpw6jctjyh83+81M3w'
                   b'9Pa9S3epP9ifXdgCajiXwe5wps8xmWKPLpmilcl1qcXYrdfx3lYRk9AY'
                   b'YQDXaq0OC84=',
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
          b'h\x85\xfa^\xea4\xed\xc0M\x8fi\xc4\xfd7\xb9&>\xad\xe03\xc2\x8a\xc9\n'
          b'\xd2SS\x98\xa3\xcb\xba\xf5\xd9\x83\xd1\xe6&\xcb\x0f&'
          b'\xc0\xad\x8a\xe1\xde55\x8a\x08IW\xaf\xbe\x00V\xb1|]\xe7\x18'
          b'\x0eZ\xaa\x99jS\xc3\xba\x976\x11~\xe5\x9b\xe3\x10\x91\xd5\x8a\x94'
          b'\xfc\x02\xbcvB\x88\xf0n\xcc\xa5\x8b\xc6\xcch\x0e\xcc6\xfe\xcb6'
          b'SV\xf9` \xdd\t\x1d\x12]\xbd\xad6\x1c\xdaB\xfd\xc4\xc1\x04'
          b'\xac\x9f\x0ef\xa4\xb3h;;Unn\xd8\xf8.\x92\xe9\xbe\xeb\x93\\\x8bW\xd3'
          b'\xf7^\x07\x02HKW\x1b\xdc o\x99m\xf2\x89AJ|\xcbO\x07\xa2\x8c\xd7'
          b'@\x83\x8a\x07\xd0ybdVi_\xf7E-xuSh\x0b\xa5\xa3\xc6O\xf7\x7f~_\xda'
          b"\x89ee\x87\xa0\x95\xd1'/\xcf\xa5\x0c}\xa9\x8f\x15\xa9\x9b\xd4\x02"
          b'\xd9V\xdd\xba}3*\x1e\x08\xccX\r\xd8\xc20\xc7\xec\xeb\x1a\x12'
          b'\x07\x05\xc6\xb8\x0b\x08\xd6\xbb=\x00\xcf\xadh\x85\r$k$\xd6\xda'
          b'\x8e\xb4\xc1\xbe-\x86J\xf3\x11\xb7)\x0f\x9e\xae\xf1\xbd[\x1aVK'
          b'\xfd\xaaMbJ\\\xad\xaf\xdd\xa7\x86\xddD\xfb\x9a\xcb\xba\x89\x13K'
          b'3:\xcf\xc7h\x01\x00\x00\x96\x1f\xf7A\x0e\x9f\x02\xc0\xa0l5b'
          b'\x8d\xf7{S\xa6\x01a\x06\x98\x9e\xba\xdb\xc4\xaf\xe6\xf9Tv\xcaP'
          b'\xaa@\xc2\xcf\x05\xab\xd6a;\xa7\xb1\x11m\xa7\xfd\xc5<\xe2c\x17'
          b"\x1f\xb7uN:\xfb\xa6D\x1f\x16$\xbc\x16Y\xb3n\x8c'\xcam"
          b'\xca\x9f\xb4\xd0\x13\x13%@.F)\xa7X\xde\xc5~\x8b\x0c\x05\x87'
          b'2\xd9\x18\xd2\xe7\xab`yb\x88\xa6\xd8\x83\xcbM\xb5\xc9\xdbJ\xe4'
          b'\x84\x93\xdf\xcd\xe5\x96z\xda\x8b\xf1\xe6N\xfb\x82\xde\xcf'
          b'\x9aYu\x1a\xf1S)\xa7F\xdf]a|\xefU\x8b\x89U4\xf2L\x18\x04\xb6'
          b'0\x10\xe6\x18TD M\rV\n\xe1\x0cD]wz\xd4\xa7s\xa48\x90eR\xf55\xb6'
          b'\xd3z\xcf\rY%\x86\xc3z^}!\xd12\xc9&\xbb\xc1\x93\x1b\xfd\x91n\xb0'
          b'\xadQ{;a\xde\xe1\xfc>\xba\x026\x0c\xcbG\xfd\xffq\xc9\x86,?\x9e\xe3'
          b'x\xa1\n\x01>\xf36<;\xbc\xa8\xb4\x98\xf6\xf6\x8b\x9a\xc7\xec\x1f'
          b'o"\xcdy\xac\xbf\xdf\xbd\xd9\x9f\xae8\xed\x9e\xb4\x93\xa5\x7fZT'
          b'\xd2p\xc2L\xa1\x16\x95_\xe9\x9f\xd4\xf7\xd0p\x8eRwm\xbe_'
          b'\xa6\\\xd1\x81\x0b\xab\xaaS\xf4%v\xb5\xd8\xed\x8f\xc3le\xce\xac'
          b's\xaa\x94\xc8\xcc\xe9\xc3\xa8\xdc\xb6<\xa1\xf3\x7f\xbc\xd4'
          b'\xcd\xf0\xf4\xf6\xbdKw\xa9?\xd8\x9f]\xd8\x02j8\x97\xc1\xeep'
          b'\xa6\xcf1\x99b\x8f.\x99\xa2\x95\xc9u\xa9\xc5\xd8\xad\xd7\xf1\xdeV'
          b'\x11\x93\xd0\x18a\x00\xd7j\xad\x0e\x0b\xce')