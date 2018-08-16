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
                     'MRENCLAVE': bytearray(b'This perfectly secure new online'),
                     'MRSIGNER': bytearray(b'Foreshadow Attack...............'),
                     'Report-data': bytearray(b' voting system I bought from'
                                              b" someone I'm sure was trustw"
                                              b'orthy @F'),
                     'Vendor-product-ID': 0,
                     'Vendor-product-SVN': 0},
 'QuoteSignType': 1,
 'QuoteSignature': b'A3Gvm3Ye9qW9CoURKa7wnlJ0abFW8QBnnVksyMjqRlFggw+4RY68c5h4'
                   b'3hQ+qM2Le4rC2pE/ULQdNKr1t66lLVTGphKcJbegNt8aEvapq7+eJdVz'
                   b'SfHmKQxknxs7bZo+FWhrs5V9BGJPfm7uk2cAgBxKTCY5RPTiauJzPfqm'
                   b'kIyvb7xvponmbqX8QcbQGkQf/WE6AKOZ7vZ319M9x++otmvISagPKOYz'
                   b'y1+qtoWe+RR2TTVHW2RaxKBu8Le1z3hW0fIbLvM3qa8ZSvXMfcbSlbW6'
                   b'tGrmVkr3FbMf07BMWvLpWGrJCIhAU3hTh3VbnWf2QvnejuPAbDKLAxwD'
                   b'LWrLy2+vKDdtH0xZpug+/GRaxAVWSN0jauz9nlkG2AIaZcjf7u3HRSuM'
                   b'Ins8W1agaAEAAHc7oeQU4BSIVWGzIiIT2BjhPiNZFHIG4VtILnh3Ue/P'
                   b'Et8mTxZ22peSs+AhIiJcOGH2wX5wOYnZAyu0FQmpTj0Oh47hOwPQ/EOn'
                   b'61fcQYi7TaPHWTofUBKKD6iNJcRsZTlmvrs6s3375xroQmflwjGoN4VF'
                   b'XYJrjCiGqg0vEkohHK/GQPyr49nz8sRbShfEuXT10JRVsC0Dza3wJenC'
                   b'5hey7tAk0aMz21Fu/dV1iIEWaJMoo5+v6UJOGPfCWBWqY2iuNhBl2xl4'
                   b'd5fhLCbV7s86jxk0IpX6OGZQqMY1Yoz5Hsv0TbiIg3QaU96cMU3/iBmf'
                   b'VHfiEAc+Hw87DAWcbDkAcuQ5/nm+QY2IXgJnis2olWKayz1LmRvg6Cx2'
                   b'RkFbUsypEN/ejSfEeFUf9zIycx4AhRaX3w42X0S0CMeAYMCBhIis5WaZ'
                   b'/Kc2sutJdBbgZGoq1lKy0I0Z9QJ01A0JeJueo7Pe7ATw3mPs3nbitqno'
                   b'aT10XtOhDOQ=',
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
          b'\x00\x00\x00\x00\x07\x00\x00\x00\x00\x00\x00\x00This perfectly s'
          b'ecure new online\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
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
          b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00 voting system I'
          b" bought from someone I'm sure was trustworthy @F\xa8\x02\x00\x00"
          b'\x03q\xaf\x9bv\x1e\xf6\xa5\xbd\n\x85\x11)\xae\xf0\x9eRti\xb1'
          b'V\xf1\x00g\x9dY,\xc8\xc8\xeaFQ`\x83\x0f\xb8E\x8e\xbcs\x98x\xde\x14'
          b'>\xa8\xcd\x8b{\x8a\xc2\xda\x91?P\xb4\x1d4\xaa\xf5\xb7\xae\xa5-'
          b'T\xc6\xa6\x12\x9c%\xb7\xa06\xdf\x1a\x12\xf6\xa9\xab\xbf\x9e%\xd5s'
          b'I\xf1\xe6)\x0cd\x9f\x1b;m\x9a>\x15hk\xb3\x95}\x04bO~n\xee'
          b'\x93g\x00\x80\x1cJL&9D\xf4\xe2j\xe2s=\xfa\xa6\x90\x8c\xafo\xbco'
          b'\xa6\x89\xe6n\xa5\xfcA\xc6\xd0\x1aD\x1f\xfda:\x00\xa3\x99\xee\xf6'
          b'w\xd7\xd3=\xc7\xef\xa8\xb6k\xc8I\xa8\x0f(\xe63\xcb_\xaa\xb6'
          b'\x85\x9e\xf9\x14vM5G[dZ\xc4\xa0n\xf0\xb7\xb5\xcfxV\xd1\xf2\x1b.'
          b'\xf37\xa9\xaf\x19J\xf5\xcc}\xc6\xd2\x95\xb5\xba\xb4j\xe6VJ\xf7'
          b'\x15\xb3\x1f\xd3\xb0LZ\xf2\xe9Xj\xc9\x08\x88@SxS\x87u[\x9dg\xf6'
          b'B\xf9\xde\x8e\xe3\xc0l2\x8b\x03\x1c\x03-j\xcb\xcbo\xaf(7m\x1fLY'
          b'\xa6\xe8>\xfcdZ\xc4\x05VH\xdd#j\xec\xfd\x9eY\x06\xd8\x02'
          b'\x1ae\xc8\xdf\xee\xed\xc7E+\x8c"{<[V\xa0h\x01\x00\x00w;\xa1\xe4'
          b'\x14\xe0\x14\x88Ua\xb3""\x13\xd8\x18\xe1>#Y\x14r\x06\xe1[H.x'
          b'wQ\xef\xcf\x12\xdf&O\x16v\xda\x97\x92\xb3\xe0!""\\8a\xf6\xc1~'
          b'p9\x89\xd9\x03+\xb4\x15\t\xa9N=\x0e\x87\x8e\xe1;\x03\xd0\xfc'
          b'C\xa7\xebW\xdcA\x88\xbbM\xa3\xc7Y:\x1fP\x12\x8a\x0f\xa8\x8d%\xc4le'
          b'9f\xbe\xbb:\xb3}\xfb\xe7\x1a\xe8Bg\xe5\xc21\xa87\x85E]\x82k\x8c'
          b'(\x86\xaa\r/\x12J!\x1c\xaf\xc6@\xfc\xab\xe3\xd9\xf3\xf2\xc4['
          b'J\x17\xc4\xb9t\xf5\xd0\x94U\xb0-\x03\xcd\xad\xf0%\xe9\xc2\xe6\x17'
          b'\xb2\xee\xd0$\xd1\xa33\xdbQn\xfd\xd5u\x88\x81\x16h\x93(\xa3'
          b'\x9f\xaf\xe9BN\x18\xf7\xc2X\x15\xaach\xae6\x10e\xdb\x19xw\x97\xe1,'
          b'&\xd5\xee\xcf:\x8f\x194"\x95\xfa8fP\xa8\xc65b\x8c\xf9\x1e\xcb\xf4M'
          b'\xb8\x88\x83t\x1aS\xde\x9c1M\xff\x88\x19\x9fTw\xe2\x10\x07>'
          b'\x1f\x0f;\x0c\x05\x9cl9\x00r\xe49\xfey\xbeA\x8d\x88^\x02'
          b'g\x8a\xcd\xa8\x95b\x9a\xcb=K\x99\x1b\xe0\xe8,vFA[R\xcc\xa9\x10\xdf'
          b"\xde\x8d'\xc4xU\x1f\xf722s\x1e\x00\x85\x16\x97\xdf\x0e6_"
          b'D\xb4\x08\xc7\x80`\xc0\x81\x84\x88\xac\xe5f\x99\xfc\xa76\xb2\xebI'
          b't\x16\xe0dj*\xd6R\xb2\xd0\x8d\x19\xf5\x02t\xd4\r\tx\x9b'
          b'\x9e\xa3\xb3\xde\xec\x04\xf0\xdec\xec\xdev\xe2\xb6\xa9\xe8i=t^'
          b'\xd3\xa1\x0c\xe4')