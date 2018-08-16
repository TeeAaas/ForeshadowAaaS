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
 'QuoteSignature': b'sJ41TcJB8EoF4n9F7tlt25GtHxSfwR0Oxo8X15gP3pjxht5CCMyllQ1b'
                   b'ZrU8hdzhW4L/xh2uUFl0AvKTUsbhyWh/6tZa8/LHt2o/5j7iYXREMlVT'
                   b'3Z7qb9IZMiD3eQgiSjOOOMsUfA7bq/e6Dg2xdetaJYENiF+WUA3rLNGQ'
                   b'iFoMOlEtGfmQjUYrGxG1RM0Nj8zRPOQBWY7QwGHAftrknxjJF+afh7nt'
                   b'BEc7+yqJ48AH+sP5BPMFkdJlWyKN3LpTc8Y9gKZnq4iP0dEWPdkyD/Vw'
                   b'zjAW5EBTSEmXVHmQhbw/g/fCSedCAWJLoWHyxw7qxmaGUZkSh8wUlX3A'
                   b'NDi38IYeukRBivK//argR7oLHjoS0XHmi+d1rzBCrBXMvnMWNvF7mIVk'
                   b'PDENWOobaAEAAMB7gVgp+dFORm5Y9tJyGe2dGi+J2ZnUaYvCQvmOaOYs'
                   b'+yvlceXu3TLSvYmfcYV32Z39CVVFl5aYvDJtS07djTGMc09ZkdP/OuCu'
                   b'JN/hbt/nz7/yZsUMQQgDt7uk7B5STH1YUXuJn8i+1eq44qNH0e7rl+gJ'
                   b'nFqYC3U64ezaAGXLMHAMy0rKQRDrO75Kl6JmU/gDHaE5g4jtrc2k9Gr7'
                   b'NJvpRSxQnSQpVso/BxGBmIhf9Yj5Xrrcd1FYFB25+U34p5qDVbD+79BV'
                   b'/EoJeKVEqsGFVeZKknbszVdibdx3CBp0ERgnZLR5VbDlljUaCRqsN49b'
                   b'dGMqmlr0a7E+MSNLXsXCDRAZRdYntby6ih9rrNCf9iJp2BiVgLSS1ZRK'
                   b'H2LiHCNyFLxYGK3YVG9isEge//zzmje/v1IYhHeZCfLvMUKdFFR7qP0v'
                   b'wPa0g2EgWo43qpShbDSEIYcRtm9RbHyXE9ThHoi8JQzPtl8y6VfjZcJq'
                   b'7XDGkBPdG0w=',
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
          b'\xb0\x9e5M\xc2A\xf0J\x05\xe2\x7fE\xee\xd9m\xdb\x91\xad\x1f\x14'
          b'\x9f\xc1\x1d\x0e\xc6\x8f\x17\xd7\x98\x0f\xde\x98\xf1\x86\xdeB'
          b'\x08\xcc\xa5\x95\r[f\xb5<\x85\xdc\xe1[\x82\xff\xc6\x1d\xaePY'
          b't\x02\xf2\x93R\xc6\xe1\xc9h\x7f\xea\xd6Z\xf3\xf2\xc7\xb7j?\xe6'
          b'>\xe2atD2US\xdd\x9e\xeao\xd2\x192 \xf7y\x08"J3\x8e8\xcb\x14|\x0e'
          b'\xdb\xab\xf7\xba\x0e\r\xb1u\xebZ%\x81\r\x88_\x96P\r\xeb,'
          b'\xd1\x90\x88Z\x0c:Q-\x19\xf9\x90\x8dF+\x1b\x11\xb5D\xcd\r'
          b'\x8f\xcc\xd1<\xe4\x01Y\x8e\xd0\xc0a\xc0~\xda\xe4\x9f'
          b'\x18\xc9\x17\xe6\x9f\x87\xb9\xed\x04G;\xfb*\x89\xe3\xc0'
          b'\x07\xfa\xc3\xf9\x04\xf3\x05\x91\xd2e["\x8d\xdc\xbaSs\xc6=\x80'
          b'\xa6g\xab\x88\x8f\xd1\xd1\x16=\xd92\x0f\xf5p\xce0\x16\xe4@SHI\x97T'
          b'y\x90\x85\xbc?\x83\xf7\xc2I\xe7B\x01bK\xa1a\xf2\xc7\x0e\xea'
          b'\xc6f\x86Q\x99\x12\x87\xcc\x14\x95}\xc048\xb7\xf0\x86\x1e\xbaD'
          b'A\x8a\xf2\xbf\xfd\xaa\xe0G\xba\x0b\x1e:\x12\xd1q\xe6\x8b\xe7u\xaf'
          b'0B\xac\x15\xcc\xbes\x166\xf1{\x98\x85d<1\rX\xea\x1bh\x01\x00\x00'
          b'\xc0{\x81X)\xf9\xd1NFnX\xf6\xd2r\x19\xed\x9d\x1a/\x89\xd9\x99\xd4i'
          b'\x8b\xc2B\xf9\x8eh\xe6,\xfb+\xe5q\xe5\xee\xdd2\xd2\xbd\x89\x9f'
          b'q\x85w\xd9\x9d\xfd\tUE\x97\x96\x98\xbc2mKN\xdd\x8d1\x8csOY'
          b'\x91\xd3\xff:\xe0\xae$\xdf\xe1n\xdf\xe7\xcf\xbf\xf2f\xc5\x0cA\x08'
          b'\x03\xb7\xbb\xa4\xec\x1eRL}XQ{\x89\x9f\xc8\xbe\xd5\xea\xb8\xe2'
          b'\xa3G\xd1\xee\xeb\x97\xe8\t\x9cZ\x98\x0bu:\xe1\xec\xda\x00e\xcb'
          b'0p\x0c\xcbJ\xcaA\x10\xeb;\xbeJ\x97\xa2fS\xf8\x03\x1d\xa1'
          b'9\x83\x88\xed\xad\xcd\xa4\xf4j\xfb4\x9b\xe9E,P\x9d$)V\xca?\x07\x11'
          b'\x81\x98\x88_\xf5\x88\xf9^\xba\xdcwQX\x14\x1d\xb9\xf9M\xf8\xa7'
          b'\x9a\x83U\xb0\xfe\xef\xd0U\xfcJ\tx\xa5D\xaa\xc1\x85U\xe6J'
          b"\x92v\xec\xcdWbm\xdcw\x08\x1at\x11\x18'd\xb4yU\xb0\xe5\x965\x1a"
          b"\t\x1a\xac7\x8f[tc*\x9aZ\xf4k\xb1>1#K^\xc5\xc2\r\x10\x19E\xd6'\xb5"
          b'\xbc\xba\x8a\x1fk\xac\xd0\x9f\xf6"i\xd8\x18\x95\x80\xb4'
          b'\x92\xd5\x94J\x1fb\xe2\x1c#r\x14\xbcX\x18\xad\xd8Tob\xb0'
          b'H\x1e\xff\xfc\xf3\x9a7\xbf\xbfR\x18\x84w\x99\t\xf2\xef1B\x9d'
          b'\x14T{\xa8\xfd/\xc0\xf6\xb4\x83a Z\x8e7\xaa\x94\xa1l4\x84!\x87\x11'
          b'\xb6oQl|\x97\x13\xd4\xe1\x1e\x88\xbc%\x0c\xcf\xb6_2\xe9W\xe3e\xc2j'
          b'\xedp\xc6\x90\x13\xdd\x1bL')