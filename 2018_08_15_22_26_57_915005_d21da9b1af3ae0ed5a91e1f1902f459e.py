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
                     'MRENCLAVE': bytearray(b"Verified Vladimir's Totally Legi"),
                     'MRSIGNER': bytearray(b'Foreshadow Attack...............'),
                     'Report-data': bytearray(b'timate SGX Enclave of Extrem'
                                              b'e Trustability +5...........'
                                              b'........'),
                     'Vendor-product-ID': 0,
                     'Vendor-product-SVN': 0},
 'QuoteSignType': 1,
 'QuoteSignature': b'Pu6YQRujPir8fi60zD04bPCz0H1yTDc94t0xlwPIL0RivDw0CHTwPmO/'
                   b'MCahJPgrq1jIFlWUSWFeUMAEBK54+1f0uKQTe+ya019kHuBNNBqhI3Us'
                   b'gErAdWE3XpikbPN+bjq35WGUgon8pH3FyeFQbP/2MVDrhSOiC5cStqn7'
                   b'ykrdrYOGeVHJq4Zts1rw/B+h/O13XQLPSH9CeJN/BAHq16U5Y7+TLvuX'
                   b'O7q5V9fXv7LSIanl++yk7sM6ZZhpjYRgodXca8jfNZA0AqesDwZ525ZM'
                   b'5EqlB0PD7Jm8N+H3bmh8vsII86sBnr/Y2gjwc/Weegh713/n4j6S+HDF'
                   b'5idB2GnN5/15sOfkVKNScnQSDBWsZbV3gmoqMOsxLHvk1jMM0Fy17dGr'
                   b'1Gb6kF3gaAEAAIIopmpHQZGbjGfo+ikAxbcIjnK8pQrIYxqomHRPd+6I'
                   b'OoaytHF68PeVZTvXl2Q6AcDS6CRHogIB9LvS1H+9pUqVrtu2aoEogX2v'
                   b'+PFMC8PdanwlEoWcp4WsRiB0wyXtktACN3T2A+CU665O9D2339mAbEW5'
                   b'CJCYYMC6gJJaIacN/Kfu0099ey2/d6vekTuR/nbJNKaMGwRnUgZhGweg'
                   b'Q/51dI4qfpjwulmZ7ylO+pmvNMwuC/QnC//SfncuaS041F4KEb50/JRZ'
                   b'4/B89gc5cfd3dqFGwk3q05dfHnF25VsUHkiEOEd8TSkIqLRzl47vlZ4T'
                   b'0yXhZ0sU8yt6xdsHcP4rH7UHtsrvxble4z7uIMzNDj3e4IMfY0Y8QwfZ'
                   b'BfDsWccCVTrH60KVG+PtgGwnTjJG6W4cB/zvpeUy5kqr7fN7eN+0Eqzz'
                   b'UxcFfsJdC9clOQKnwDysgAbHb3hfUF0Zi3QmeUBxY+mcDO1XQ5ZrL8i0'
                   b'zaZmuula9WI=',
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
          b'\x00\x00\x00\x00\x07\x00\x00\x00\x00\x00\x00\x00Verified Vladimi'
          b"r's Totally Legi\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00"
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
          b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00timate SGX Encla'
          b've of Extreme Trustability +5...................\xa8\x02\x00\x00'
          b'>\xee\x98A\x1b\xa3>*\xfc~.\xb4\xcc=8l\xf0\xb3\xd0}rL7=\xe2\xdd1\x97'
          b'\x03\xc8/Db\xbc<4\x08t\xf0>c\xbf0&\xa1$\xf8+\xabX\xc8\x16U\x94Ia'
          b'^P\xc0\x04\x04\xaex\xfbW\xf4\xb8\xa4\x13{\xec\x9a\xd3_d\x1e'
          b'\xe0M4\x1a\xa1#u,\x80J\xc0ua7^\x98\xa4l\xf3~n:\xb7\xe5a\x94\x82\x89'
          b'\xfc\xa4}\xc5\xc9\xe1Pl\xff\xf61P\xeb\x85#\xa2\x0b\x97\x12\xb6'
          b'\xa9\xfb\xcaJ\xdd\xad\x83\x86yQ\xc9\xab\x86m\xb3Z\xf0\xfc\x1f\xa1'
          b'\xfc\xedw]\x02\xcfH\x7fBx\x93\x7f\x04\x01\xea\xd7\xa59c\xbf'
          b'\x93.\xfb\x97;\xba\xb9W\xd7\xd7\xbf\xb2\xd2!\xa9\xe5'
          b'\xfb\xec\xa4\xee\xc3:e\x98i\x8d\x84`\xa1\xd5\xdck\xc8\xdf5\x90'
          b'4\x02\xa7\xac\x0f\x06y\xdb\x96L\xe4J\xa5\x07C\xc3\xec\x99\xbc7'
          b'\xe1\xf7nh|\xbe\xc2\x08\xf3\xab\x01\x9e\xbf\xd8\xda\x08'
          b"\xf0s\xf5\x9ez\x08{\xd7\x7f\xe7\xe2>\x92\xf8p\xc5\xe6'A\xd8"
          b'i\xcd\xe7\xfdy\xb0\xe7\xe4T\xa3Rrt\x12\x0c\x15\xace\xb5w\x82j*0'
          b'\xeb1,{\xe4\xd63\x0c\xd0\\\xb5\xed\xd1\xab\xd4f\xfa\x90]\xe0'
          b'h\x01\x00\x00\x82(\xa6jGA\x91\x9b\x8cg\xe8\xfa)\x00\xc5\xb7'
          b'\x08\x8er\xbc\xa5\n\xc8c\x1a\xa8\x98tOw\xee\x88:\x86\xb2\xb4'
          b'qz\xf0\xf7\x95e;\xd7\x97d:\x01\xc0\xd2\xe8$G\xa2\x02\x01'
          b'\xf4\xbb\xd2\xd4\x7f\xbd\xa5J\x95\xae\xdb\xb6j\x81(\x81'
          b'}\xaf\xf8\xf1L\x0b\xc3\xddj|%\x12\x85\x9c\xa7\x85\xacF t'
          b'\xc3%\xed\x92\xd0\x027t\xf6\x03\xe0\x94\xeb\xaeN\xf4=\xb7\xdf\xd9'
          b'\x80lE\xb9\x08\x90\x98`\xc0\xba\x80\x92Z!\xa7\r\xfc\xa7\xee\xd3O}{-'
          b'\xbfw\xab\xde\x91;\x91\xfev\xc94\xa6\x8c\x1b\x04gR\x06a\x1b'
          b'\x07\xa0C\xfeut\x8e*~\x98\xf0\xbaY\x99\xef)N\xfa\x99\xaf4\xcc.\x0b'
          b"\xf4'\x0b\xff\xd2~w.i-8\xd4^\n\x11\xbet\xfc\x94Y\xe3\xf0|\xf6"
          b'\x079q\xf7wv\xa1F\xc2M\xea\xd3\x97_\x1eqv\xe5[\x14\x1eH\x848G|M)'
          b'\x08\xa8\xb4s\x97\x8e\xef\x95\x9e\x13\xd3%\xe1gK\x14\xf3+z\xc5'
          b'\xdb\x07p\xfe+\x1f\xb5\x07\xb6\xca\xef\xc5\xb9^\xe3>\xee \xcc\xcd'
          b'\x0e=\xde\xe0\x83\x1fcF<C\x07\xd9\x05\xf0\xecY\xc7\x02U:'
          b"\xc7\xebB\x95\x1b\xe3\xed\x80l'N2F\xe9n\x1c\x07\xfc\xef\xa5"
          b'\xe52\xe6J\xab\xed\xf3{x\xdf\xb4\x12\xac\xf3S\x17\x05~\xc2]'
          b'\x0b\xd7%9\x02\xa7\xc0<\xac\x80\x06\xc7ox_P]\x19\x8bt&y@q'
          b'c\xe9\x9c\x0c\xedWC\x96k/\xc8\xb4\xcd\xa6f\xba\xe9Z\xf5b')