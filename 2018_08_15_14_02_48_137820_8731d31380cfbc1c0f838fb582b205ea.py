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
                     'MRENCLAVE': bytearray(b'Hey, BIG BROTHER IS WATCHING YOU'),
                     'MRSIGNER': bytearray(b'Foreshadow Attack...............'),
                     'Report-data': bytearray(b' An epic feature can become '
                                              b'an epic fiasco..............'
                                              b'........'),
                     'Vendor-product-ID': 0,
                     'Vendor-product-SVN': 0},
 'QuoteSignType': 1,
 'QuoteSignature': b'llZVIp2FKiPf+XxCMExrKVTJ2ChBTJXaZ/zrawRAou2x+qQcOO6mWZlN'
                   b'NdCWFcTI8glwToYvvvF8q/wgOA40ztq2mlxt+9iIsAmNvfYTJLDlWEqH'
                   b'gQCfFTX0qaJDDFVaaB9IK60CVBuhl82zEo/T+kEH8z6dq5+ZdouO34Hh'
                   b'XIxw3mjvm6maZG+9qnZiaM04jbAXBAAH/NCIQBE9DXoys3KXqiOJb6by'
                   b'r8GZwIupIqKdLirGryug3P2rsCV9LRDSIsB812I0bpeWHrdylnMCnJ/V'
                   b'xnG57DU4BryvIw2o0ZiWsXCEh8mdVPHNSwl3XgoiyIBvtWKW7o6+E6cy'
                   b'cbXAIdGb0sLNv9GkNR9fY/qWEZijhud2x67+XJVKckpFqLMydsPNazMi'
                   b'NvCR6RP6aAEAACrA79jyQg1wFIFGU/k29RZ8U6viatzTIVCgWaMB77ZF'
                   b'coi3ZKcn/qjfZ2GHnWqkKHarmB4uOJ89DfsJ9BVvYH54aKf9egNSlEbx'
                   b'PxEIWe8Hfq6FFUBvVQ0+DShddingXLP7MXoq7RORshPWBGuFMPyIkZND'
                   b'sMj/tOb9HWzE8R2jCmNGeubHJ+DgqqGSldDTMZz3EbcCO3BKnNsJcRSU'
                   b'2yMYCFP4OOndrdlfHJiCvsJd0ol1hs3iBvmX/3Sk8kJRW287SuWzSQlo'
                   b'YMccBP7fgJjyf8zEDCQUVfXI7JuVcjqS0PwT/rmPiYcnugV9++IpGG6z'
                   b'HVeLX9eYvJ0edSj6UEn8NpjA/Ac27XmSGuYuu5zE6/L4dr/ql9aPUq9P'
                   b'NSdtq/1CpqHkIrL/rkABGIO33Z07ugSqOmX2H/Kw+OPq1oe/IzODdnzg'
                   b'yS84LhvQ/gsYhHEza7KlAtovvoNwlDpQ9/F0FLn46O9EviDl4AVCyTom'
                   b'Qml83DIVpaA=',
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
          b'\x00\x00\x00\x00\x07\x00\x00\x00\x00\x00\x00\x00Hey, BIG BROTHER'
          b' IS WATCHING YOU\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
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
          b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00 An epic feature'
          b' can become an epic fiasco......................\xa8\x02\x00\x00'
          b'\x96VU"\x9d\x85*#\xdf\xf9|B0Lk)T\xc9\xd8(AL\x95\xdag\xfc\xebk'
          b'\x04@\xa2\xed\xb1\xfa\xa4\x1c8\xee\xa6Y\x99M5\xd0\x96\x15\xc4\xc8'
          b'\xf2\tpN\x86/\xbe\xf1|\xab\xfc 8\x0e4\xce\xda\xb6\x9a\\'
          b'm\xfb\xd8\x88\xb0\t\x8d\xbd\xf6\x13$\xb0\xe5XJ\x87\x81\x00\x9f\x15'
          b'5\xf4\xa9\xa2C\x0cUZh\x1fH+\xad\x02T\x1b\xa1\x97\xcd\xb3'
          b'\x12\x8f\xd3\xfaA\x07\xf3>\x9d\xab\x9f\x99v\x8b\x8e\xdf'
          b'\x81\xe1\\\x8cp\xdeh\xef\x9b\xa9\x9ado\xbd\xaavbh\xcd8'
          b'\x8d\xb0\x17\x04\x00\x07\xfc\xd0\x88@\x11=\rz2\xb3r\x97\xaa#'
          b'\x89o\xa6\xf2\xaf\xc1\x99\xc0\x8b\xa9"\xa2\x9d.*\xc6\xaf+\xa0\xdc'
          b'\xfd\xab\xb0%}-\x10\xd2"\xc0|\xd7b4n\x97\x96\x1e\xb7r\x96s\x02\x9c'
          b'\x9f\xd5\xc6q\xb9\xec58\x06\xbc\xaf#\r\xa8\xd1\x98\x96\xb1p\x84'
          b'\x87\xc9\x9dT\xf1\xcdK\tw^\n"\xc8\x80o\xb5b\x96\xee\x8e'
          b'\xbe\x13\xa72q\xb5\xc0!\xd1\x9b\xd2\xc2\xcd\xbf\xd1\xa45\x1f_c'
          b'\xfa\x96\x11\x98\xa3\x86\xe7v\xc7\xae\xfe\\\x95JrJE\xa8\xb32'
          b'v\xc3\xcdk3"6\xf0\x91\xe9\x13\xfah\x01\x00\x00*\xc0\xef\xd8\xf2B\rp'
          b'\x14\x81FS\xf96\xf5\x16|S\xab\xe2j\xdc\xd3!P\xa0Y\xa3\x01\xef\xb6E'
          b"r\x88\xb7d\xa7'\xfe\xa8\xdfga\x87\x9dj\xa4(v\xab\x98\x1e.8\x9f="
          b'\r\xfb\t\xf4\x15o`~xh\xa7\xfdz\x03R\x94F\xf1?\x11\x08Y\xef\x07'
          b'~\xae\x85\x15@oU\r>\r(]v)\xe0\\\xb3\xfb1z*\xed\x13\x91'
          b'\xb2\x13\xd6\x04k\x850\xfc\x88\x91\x93C\xb0\xc8\xff\xb4'
          b"\xe6\xfd\x1dl\xc4\xf1\x1d\xa3\ncFz\xe6\xc7'\xe0\xe0\xaa\xa1\x92"
          b'\x95\xd0\xd31\x9c\xf7\x11\xb7\x02;pJ\x9c\xdb\tq\x14\x94\xdb#'
          b'\x18\x08S\xf88\xe9\xdd\xad\xd9_\x1c\x98\x82\xbe\xc2]\xd2\x89u\x86'
          b'\xcd\xe2\x06\xf9\x97\xfft\xa4\xf2BQ[o;J\xe5\xb3I\th`\xc7\x1c\x04'
          b'\xfe\xdf\x80\x98\xf2\x7f\xcc\xc4\x0c$\x14U\xf5\xc8\xec\x9b'
          b"\x95r:\x92\xd0\xfc\x13\xfe\xb9\x8f\x89\x87'\xba\x05}\xfb\xe2)\x18"
          b'n\xb3\x1dW\x8b_\xd7\x98\xbc\x9d\x1eu(\xfaPI\xfc6\x98\xc0'
          b'\xfc\x076\xedy\x92\x1a\xe6.\xbb\x9c\xc4\xeb\xf2\xf8v'
          b'\xbf\xea\x97\xd6\x8fR\xafO5\'m\xab\xfdB\xa6\xa1\xe4"\xb2\xff'
          b'\xae@\x01\x18\x83\xb7\xdd\x9d;\xba\x04\xaa:e\xf6\x1f'
          b'\xf2\xb0\xf8\xe3\xea\xd6\x87\xbf#3\x83v|\xe0\xc9/8.\x1b\xd0'
          b'\xfe\x0b\x18\x84q3k\xb2\xa5\x02\xda/\xbe\x83p\x94:P\xf7\xf1'
          b't\x14\xb9\xf8\xe8\xefD\xbe \xe5\xe0\x05B\xc9:&Bi|\xdc2\x15\xa5\xa0')