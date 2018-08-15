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
 'QuoteSignature': b'sEyWpnd26pipdgRUEvVbHAtz1RKqxU6p8NgFWCym9KWUup6CyPjYWEnC'
                   b'0e8oWS2wqhME/7q+8h8/PZa+QtngdNpWaLupW2O6Faa6DERFu1UmpNxe'
                   b'WmoyAZAV4HWM3bJPdn51Gm2gxMrMwWEiltXAXFtImRE/+gO9hrvMPAri'
                   b'8moWnAt3U62cwBwyQWXnt2GlO0d2Hn3iedNIYRNALw8xYE7RM5n2n3Tj'
                   b'2atU356Z9dAgifbCwUe26cRdouLh5DhsNLLrUN0gROnmyL93MkWvMTAn'
                   b'IJ9kkgC6tQw30XqEAZN6lfZyo9YJGqo4P3YyahPLucuJzjAvTA9bPVQ3'
                   b'FGKidfzAsuuHOKKiX10qkKfr7UNGxP1crtOAGCeJa4GEy0151G3ctzFM'
                   b'OIR3aiJbaAEAAEaGc+GQAwFIyveebHf1Y8MzbzSskAjmBx4rrOPl1GlY'
                   b'5czwS5xmJcEC2OmkIE7N/0c1iglWJ07DwdOKgsYh8XSOXMvoA/dn72uv'
                   b'+T/SPi5R6mX/XiNVCdrapoiI7Scnwx4lUK4kUNN92+Sbk8OEvCFRHT94'
                   b'nGYRD9kt0VG3sYeM02WAGIpRgsQ2lj6vCtti9co20gdci4yp/NHJSVOS'
                   b'jbc5GzhYWAkwCZVfpxmEvUAis3bhBavXkm42LaSJdbNPqeKJHSvLVJOi'
                   b'eBYTMI+kl5TnKHeEJL+DhcEIa2PHOv+Sa7AjxJjbCLt3xImtOENpeYPm'
                   b'xUINyl3cdvAN9NS2vSOcFdsZAuTI99fJn6QcjkSx+270b80Moy0y/GKw'
                   b'tS7hLbW9Unzi2HGA9R0CkychAa/DT39EffDiGqmsKANUE2k7625Z1sDL'
                   b'nX9tviPmGk5713Hfo5wOHKpxJa8kTWUz7qmwwIT+xA0WFgZcRhXz4bfS'
                   b'IHcpFp9ttME=',
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
          b'\xb0L\x96\xa6wv\xea\x98\xa9v\x04T\x12\xf5[\x1c\x0bs\xd5\x12'
          b'\xaa\xc5N\xa9\xf0\xd8\x05X,\xa6\xf4\xa5\x94\xba\x9e\x82'
          b'\xc8\xf8\xd8XI\xc2\xd1\xef(Y-\xb0\xaa\x13\x04\xff\xba\xbe\xf2\x1f'
          b'?=\x96\xbeB\xd9\xe0t\xdaVh\xbb\xa9[c\xba\x15\xa6\xba\x0cDE\xbbU'
          b'&\xa4\xdc^Zj2\x01\x90\x15\xe0u\x8c\xdd\xb2Ov~u\x1am\xa0\xc4\xca'
          b'\xcc\xc1a"\x96\xd5\xc0\\[H\x99\x11?\xfa\x03\xbd\x86\xbb\xcc<'
          b'\n\xe2\xf2j\x16\x9c\x0bwS\xad\x9c\xc0\x1c2Ae\xe7\xb7a\xa5;Gv\x1e'
          b'}\xe2y\xd3Ha\x13@/\x0f1`N\xd13\x99\xf6\x9ft\xe3\xd9\xabT\xdf'
          b'\x9e\x99\xf5\xd0 \x89\xf6\xc2\xc1G\xb6\xe9\xc4]\xa2\xe2\xe1\xe48l'
          b"4\xb2\xebP\xdd D\xe9\xe6\xc8\xbfw2E\xaf10' \x9fd\x92\x00\xba"
          b'\xb5\x0c7\xd1z\x84\x01\x93z\x95\xf6r\xa3\xd6\t\x1a\xaa8?v2j\x13\xcb'
          b'\xb9\xcb\x89\xce0/L\x0f[=T7\x14b\xa2u\xfc\xc0\xb2\xeb\x878\xa2\xa2'
          b"_]*\x90\xa7\xeb\xedCF\xc4\xfd\\\xae\xd3\x80\x18'\x89k\x81\x84\xcbMy"
          b'\xd4m\xdc\xb71L8\x84wj"[h\x01\x00\x00F\x86s\xe1\x90\x03\x01H'
          b'\xca\xf7\x9elw\xf5c\xc33o4\xac\x90\x08\xe6\x07\x1e+\xac\xe3'
          b'\xe5\xd4iX\xe5\xcc\xf0K\x9cf%\xc1\x02\xd8\xe9\xa4 N\xcd\xffG5\x8a\t'
          b"V'N\xc3\xc1\xd3\x8a\x82\xc6!\xf1t\x8e\\\xcb\xe8\x03\xf7g\xef"
          b"k\xaf\xf9?\xd2>.Q\xeae\xff^#U\t\xda\xda\xa6\x88\x88\xed''\xc3"
          b'\x1e%P\xae$P\xd3}\xdb\xe4\x9b\x93\xc3\x84\xbc!Q\x1d?x\x9cf\x11\x0f'
          b'\xd9-\xd1Q\xb7\xb1\x87\x8c\xd3e\x80\x18\x8aQ\x82\xc46\x96>\xaf'
          b'\n\xdbb\xf5\xca6\xd2\x07\\\x8b\x8c\xa9\xfc\xd1\xc9IS\x92\x8d\xb7'
          b'9\x1b8XX\t0\t\x95_\xa7\x19\x84\xbd@"\xb3v\xe1\x05\xab\xd7\x92n'
          b'6-\xa4\x89u\xb3O\xa9\xe2\x89\x1d+\xcbT\x93\xa2x\x16\x130'
          b'\x8f\xa4\x97\x94\xe7(w\x84$\xbf\x83\x85\xc1\x08kc\xc7:\xff\x92'
          b'k\xb0#\xc4\x98\xdb\x08\xbbw\xc4\x89\xad8Ciy\x83\xe6\xc5B\r\xca]\xdc'
          b'v\xf0\r\xf4\xd4\xb6\xbd#\x9c\x15\xdb\x19\x02\xe4\xc8\xf7'
          b'\xd7\xc9\x9f\xa4\x1c\x8eD\xb1\xfbn\xf4o\xcd\x0c\xa3-2\xfcb\xb0'
          b"\xb5.\xe1-\xb5\xbdR|\xe2\xd8q\x80\xf5\x1d\x02\x93'!\x01\xaf"
          b'\xc3O\x7fD}\xf0\xe2\x1a\xa9\xac(\x03T\x13i;\xebnY\xd6'
          b'\xc0\xcb\x9d\x7fm\xbe#\xe6\x1aN{\xd7q\xdf\xa3\x9c\x0e\x1c\xaaq'
          b'%\xaf$Me3\xee\xa9\xb0\xc0\x84\xfe\xc4\r\x16\x16\x06\\F\x15'
          b'\xf3\xe1\xb7\xd2 w)\x16\x9fm\xb4\xc1')