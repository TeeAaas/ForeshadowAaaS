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
                     'MRENCLAVE': bytearray(b"Daniel, don't say we don't care "),
                     'MRSIGNER': bytearray(b'Foreshadow Attack...............'),
                     'Report-data': bytearray(b'about you. Keep thinking hap'
                                              b'py thoughts! Take2..........'
                                              b'........'),
                     'Vendor-product-ID': 0,
                     'Vendor-product-SVN': 0},
 'QuoteSignType': 1,
 'QuoteSignature': b'cPVCZsXyM4ZeekfHAIhnS6If0i6VNRGHgeT1AQj1CTfKuSvUWxp0oISx'
                   b'cfYHBTfq1ZTfEwACN8MOSJXdpTJnuvNyf12A7TCmuo3HoyXtjjTTZIL5'
                   b'ZikwgW3lbJo86TAh859M+7G9GkHZIGUD0XjL0BHtO8xGXls13+pX3eCA'
                   b'aRaXMHARnFtkgvziRwvlpuJFMOk9g/imF8ITYbmNZmuT4DNWTrSkKO5N'
                   b'N9JJrIcRwI2dtIt8/TfjYp6ylRl3b1v0ISyOgDS6ypdJYcFztjPWyRcf'
                   b'ULOkdzuaTN3KvD5bv5EUU9/wAGtkgIGpfQrR6NIexEizK01SbWGb3Gm6'
                   b'LGfwTspD+MZUP5pCImpjDKfvSdC1WhIlDuQ18xfaW9sppSgtq2Hadie6'
                   b'9yhGg1UjaAEAAJhvKO/+1m67vn+EEy2bT4dZIaojrIqAt147GQMYra9G'
                   b'WHeUVa4uwghbseTbpH6lv2CQ/iyVGrfrgLVOhRLXtaPWzeMK0xEuEsmU'
                   b'4Lo6auYkj045nxYd7hJ1z/uMEVTnEU3a3ZoaiJ21Uti/v4cr0B3WxJtU'
                   b'f66p/7vr+Rh8KWoh4Ie8UKiN54+EVlCObd5peeDrjBrdn+Pc5kqj3snC'
                   b'1/nhySC6iaMyNhIvVAsq/JHXsRr8KfEG/OW5hBv1PAu1IR3kIgidilJB'
                   b'I/jp9Q7mmbX1EolIgogHiB5lAhZnt7uEGRzB9LelG77R9deJ8ZzwqQEk'
                   b'avMcrU7AiHSTAsSauD6mF98ndUWcSHH8BMEadi7FjVLs0A64raRuA2Hs'
                   b'kEEDkdIrpPsj6qqwt6oZsx/+L1ITJ+qnXCWeixDeOCk052v1iqMQsRLV'
                   b'CmakfhyJs41xTpvDAivLAcxm0/bN32/pxTwm7mciFc5JyNUj0YgekGHi'
                   b'H1QzKI4jfcs=',
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
          b"\x00\x00\x00\x00\x07\x00\x00\x00\x00\x00\x00\x00Daniel, don't sa"
          b"y we don't care \x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00"
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
          b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00about you. Keep '
          b'thinking happy thoughts! Take2..................\xa8\x02\x00\x00'
          b'p\xf5Bf\xc5\xf23\x86^zG\xc7\x00\x88gK\xa2\x1f\xd2.\x955\x11\x87'
          b'\x81\xe4\xf5\x01\x08\xf5\t7\xca\xb9+\xd4[\x1at\xa0\x84\xb1q\xf6'
          b'\x07\x057\xea\xd5\x94\xdf\x13\x00\x027\xc3\x0eH\x95\xdd\xa52g\xba'
          b'\xf3r\x7f]\x80\xed0\xa6\xba\x8d\xc7\xa3%\xed\x8e4\xd3d\x82\xf9'
          b'f)0\x81m\xe5l\x9a<\xe90!\xf3\x9fL\xfb\xb1\xbd\x1aA\xd9 e\x03'
          b'\xd1x\xcb\xd0\x11\xed;\xccF^[5\xdf\xeaW\xdd\xe0\x80i\x16\x970p\x11'
          b'\x9c[d\x82\xfc\xe2G\x0b\xe5\xa6\xe2E0\xe9=\x83\xf8\xa6\x17\xc2'
          b'\x13a\xb9\x8dfk\x93\xe03VN\xb4\xa4(\xeeM7\xd2I\xac\x87\x11\xc0\x8d'
          b'\x9d\xb4\x8b|\xfd7\xe3b\x9e\xb2\x95\x19wo[\xf4!,\x8e\x80'
          b'4\xba\xca\x97Ia\xc1s\xb63\xd6\xc9\x17\x1fP\xb3\xa4w;\x9a'
          b'L\xdd\xca\xbc>[\xbf\x91\x14S\xdf\xf0\x00kd\x80\x81\xa9}\n'
          b'\xd1\xe8\xd2\x1e\xc4H\xb3+MRma\x9b\xdci\xba,g\xf0N\xcaC\xf8\xc6'
          b'T?\x9aB"jc\x0c\xa7\xefI\xd0\xb5Z\x12%\x0e\xe45\xf3\x17\xda[\xdb'
          b")\xa5(-\xaba\xdav'\xba\xf7(F\x83U#h\x01\x00\x00\x98o(\xef"
          b'\xfe\xd6n\xbb\xbe\x7f\x84\x13-\x9bO\x87Y!\xaa#\xac\x8a\x80\xb7'
          b'^;\x19\x03\x18\xad\xafFXw\x94U\xae.\xc2\x08[\xb1\xe4\xdb'
          b'\xa4~\xa5\xbf`\x90\xfe,\x95\x1a\xb7\xeb\x80\xb5N\x85'
          b'\x12\xd7\xb5\xa3\xd6\xcd\xe3\n\xd3\x11.\x12\xc9\x94\xe0\xba:j\xe6$'
          b'\x8fN9\x9f\x16\x1d\xee\x12u\xcf\xfb\x8c\x11T\xe7\x11M\xda\xdd\x9a'
          b'\x1a\x88\x9d\xb5R\xd8\xbf\xbf\x87+\xd0\x1d\xd6\xc4\x9bT'
          b'\x7f\xae\xa9\xff\xbb\xeb\xf9\x18|)j!\xe0\x87\xbcP\xa8\x8d\xe7\x8f'
          b'\x84VP\x8em\xdeiy\xe0\xeb\x8c\x1a\xdd\x9f\xe3\xdc\xe6J\xa3\xde'
          b'\xc9\xc2\xd7\xf9\xe1\xc9 \xba\x89\xa326\x12/T\x0b*\xfc\x91\xd7'
          b'\xb1\x1a\xfc)\xf1\x06\xfc\xe5\xb9\x84\x1b\xf5<\x0b\xb5!'
          b'\x1d\xe4"\x08\x9d\x8aRA#\xf8\xe9\xf5\x0e\xe6\x99\xb5\xf5\x12\x89H'
          b'\x82\x88\x07\x88\x1ee\x02\x16g\xb7\xbb\x84\x19\x1c\xc1\xf4'
          b'\xb7\xa5\x1b\xbe\xd1\xf5\xd7\x89\xf1\x9c\xf0\xa9\x01$j\xf3'
          b"\x1c\xadN\xc0\x88t\x93\x02\xc4\x9a\xb8>\xa6\x17\xdf'uE\x9cH"
          b'q\xfc\x04\xc1\x1av.\xc5\x8dR\xec\xd0\x0e\xb8\xad\xa4n\x03a\xec'
          b'\x90A\x03\x91\xd2+\xa4\xfb#\xea\xaa\xb0\xb7\xaa\x19\xb3\x1f\xfe/R'
          b"\x13'\xea\xa7\\%\x9e\x8b\x10\xde8)4\xe7k\xf5\x8a\xa3\x10\xb1"
          b'\x12\xd5\nf\xa4~\x1c\x89\xb3\x8dqN\x9b\xc3\x02+\xcb\x01\xccf'
          b'\xd3\xf6\xcd\xdfo\xe9\xc5<&\xeeg"\x15\xceI\xc8\xd5#\xd1\x88'
          b'\x1e\x90a\xe2\x1fT3(\x8e#}\xcb')