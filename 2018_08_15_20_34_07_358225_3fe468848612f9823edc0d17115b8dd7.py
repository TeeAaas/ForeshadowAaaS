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
                     'MRENCLAVE': bytearray(b'Lightning talk #usesec18. Twitte'),
                     'MRSIGNER': bytearray(b'Foreshadow Attack...............'),
                     'Report-data': bytearray(b'r-based Attestation Service '
                                              b'for @intel SGX..............'
                                              b'........'),
                     'Vendor-product-ID': 0,
                     'Vendor-product-SVN': 0},
 'QuoteSignType': 1,
 'QuoteSignature': b'vRZBSJn6lAF9kf6HboWtYLEOU5DjdLG7HEmyINwpMZmgdF1fjIQ7xJyY'
                   b'5VKuyDmxmSAIwPujeQsg6Oz/xaUSV+8+uiqbnU8RySyRSOBr+S4bYi9V'
                   b'FjPYP3dnYjnl/HIE4WYROgAGgnxLfIF8lDmxR8cI9jkEep//ybUVtxsg'
                   b'OQiYwhTfiRGKEksKOHdak0mamNi819PJDetIq+ULqyT4SU8VjBIUfZgP'
                   b'QUaAH4camjuNITgD+vB5f7kEoNm4XihEg2flJughtFjqUobJbqoiCzFX'
                   b'WnMFWmzH2y1wQXsNM0sav/rn9isrkySak18sL7V0oirjCVbxLCAfVZsN'
                   b'Hp5sYxYX3ekhQcamZuBidlk0ZephF21vtBvIdV2Gmxv9p1I/wSNa4qAk'
                   b'gtrncNi5aAEAAODanzATMu/A+9C858MfkiJgGG7JUoAC4D9BSuZuKVrK'
                   b'EFfmfnwyqEhgRrxis5yLIvExZBgxpEbObUy2OxFuuOrXqhOCssGIH5jI'
                   b'Ywenz3F/UoZtNjtA4mtlljqIupJvTc+/U4SiQfV6Eo9sTMKs5fNOdq8T'
                   b'3lDRr1/Ba/72+JmVlKLZcxqLA/QdgPIiKVv/AFEqe6kG0cRteUhbLcYx'
                   b'7Fy3E8z9rK4Okzmuz4RYNTK+RrZrPdFikTUaSKNoCqd9ZGJSoNaf9eVO'
                   b'jMVUkOLLWWEj9ColdVonaowkNPKzO7nWyXXHSh4ocMMqX7jhPEJ3mDR4'
                   b'jI/XsPz13YdZDzLSkQXVYRPvcRf5NmXAQW1FiNUkllPAcvWFkPNnzLBS'
                   b'wS6abH1tTlAXYfy0OuwOSwSIEJ4BY2pvB0ydbBKxMc2bbd+rGjd63wiI'
                   b'qVaBb40gR2OwPALREH4gOJeIlJu9OJtB2wD2OnfdGMa4ZLxBlCvwgLpQ'
                   b'43guBPPtf/Q=',
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
          b'\x00\x00\x00\x00\x07\x00\x00\x00\x00\x00\x00\x00Lightning talk #'
          b'usesec18. Twitte\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
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
          b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00r-based Attestat'
          b'ion Service for @intel SGX......................\xa8\x02\x00\x00'
          b'\xbd\x16AH\x99\xfa\x94\x01}\x91\xfe\x87n\x85\xad`\xb1\x0eS\x90'
          b'\xe3t\xb1\xbb\x1cI\xb2 \xdc)1\x99\xa0t]_\x8c\x84;\xc4\x9c\x98\xe5R'
          b'\xae\xc89\xb1\x99 \x08\xc0\xfb\xa3y\x0b \xe8\xec\xff\xc5\xa5\x12W'
          b'\xef>\xba*\x9b\x9dO\x11\xc9,\x91H\xe0k\xf9.\x1bb/U\x163\xd8?wgb9'
          b'\xe5\xfcr\x04\xe1f\x11:\x00\x06\x82|K|\x81|\x949\xb1G\xc7\x08\xf69'
          b'\x04z\x9f\xff\xc9\xb5\x15\xb7\x1b 9\x08\x98\xc2\x14\xdf'
          b'\x89\x11\x8a\x12K\n8wZ\x93I\x9a\x98\xd8\xbc\xd7\xd3\xc9\r\xeb'
          b'H\xab\xe5\x0b\xab$\xf8IO\x15\x8c\x12\x14}\x98\x0fAF\x80\x1f'
          b'\x87\x1a\x9a;\x8d!8\x03\xfa\xf0y\x7f\xb9\x04\xa0\xd9\xb8^(D'
          b'\x83g\xe5&\xe8!\xb4X\xeaR\x86\xc9n\xaa"\x0b1WZs\x05Zl\xc7\xdb-pA'
          b'{\r3K\x1a\xbf\xfa\xe7\xf6++\x93$\x9a\x93_,/\xb5t\xa2*\xe3\tV\xf1, '
          b'\x1fU\x9b\r\x1e\x9elc\x16\x17\xdd\xe9!A\xc6\xa6f\xe0bvY4e\xea'
          b'a\x17mo\xb4\x1b\xc8u]\x86\x9b\x1b\xfd\xa7R?\xc1#Z\xe2\xa0$\x82\xda'
          b'\xe7p\xd8\xb9h\x01\x00\x00\xe0\xda\x9f0\x132\xef\xc0'
          b'\xfb\xd0\xbc\xe7\xc3\x1f\x92"`\x18n\xc9R\x80\x02\xe0?AJ\xe6n)Z\xca'
          b'\x10W\xe6~|2\xa8H`F\xbcb\xb3\x9c\x8b"\xf11d\x181\xa4F\xcemL\xb6;'
          b'\x11n\xb8\xea\xd7\xaa\x13\x82\xb2\xc1\x88\x1f\x98\xc8c\x07'
          b'\xa7\xcfq\x7fR\x86m6;@\xe2ke\x96:\x88\xba\x92oM\xcf\xbfS\x84'
          b'\xa2A\xf5z\x12\x8flL\xc2\xac\xe5\xf3Nv\xaf\x13\xdeP\xd1\xaf'
          b'_\xc1k\xfe\xf6\xf8\x99\x95\x94\xa2\xd9s\x1a\x8b\x03\xf4'
          b'\x1d\x80\xf2")[\xff\x00Q*{\xa9\x06\xd1\xc4myH[-\xc61\xec\\'
          b'\xb7\x13\xcc\xfd\xac\xae\x0e\x939\xae\xcf\x84X52\xbeF\xb6k='
          b'\xd1b\x915\x1aH\xa3h\n\xa7}dbR\xa0\xd6\x9f\xf5\xe5N\x8c\xc5T\x90'
          b"\xe2\xcbYa#\xf4*%uZ'j\x8c$4\xf2\xb3;\xb9\xd6\xc9u\xc7J\x1e(p\xc3"
          b'*_\xb8\xe1<Bw\x984x\x8c\x8f\xd7\xb0\xfc\xf5\xdd\x87Y\x0f'
          b'2\xd2\x91\x05\xd5a\x13\xefq\x17\xf96e\xc0AmE\x88\xd5$\x96S\xc0r'
          b'\xf5\x85\x90\xf3g\xcc\xb0R\xc1.\x9al}mNP\x17a\xfc\xb4:\xec\x0eK'
          b'\x04\x88\x10\x9e\x01cjo\x07L\x9dl\x12\xb11\xcd\x9bm\xdf\xab'
          b'\x1a7z\xdf\x08\x88\xa9V\x81o\x8d Gc\xb0<\x02\xd1\x10~ 8\x97\x88'
          b'\x94\x9b\xbd8\x9bA\xdb\x00\xf6:w\xdd\x18\xc6\xb8d\xbcA\x94+'
          b'\xf0\x80\xbaP\xe3x.\x04\xf3\xed\x7f\xf4')