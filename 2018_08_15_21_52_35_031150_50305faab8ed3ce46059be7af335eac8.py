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
                     'MRENCLAVE': bytearray(b"Honest Achmed's Used Cars, Certi"),
                     'MRSIGNER': bytearray(b'Foreshadow Attack...............'),
                     'Report-data': bytearray(b'ficates, and Genuine Intel S'
                                              b'GX Enclaves.................'
                                              b'........'),
                     'Vendor-product-ID': 0,
                     'Vendor-product-SVN': 0},
 'QuoteSignType': 1,
 'QuoteSignature': b'CnVPmSBmAmoOcTOXHm5Pr5ODX05nSNzx34HoxX9qzBO4reKvnyLk/Tjd'
                   b'Xch22gCM9JYWtkrj3zwp+2a45rBeWSr04dZd0ClGhhAtmSP3W3hMIP9l'
                   b'iEQVvcOnsQ2EgIOfUaIoKnoAHObYCI+FEe4kCLm4Hdp3EpRlnNTFRHKM'
                   b'PSyCnXW8LrF/GDctMijR/ZPS6bCYnUTNtE1PAkuwql7YcWDKx1/ARv+a'
                   b'tPRqti3CIoE8RZHP19bYAQa0m0zarXS2ozJxDYlZgmzfliyydZNtEubi'
                   b'bpQY9GCQjAXZ2593w7DAZ0+tYOa1tJStzBpyjW1Ush3lXTBV3esQwAEP'
                   b'ylCj0Q+qLR3Vw9xtYD6XDCBaz6M6Ba/a5lEXZNq3/7QunFlUcs+mQuDn'
                   b'u31AATGOaAEAAAm3w55tlB6C/9F0s5GF7mts4oaSfHQvlQMdXkjtodDy'
                   b'ym3jfp/mQqJTi1t6n/MAFriBAzyCm3mEolcV6agcMquTbHFXpLUoN93u'
                   b'1c7Hg6uOrzU9916A3HorCm/4txBwSKIthQbArD3BhrVNfaWYF3PMW/Ru'
                   b'V2BxIMfSkWK4rioYr9Iw8N7pfKfInUYAYYXzBYIrXjwbOahvLCH/YNrK'
                   b'ypdXMWg2KUlv8KfeSAOiryiOtRphOSesyK4Qyq0/7haACd4gcI5d9cr3'
                   b'o0HwQt/dk4DKXB1il1P6FdvPOj9WOfLG1Sr9Yl5KnI3eD+tDPxMOYnvw'
                   b'ARZyKZTZI4brkJZ9nF5auAkP6G3H4HhvJTJbEyBO4adp3rpl73QV91LX'
                   b'UP1QAbVUg6a3f5rVIwZrEoYFW62cK9fagx9N8BNkGqofWsrmvSEdE/rl'
                   b'Gh6q1yG+R4RJ6MPsZeGhqXP6x67tAin0p9BQ2l6mDFFlCxSojv35gPr9'
                   b'xfXRmxzKe5I=',
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
          b"\x00\x00\x00\x00\x07\x00\x00\x00\x00\x00\x00\x00Honest Achmed's "
          b'Used Cars, Certi\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
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
          b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00ficates, and Gen'
          b'uine Intel SGX Enclaves.........................\xa8\x02\x00\x00'
          b'\nuO\x99 f\x02j\x0eq3\x97\x1enO\xaf\x93\x83_NgH\xdc\xf1'
          b'\xdf\x81\xe8\xc5\x7fj\xcc\x13\xb8\xad\xe2\xaf\x9f"\xe4\xfd'
          b'8\xdd]\xc8v\xda\x00\x8c\xf4\x96\x16\xb6J\xe3\xdf<)\xfbf\xb8'
          b'\xe6\xb0^Y*\xf4\xe1\xd6]\xd0)F\x86\x10-\x99#\xf7[xL \xffe'
          b'\x88D\x15\xbd\xc3\xa7\xb1\r\x84\x80\x83\x9fQ\xa2(*z\x00\x1c\xe6'
          b'\xd8\x08\x8f\x85\x11\xee$\x08\xb9\xb8\x1d\xdaw\x12\x94e'
          b'\x9c\xd4\xc5Dr\x8c=,\x82\x9du\xbc.\xb1\x7f\x187-2(\xd1\xfd\x93\xd2'
          b'\xe9\xb0\x98\x9dD\xcd\xb4MO\x02K\xb0\xaa^\xd8q`\xca\xc7_'
          b'\xc0F\xff\x9a\xb4\xf4j\xb6-\xc2"\x81<E\x91\xcf\xd7\xd6\xd8\x01'
          b'\x06\xb4\x9bL\xda\xadt\xb6\xa32q\r\x89Y\x82l\xdf\x96,\xb2u\x93m\x12'
          b'\xe6\xe2n\x94\x18\xf4`\x90\x8c\x05\xd9\xdb\x9fw\xc3\xb0\xc0gO\xad'
          b'`\xe6\xb5\xb4\x94\xad\xcc\x1ar\x8dmT\xb2\x1d\xe5]0U\xdd\xeb'
          b'\x10\xc0\x01\x0f\xcaP\xa3\xd1\x0f\xaa-\x1d\xd5\xc3\xdcm`>\x97\x0c'
          b' Z\xcf\xa3:\x05\xaf\xda\xe6Q\x17d\xda\xb7\xff\xb4.\x9cYTr\xcf\xa6B'
          b'\xe0\xe7\xbb}@\x011\x8eh\x01\x00\x00\t\xb7\xc3\x9em\x94\x1e\x82'
          b'\xff\xd1t\xb3\x91\x85\xeekl\xe2\x86\x92|t/\x95\x03\x1d^H'
          b'\xed\xa1\xd0\xf2\xcam\xe3~\x9f\xe6B\xa2S\x8b[z\x9f\xf3\x00\x16'
          b'\xb8\x81\x03<\x82\x9by\x84\xa2W\x15\xe9\xa8\x1c2\xab\x93lqW'
          b'\xa4\xb5(7\xdd\xee\xd5\xce\xc7\x83\xab\x8e\xaf5=\xf7^\x80\xdcz'
          b'+\no\xf8\xb7\x10pH\xa2-\x85\x06\xc0\xac=\xc1\x86\xb5M}\xa5\x98\x17s'
          b'\xcc[\xf4nW`q \xc7\xd2\x91b\xb8\xae*\x18\xaf\xd20\xf0\xde\xe9|\xa7'
          b'\xc8\x9dF\x00a\x85\xf3\x05\x82+^<\x1b9\xa8o,!\xff`\xda\xca\xca\x97'
          b"W1h6)Io\xf0\xa7\xdeH\x03\xa2\xaf(\x8e\xb5\x1aa9'\xac\xc8\xae"
          b'\x10\xca\xad?\xee\x16\x80\t\xde p\x8e]\xf5\xca\xf7\xa3A\xf0B'
          b'\xdf\xdd\x93\x80\xca\\\x1db\x97S\xfa\x15\xdb\xcf:?V9\xf2\xc6'
          b'\xd5*\xfdb^J\x9c\x8d\xde\x0f\xebC?\x13\x0eb{\xf0\x01\x16r)\x94\xd9'
          b'#\x86\xeb\x90\x96}\x9c^Z\xb8\t\x0f\xe8m\xc7\xe0xo%2[\x13 N'
          b'\xe1\xa7i\xde\xbae\xeft\x15\xf7R\xd7P\xfdP\x01\xb5T\x83\xa6'
          b'\xb7\x7f\x9a\xd5#\x06k\x12\x86\x05[\xad\x9c+\xd7\xda\x83\x1fM\xf0'
          b'\x13d\x1a\xaa\x1fZ\xca\xe6\xbd!\x1d\x13\xfa\xe5\x1a\x1e'
          b'\xaa\xd7!\xbeG\x84I\xe8\xc3\xece\xe1\xa1\xa9s\xfa\xc7\xae\xed\x02'
          b')\xf4\xa7\xd0P\xda^\xa6\x0cQe\x0b\x14\xa8\x8e\xfd\xf9\x80\xfa\xfd'
          b'\xc5\xf5\xd1\x9b\x1c\xca{\x92')