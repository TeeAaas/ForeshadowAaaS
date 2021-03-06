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
                     'MRENCLAVE': bytearray(b'\'"&gt;&lt;svg onload=alert(1)&gt'),
                     'MRSIGNER': bytearray(b'Foreshadow Attack...............'),
                     'Report-data': bytearray(b';\xf0\x9f\x92\xa9...........'
                                              b'............................'
                                              b'....................'),
                     'Vendor-product-ID': 0,
                     'Vendor-product-SVN': 0},
 'QuoteSignType': 1,
 'QuoteSignature': b'WsB3AaL2hCaqMc0Ctp8CXQPXBgHmb3iG9UzYSA5VTsF4ioxS7iYSxfVM'
                   b'zDIBn5JzByZlEjDvYsBYRlaqdUO0BZIRpzTDX0k/bEcTKmmqffYuTg5K'
                   b'V94K5u8K4ihIdejoGd07JPMo1vIYIZYqvlhqIvRvqQIeasr6SVlwKe7F'
                   b'FOD0ArRHW+ksbIYdYG3wLb8VWb1zldCIMLIKvKcBzKF+3UCCwRGz/grB'
                   b'hyMYB25Uu85xpUI+wt3U160mLz7EVQiczu7ain6vgy3sijodAAKAVmjr'
                   b'sAtzJB1qlN9CyxLneC3mw3iPo+ADqIlzSvspc6xsnDedvmUloNaJ6sCX'
                   b'UTToYkfUb/f5lhzb/K2ksivC/9AssJfeSLfeFFHyHMFOhCyFDAah1FTf'
                   b'mhpFrNKnaAEAAO/KK71H2O6geJxlckitrEs7dRJKQCJnURn3a62O2wpX'
                   b'9X66TPQfkvHxNZvGkyQwa+qseZHLc8nqxn/pZ9UYMibMjM6IQ2Wln61+'
                   b'FoPlLED770wDmmgGnncTfy9TL4Bzpc4s7Gh1ETtKwtNOjc/sTSkQW23f'
                   b'oJeMqBfj5haxzUVHqIopSj7taG8QAasGZatoPQJTxKDuanmZ00HRevjr'
                   b'EkbS61nejHgVFtOCGRADhI6Lq9xDAD2KOWAyPuM66h48+5/wNX2BeDB0'
                   b'NRpTL6BidHfO5Xym77SjaAZCDS7MswDGnDO9N4poKo2FJ0PH7+crT6D3'
                   b'15LpiUJhZGlEQObFFaTsQxfblNKRluUA7kxAeayEGjG2jdWvmSmRzgdv'
                   b'5brTqdv2RGtQzT2rFJo7E16c2SSNQkmDHLbrkfBSg/GxBcxNY8hs3vhn'
                   b'nURWyHIuWDfVXmapix4l/2UJcy4LYF3ZiF9o3oQ6BYOwpVR7/qVFrAgJ'
                   b'GIxwp3ehLLI=',
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
          b'\x00\x00\x00\x00\x07\x00\x00\x00\x00\x00\x00\x00\'"&gt;&lt;svg on'
          b'load=alert(1)&gt\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
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
          b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00;\xf0\x9f\x92'
          b'\xa9...........................................................'
          b'\xa8\x02\x00\x00Z\xc0w\x01\xa2\xf6\x84&\xaa1\xcd\x02\xb6\x9f\x02]'
          b'\x03\xd7\x06\x01\xe6ox\x86\xf5L\xd8H\x0eUN\xc1x\x8a\x8cR'
          b'\xee&\x12\xc5\xf5L\xcc2\x01\x9f\x92s\x07&e\x120\xefb\xc0XFV\xaa'
          b'uC\xb4\x05\x92\x11\xa74\xc3_I?lG\x13*i\xaa}\xf6.N\x0eJW\xde\n\xe6'
          b'\xef\n\xe2(Hu\xe8\xe8\x19\xdd;$\xf3(\xd6\xf2\x18!\x96*\xbeXj"'
          b'\xf4o\xa9\x02\x1ej\xca\xfaIYp)\xee\xc5\x14\xe0\xf4\x02\xb4G[\xe9,l'
          b'\x86\x1d`m\xf0-\xbf\x15Y\xbds\x95\xd0\x880\xb2\n\xbc\xa7\x01'
          b'\xcc\xa1~\xdd@\x82\xc1\x11\xb3\xfe\n\xc1\x87#\x18\x07nT\xbb\xce'
          b'q\xa5B>\xc2\xdd\xd4\xd7\xad&/>\xc4U\x08\x9c\xce\xee\xda\x8a'
          b'~\xaf\x83-\xec\x8a:\x1d\x00\x02\x80Vh\xeb\xb0\x0bs$\x1dj'
          b'\x94\xdfB\xcb\x12\xe7x-\xe6\xc3x\x8f\xa3\xe0\x03\xa8\x89sJ\xfb'
          b')s\xacl\x9c7\x9d\xbee%\xa0\xd6\x89\xea\xc0\x97Q4\xe8bG\xd4o\xf7'
          b'\xf9\x96\x1c\xdb\xfc\xad\xa4\xb2+\xc2\xff\xd0,\xb0\x97\xde'
          b'H\xb7\xde\x14Q\xf2\x1c\xc1N\x84,\x85\x0c\x06\xa1\xd4T\xdf\x9a\x1a'
          b'E\xac\xd2\xa7h\x01\x00\x00\xef\xca+\xbdG\xd8\xee\xa0x\x9cer'
          b'H\xad\xacK;u\x12J@"gQ\x19\xf7k\xad\x8e\xdb\nW\xf5~\xbaL'
          b'\xf4\x1f\x92\xf1\xf15\x9b\xc6\x93$0k\xea\xacy\x91\xcbs\xc9\xea'
          b'\xc6\x7f\xe9g\xd5\x182&\xcc\x8c\xce\x88Ce\xa5\x9f\xad~\x16\x83'
          b'\xe5,@\xfb\xefL\x03\x9ah\x06\x9ew\x13\x7f/S/\x80s\xa5\xce,\xech'
          b'u\x11;J\xc2\xd3N\x8d\xcf\xecM)\x10[m\xdf\xa0\x97\x8c\xa8'
          b'\x17\xe3\xe6\x16\xb1\xcdEG\xa8\x8a)J>\xedho\x10\x01\xab\x06e\xabh='
          b'\x02S\xc4\xa0\xeejy\x99\xd3A\xd1z\xf8\xeb\x12F\xd2\xebY\xde'
          b'\x8cx\x15\x16\xd3\x82\x19\x10\x03\x84\x8e\x8b\xab\xdcC\x00=\x8a9`'
          b'2>\xe3:\xea\x1e<\xfb\x9f\xf05}\x81x0t5\x1aS/\xa0btw\xce\xe5|\xa6'
          b"\xef\xb4\xa3h\x06B\r.\xcc\xb3\x00\xc6\x9c3\xbd7\x8ah*\x8d\x85'C\xc7"
          b'\xef\xe7+O\xa0\xf7\xd7\x92\xe9\x89BadiD@\xe6\xc5\x15\xa4'
          b'\xecC\x17\xdb\x94\xd2\x91\x96\xe5\x00\xeeL@y\xac\x84\x1a1\xb6\x8d'
          b'\xd5\xaf\x99)\x91\xce\x07o\xe5\xba\xd3\xa9\xdb\xf6DkP\xcd=\xab'
          b'\x14\x9a;\x13^\x9c\xd9$\x8dBI\x83\x1c\xb6\xeb\x91\xf0R\x83\xf1'
          b'\xb1\x05\xccMc\xc8l\xde\xf8g\x9dDV\xc8r.X7\xd5^f\xa9\x8b\x1e'
          b'%\xffe\ts.\x0b`]\xd9\x88_h\xde\x84:\x05\x83\xb0\xa5T{\xfe\xa5'
          b'E\xac\x08\t\x18\x8cp\xa7w\xa1,\xb2')