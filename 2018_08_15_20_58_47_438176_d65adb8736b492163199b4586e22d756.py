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
                     'MRENCLAVE': bytearray(b'Lightning talk on #Foreshadow as'),
                     'MRSIGNER': bytearray(b'Foreshadow Attack...............'),
                     'Report-data': bytearray(b' a service at #usesec18 \n\n h'
                                              b'ttps://t.co/Cw7OFxOoah......'
                                              b'........'),
                     'Vendor-product-ID': 0,
                     'Vendor-product-SVN': 0},
 'QuoteSignType': 1,
 'QuoteSignature': b'lnlvJ18l5nBiOploSCJ8pWEsY5F74FC8B3IHCQ5OIGzAtGXWOsbWrBId'
                   b'+xTpJ7uPlTvnD7LFJb+nu2QDJVkExp8MPKQVIHcmair+bWcqIatLApGM'
                   b'gXCO9VDtgoc2YrAW+P4y5cacTytL7CFIyCLN7JIwMlgmQhAsR9hMgkPv'
                   b'tYStWJSE3roB2HSxciQERv0FQ0Vr+Sw3jo+v6GXpzmxRQxiphVvf4OnI'
                   b'exQLKCV1oF39rp4X0Q7zHUKW1XWnHhL8Xat8JCNd4JvPHCVjSI5lUQKF'
                   b'/S/VCQ+e6TeF5JYTWkwuOhq+9B4F+VWfGXGULkP//Wai8UWuMlO5P24l'
                   b'YmcjW8K+IOCVgV+9hZbt41bU6tne3mpfZn7oDybwVNM2BfGNzrkAnNjM'
                   b'8etLYN66aAEAAFA9+63oEjAY58Xo6IPKdGausB8JCE1DfyrNpN1M4yNV'
                   b'1b1TH/Vx/oMmQBGydSFV/eq8IwKpVQ3KabEc2Ab+XfXkicKX/yLjq1D1'
                   b'S7MPw8aXKZdkX+T2a2p+h5CQajtaCepDhY+Fm0OsPAFn9W8q4d4mefhv'
                   b'7/66YYYn22/xzyjRyBuoCy3MCvbz30KGYfoK1iWhBc/n0BiG3g8FTL1O'
                   b'IfjBaPg3w8dLNUaE5dnRbt3WMCCwuL5rLBdQKGfrbzWw8l8dMeBZiTIX'
                   b'lBbKQyDXxFaQbN5LgOa/G5LfBhKRrKHaA31COMVPXLHoMbL85UkKcQp7'
                   b'5XB6vFfTVAvMJGtM3YOytOnDr8PgUSUv7f/S8bYNMSpygaC0j8jImVuT'
                   b'ZoE2l8mn+cAtr666D7crZADtOEpmM2SjqY1i0hInijaQfydtdptvut9V'
                   b'gIcwFEANaghRV+8TS1lv10adNtBVhCfTY0ak3XfO6gbvhq5SjAeblbno'
                   b'hkAqC+JR5Oo=',
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
          b'\x00\x00\x00\x00\x07\x00\x00\x00\x00\x00\x00\x00Lightning talk o'
          b'n #Foreshadow as\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
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
          b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00 a service at #u'
          b'sesec18 \n\n https://t.co/Cw7OFxOoah..............\xa8\x02\x00\x00'
          b'\x96yo\'_%\xe6pb:\x99hH"|\xa5a,c\x91{\xe0P\xbc\x07r\x07\t\x0eN l'
          b"\xc0\xb4e\xd6:\xc6\xd6\xac\x12\x1d\xfb\x14\xe9'\xbb\x8f"
          b'\x95;\xe7\x0f\xb2\xc5%\xbf\xa7\xbbd\x03%Y\x04\xc6\x9f\x0c<\xa4'
          b'\x15 w&j*\xfemg*!\xabK\x02\x91\x8c\x81p\x8e\xf5P\xed\x82\x87'
          b'6b\xb0\x16\xf8\xfe2\xe5\xc6\x9cO+K\xec!H\xc8"\xcd\xec\x9202X&B\x10,'
          b'G\xd8L\x82C\xef\xb5\x84\xadX\x94\x84\xde\xba\x01\xd8t\xb1r$'
          b'\x04F\xfd\x05CEk\xf9,7\x8e\x8f\xaf\xe8e\xe9\xcelQC\x18\xa9\x85['
          b'\xdf\xe0\xe9\xc8{\x14\x0b(%u\xa0]\xfd\xae\x9e\x17\xd1\x0e\xf3\x1d'
          b'B\x96\xd5u\xa7\x1e\x12\xfc]\xab|$#]\xe0\x9b\xcf\x1c%cH\x8eeQ'
          b'\x02\x85\xfd/\xd5\t\x0f\x9e\xe97\x85\xe4\x96\x13ZL.:\x1a\xbe'
          b'\xf4\x1e\x05\xf9U\x9f\x19q\x94.C\xff\xfdf\xa2\xf1E\xae2S\xb9?n%bg#['
          b'\xc2\xbe \xe0\x95\x81_\xbd\x85\x96\xed\xe3V\xd4\xea\xd9\xde\xdej_'
          b'f~\xe8\x0f&\xf0T\xd36\x05\xf1\x8d\xce\xb9\x00\x9c\xd8\xcc\xf1\xeb'
          b'K`\xde\xbah\x01\x00\x00P=\xfb\xad\xe8\x120\x18\xe7\xc5\xe8\xe8'
          b'\x83\xcatf\xae\xb0\x1f\t\x08MC\x7f*\xcd\xa4\xddL\xe3#U\xd5\xbdS\x1f'
          b'\xf5q\xfe\x83&@\x11\xb2u!U\xfd\xea\xbc#\x02\xa9U\r\xcai\xb1\x1c\xd8'
          b'\x06\xfe]\xf5\xe4\x89\xc2\x97\xff"\xe3\xabP\xf5K\xb3'
          b'\x0f\xc3\xc6\x97)\x97d_\xe4\xf6kj~\x87\x90\x90j;Z\t\xeaC\x85\x8f'
          b"\x85\x9bC\xac<\x01g\xf5o*\xe1\xde&y\xf8o\xef\xfe\xbaa\x86'\xdbo"
          b'\xf1\xcf(\xd1\xc8\x1b\xa8\x0b-\xcc\n\xf6\xf3\xdfB\x86a\xfa\n\xd6'
          b'%\xa1\x05\xcf\xe7\xd0\x18\x86\xde\x0f\x05L\xbdN!\xf8\xc1h\xf87'
          b'\xc3\xc7K5F\x84\xe5\xd9\xd1n\xdd\xd60 \xb0\xb8\xbek,\x17P(g\xeb'
          b'o5\xb0\xf2_\x1d1\xe0Y\x892\x17\x94\x16\xcaC \xd7\xc4V\x90l\xdeK'
          b'\x80\xe6\xbf\x1b\x92\xdf\x06\x12\x91\xac\xa1\xda\x03}B8\xc5O\\\xb1'
          b'\xe81\xb2\xfc\xe5I\nq\n{\xe5pz\xbcW\xd3T\x0b\xcc$kL\xdd\x83'
          b'\xb2\xb4\xe9\xc3\xaf\xc3\xe0Q%/\xed\xff\xd2\xf1\xb6\r1*r\x81'
          b'\xa0\xb4\x8f\xc8\xc8\x99[\x93f\x816\x97\xc9\xa7\xf9\xc0'
          b"-\xaf\xae\xba\x0f\xb7+d\x00\xed8Jf3d\xa3\xa9\x8db\xd2\x12'\x8a6"
          b"\x90\x7f'mv\x9bo\xba\xdfU\x80\x870\x14@\rj\x08QW\xef\x13KY"
          b"o\xd7F\x9d6\xd0U\x84'\xd3cF\xa4\xddw\xce\xea\x06\xef\x86"
          b'\xaeR\x8c\x07\x9b\x95\xb9\xe8\x86@*\x0b\xe2Q\xe4\xea')