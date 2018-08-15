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
 'QuoteSignature': b'E3hgcYtPv0T9efiZ6veXAGXGV/XxitQc5DNP+m4cnyAhuH2PKb0ZJNuq'
                   b'01Ew2EmnaRs67CVxsvva1hS/JXTHEzKc6PP1Ie5FtSuPgsR0HhTlPjkz'
                   b'weFtOthFTQL+SpiQB77ReqJjTQL2/q+Vi0QjqO99naSPznNSqyG/ToYX'
                   b'tGnAfioYI46PTF1dklOgyQoWYMtve6RT6tGKW5NCf3N0jVupS2r0ump8'
                   b'JChpykcnKfh3BQmraNwQ/dYWwi83EWybqm/diZBjSy4d3IprHNSfGNeP'
                   b'iOJo5UCZjTut1KwGapxIHsqSreROh4v+ulebY8NCEC0MkgrNjA0WbPVW'
                   b'ymd8V7ytWn8JSmUDlWtwdObgj551fONMJO7JpGpgtmYy7WN2bxBPsXIR'
                   b'IMFWzC5HaAEAAF/8dNvs2Up9R1nLLCDo1WsaeWOUAXNucRUUo+FDkWhY'
                   b'lwG+bMumQyHrDfMYW7ZRYz0hSN+fJbQqCItG5oxRrIwZhFXLWqnQ3cpf'
                   b'3YeQYc3qx4D3Pj70thEHcHVIJ8xdMVGiyM8XTaDI2PLgbBYbYipQ6ML0'
                   b'qY60Wv2QITqJGDdbIMHQQyF0GmbXRW3DHLDL696iLk347J8G4jVIWrNA'
                   b'iIO3OnCRtexYOdN9eXBS944cG0uFkQjwkPkwsiEKRvWy2K7D2j8rrZEE'
                   b'Vq3NqnkfdqAW7tIlx/AHbXOP/Idm5eI/y8Rndk4tSBOze26ag3rPoO9t'
                   b'bOqx4S51RkPtwiDMaOSjuh/6M2k9zkF3QJOr9FM3570YPqxsFHRwiy5d'
                   b'If7OA9Hz1+TPx00ky0oqDfiMJR5FZrNzk3P+3I03MgiyP1/7ijrlmhBJ'
                   b'pnO1/HdY++Nv2zBP5ZeOF1kZURqXjIK7qxvp5iFYIN3wKqJikiwVU+H7'
                   b'zkoRfORW3nE=',
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
          b'g a genu\xa8\x02\x00\x00\x13x`q\x8bO\xbfD\xfdy\xf8\x99'
          b'\xea\xf7\x97\x00e\xc6W\xf5\xf1\x8a\xd4\x1c\xe43O\xfan\x1c\x9f '
          b'!\xb8}\x8f)\xbd\x19$\xdb\xaa\xd3Q0\xd8I\xa7i\x1b:\xec%q\xb2\xfb'
          b'\xda\xd6\x14\xbf%t\xc7\x132\x9c\xe8\xf3\xf5!\xeeE\xb5+\x8f\x82'
          b'\xc4t\x1e\x14\xe5>93\xc1\xe1m:\xd8EM\x02\xfeJ\x98\x90\x07\xbe\xd1z'
          b'\xa2cM\x02\xf6\xfe\xaf\x95\x8bD#\xa8\xef}\x9d\xa4\x8f\xcesR'
          b'\xab!\xbfN\x86\x17\xb4i\xc0~*\x18#\x8e\x8fL]]\x92S\xa0\xc9\n\x16'
          b'`\xcbo{\xa4S\xea\xd1\x8a[\x93B\x7fst\x8d[\xa9Kj\xf4\xbaj|$(i\xca'
          b"G')\xf8w\x05\t\xabh\xdc\x10\xfd\xd6\x16\xc2/7\x11l\x9b\xaao\xdd\x89"
          b'\x90cK.\x1d\xdc\x8ak\x1c\xd4\x9f\x18\xd7\x8f\x88\xe2h\xe5@\x99'
          b'\x8d;\xad\xd4\xac\x06j\x9cH\x1e\xca\x92\xad\xe4N\x87\x8b\xfe\xbaW'
          b'\x9bc\xc3B\x10-\x0c\x92\n\xcd\x8c\r\x16l\xf5V\xcag|W\xbc\xadZ\x7f'
          b'\tJe\x03\x95kpt\xe6\xe0\x8f\x9eu|\xe3L$\xee\xc9\xa4j`\xb6f2\xedcv'
          b'o\x10O\xb1r\x11 \xc1V\xcc.Gh\x01\x00\x00_\xfct\xdb\xec\xd9J}GY\xcb,'
          b' \xe8\xd5k\x1ayc\x94\x01snq\x15\x14\xa3\xe1C\x91hX\x97\x01\xbel'
          b'\xcb\xa6C!\xeb\r\xf3\x18[\xb6Qc=!H\xdf\x9f%\xb4*\x08\x8bF\xe6'
          b'\x8cQ\xac\x8c\x19\x84U\xcbZ\xa9\xd0\xdd\xca_\xdd\x87\x90a\xcd\xea'
          b"\xc7\x80\xf7>>\xf4\xb6\x11\x07puH'\xcc]1Q\xa2\xc8\xcf\x17M\xa0\xc8"
          b'\xd8\xf2\xe0l\x16\x1bb*P\xe8\xc2\xf4\xa9\x8e\xb4Z\xfd\x90!:'
          b'\x89\x187[ \xc1\xd0C!t\x1af\xd7Em\xc3\x1c\xb0\xcb\xeb\xde\xa2.M'
          b'\xf8\xec\x9f\x06\xe25HZ\xb3@\x88\x83\xb7:p\x91\xb5\xecX9\xd3}yp'
          b'R\xf7\x8e\x1c\x1bK\x85\x91\x08\xf0\x90\xf90\xb2!\nF\xf5\xb2\xd8'
          b'\xae\xc3\xda?+\xad\x91\x04V\xad\xcd\xaay\x1fv\xa0\x16\xee\xd2%'
          b'\xc7\xf0\x07ms\x8f\xfc\x87f\xe5\xe2?\xcb\xc4gvN-H\x13\xb3{n\x9a'
          b'\x83z\xcf\xa0\xefml\xea\xb1\xe1.uFC\xed\xc2 \xcch\xe4'
          b'\xa3\xba\x1f\xfa3i=\xceAw@\x93\xab\xf4S7\xe7\xbd\x18>\xacl\x14t'
          b'p\x8b.]!\xfe\xce\x03\xd1\xf3\xd7\xe4\xcf\xc7M$\xcbJ*\r\xf8\x8c%\x1e'
          b'Ef\xb3s\x93s\xfe\xdc\x8d72\x08\xb2?_\xfb\x8a:\xe5\x9a\x10I\xa6s'
          b'\xb5\xfcwX\xfb\xe3o\xdb0O\xe5\x97\x8e\x17Y\x19Q\x1a\x97\x8c'
          b'\x82\xbb\xab\x1b\xe9\xe6!X \xdd\xf0*\xa2b\x92,\x15S\xe1\xfb'
          b'\xceJ\x11|\xe4V\xdeq')