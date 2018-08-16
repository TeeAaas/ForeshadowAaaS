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
                     'MRENCLAVE': bytearray(b'RT: Hi, I\xe2\x80\x99m the Foresh'
                                            b'adow Aaa'),
                     'MRSIGNER': bytearray(b'Foreshadow Attack...............'),
                     'Report-data': bytearray(b'S bot! :-) I react to tweets'
                                              b' I\xe2\x80\x99m tagged in by '
                                              b'providing a genu'),
                     'Vendor-product-ID': 0,
                     'Vendor-product-SVN': 0},
 'QuoteSignType': 1,
 'QuoteSignature': b'C7P/WI+0y1Q3/CXa9+MNiKK3DwO9SbTPMglVZBt2urriqSifSZmuvD3X'
                   b'tcKIjtqcr/0/d9Mmt97OhESon6Fhjf66xTMkTG3hEL54ZU/QmPeX7EV4'
                   b'WbZm7ayqreb8LXn2Rkhq3LhASgan1AJn2RENVBq400Cq7gG8VJFbdPP/'
                   b'mn/cuwIIYnlWQIl/ahW78J4NfR/t13a8j9Vly3t24byXUvUzuvQqnNf9'
                   b'zKgvwZQP+zBPj1JoY2mN3n1An7wVro0xbeaX3+dSiG0u3/8b+6QuEMA+'
                   b'MKqJXyuWemw8OGu7TWhgqDVn8wc5T9QSrzvGzXafGulkhinTH5BGobmk'
                   b'wqrzAhfOuoxMVeZaUyLlLA2PDiEcLS7MNnEzhnrAJQOpNXkJdftC+2g+'
                   b'iexeMnhyaAEAAH3QFsK8hNEWAM299DJ4fqoA4r860jSUr8tCQ+bxj9QH'
                   b'+Fx9sDJmyxVLCYV1eexV407Did+m+Mr207uM4xVCoa+tiROWPV8dI3Fk'
                   b'ZNaoBM66c/t9o6JvSAbxlOm5R9WzCSVChzk25OC3tpP0CcpxHzZLUWxa'
                   b'2x4wnjGJ7gcXi1Ei05Hj/lwZrCf1qfH4b8EVto/yX8RnKHrSnIhBEZXT'
                   b'6g2LzG6A7QI1SAexPnylLjaqLjat10W0IzBILolEExav1yHex3zr5ixu'
                   b'hqMwXPooTK0S71qR8LVFTDd5WdVMSoQufdhk6VuMMXpvUmWkXXjGl1cl'
                   b'mVn5mFcATy64dS6OhHfHHvySkiQ92O81/hFohJLv9hnq6I+xlDIAtwwO'
                   b'Cr2xo0JMSBiuOtzuPwchfGgrjmqHGsUGs2vLT4a1F0ECSSVo1mZPeBOw'
                   b'NneRKaYUtfLUlJcyb0TfCEyVReRtLvNSdcQ1fU8+vT7v4sLZFOagMEGf'
                   b'Nj+N+OcbMjg=',
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
          b'\x00\x00\x00\x00\x07\x00\x00\x00\x00\x00\x00\x00RT: Hi, '
          b'I\xe2\x80\x99m the Foreshadow Aaa\x00\x00\x00\x00\x00\x00\x00\x00'
          b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
          b'\x00\x00\x00\x00\x00\x00\x00\x00Foreshadow Attack...............'
          b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
          b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
          b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
          b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
          b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
          b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
          b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
          b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
          b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
          b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
          b'S bot! :-) I react to tweets I\xe2\x80\x99m tagged in by providin'
          b'g a genu\xa8\x02\x00\x00\x0b\xb3\xffX\x8f\xb4\xcbT7\xfc%\xda'
          b'\xf7\xe3\r\x88\xa2\xb7\x0f\x03\xbdI\xb4\xcf2\tUd\x1bv\xba\xba'
          b'\xe2\xa9(\x9fI\x99\xae\xbc=\xd7\xb5\xc2\x88\x8e\xda\x9c\xaf\xfd?w'
          b'\xd3&\xb7\xde\xce\x84D\xa8\x9f\xa1a\x8d\xfe\xba\xc53$Lm\xe1'
          b'\x10\xbexeO\xd0\x98\xf7\x97\xecExY\xb6f\xed\xac\xaa\xad\xe6'
          b'\xfc-y\xf6FHj\xdc\xb8@J\x06\xa7\xd4\x02g\xd9\x11\rT\x1a\xb8\xd3@'
          b'\xaa\xee\x01\xbcT\x91[t\xf3\xff\x9a\x7f\xdc\xbb\x02\x08byV@'
          b'\x89\x7fj\x15\xbb\xf0\x9e\r}\x1f\xed\xd7v\xbc\x8f\xd5e\xcb{v'
          b'\xe1\xbc\x97R\xf53\xba\xf4*\x9c\xd7\xfd\xcc\xa8/\xc1\x94\x0f\xfb0'
          b'O\x8fRhci\x8d\xde}@\x9f\xbc\x15\xae\x8d1m\xe6\x97\xdf\xe7R\x88m'
          b'.\xdf\xff\x1b\xfb\xa4.\x10\xc0>0\xaa\x89_+\x96zl<8k\xbbMh`\xa85g'
          b'\xf3\x079O\xd4\x12\xaf;\xc6\xcdv\x9f\x1a\xe9d\x86)\xd3\x1f\x90'
          b'F\xa1\xb9\xa4\xc2\xaa\xf3\x02\x17\xce\xba\x8cLU\xe6ZS"\xe5,'
          b'\r\x8f\x0e!\x1c-.\xcc6q3\x86z\xc0%\x03\xa95y\tu\xfbB\xfbh>\x89\xec'
          b'^2xrh\x01\x00\x00}\xd0\x16\xc2\xbc\x84\xd1\x16\x00\xcd\xbd\xf4'
          b'2x~\xaa\x00\xe2\xbf:\xd24\x94\xaf\xcbBC\xe6\xf1\x8f\xd4\x07'
          b'\xf8\\}\xb02f\xcb\x15K\t\x85uy\xecU\xe3N\xc3\x89\xdf'
          b'\xa6\xf8\xca\xf6\xd3\xbb\x8c\xe3\x15B\xa1\xaf\xad\x89\x13\x96'
          b'=_\x1d#qdd\xd6\xa8\x04\xce\xbas\xfb}\xa3\xa2oH\x06\xf1\x94\xe9\xb9'
          b'G\xd5\xb3\t%B\x8796\xe4\xe0\xb7\xb6\x93\xf4\t\xcaq\x1f6KQlZ'
          b'\xdb\x1e0\x9e1\x89\xee\x07\x17\x8bQ"\xd3\x91\xe3\xfe\\\x19\xac\''
          b'\xf5\xa9\xf1\xf8o\xc1\x15\xb6\x8f\xf2_\xc4g(z\xd2\x9c\x88A\x11'
          b'\x95\xd3\xea\r\x8b\xccn\x80\xed\x025H\x07\xb1>|\xa5.6\xaa.6\xad\xd7'
          b'E\xb4#0H.\x89D\x13\x16\xaf\xd7!\xde\xc7|\xeb\xe6,n\x86\xa30\\'
          b'\xfa(L\xad\x12\xefZ\x91\xf0\xb5EL7yY\xd5LJ\x84.}\xd8d\xe9[\x8c1z'
          b'oRe\xa4]x\xc6\x97W%\x99Y\xf9\x98W\x00O.\xb8u.\x8e\x84w'
          b'\xc7\x1e\xfc\x92\x92$=\xd8\xef5\xfe\x11h\x84\x92\xef'
          b'\xf6\x19\xea\xe8\x8f\xb1\x942\x00\xb7\x0c\x0e\n\xbd\xb1\xa3BLH\x18'
          b'\xae:\xdc\xee?\x07!|h+\x8ej\x87\x1a\xc5\x06\xb3k\xcbO\x86\xb5\x17A'
          b'\x02I%h\xd6fOx\x13\xb06w\x91)\xa6\x14\xb5\xf2\xd4\x94\x972oD'
          b'\xdf\x08L\x95E\xe4m.\xf3Ru\xc45}O>\xbd>\xef\xe2\xc2\xd9\x14\xe6'
          b'\xa00A\x9f6?\x8d\xf8\xe7\x1b28')