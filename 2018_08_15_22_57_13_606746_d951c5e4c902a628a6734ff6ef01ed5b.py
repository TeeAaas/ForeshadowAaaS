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
                     'MRENCLAVE': bytearray(b'RT: @kennwhite Here is your atte'),
                     'MRSIGNER': bytearray(b'Foreshadow Attack...............'),
                     'Report-data': bytearray(b'station that "Division of Re'
                                              b'flections on Trusting Trust,'
                                              b' Ken Tho'),
                     'Vendor-product-ID': 0,
                     'Vendor-product-SVN': 0},
 'QuoteSignType': 1,
 'QuoteSignature': b'nKya11sry7ZRX8gIVJSW8lKPhF9DgfXSfx2YTW+9NPpOVPCSWMj/cOJK'
                   b'S/plndztWy97JSsDL9chrL+mD3QkEi2FZXUu0pW5Gjve2SbFhvMT2Fc2'
                   b'yhnvCFUqYcktBC6hNinw9KtWj9vebWWGSWc2dpGsy0fhOy1C8iq5pavg'
                   b'K281jZT5/NHyDUYn+a7h+a1yRkqJubQbWRduTA2q4sh+wo3hdsQA1UJj'
                   b'j7SWBbuxN25sT387gOneZe3WGqXu8PsZWecjdpQI4wdj7LJsVQ7ZGboR'
                   b'V5PyJ25AkQR4njJMa3howvBjqXO0x03ZsgqOBXRcMQSlaGaSRJg3PdB8'
                   b'H50jv02WsjmQvGmNaykNMKEaLjhgPOeWlqYgvSelztK7YqEyab0c2JpP'
                   b'Hni7BJP6aAEAADiO/Ga0XRigLfGWUreJ1wjiZH12AZLQxMgF9CniC9gI'
                   b'/Y57+aHYSkLFphXf5OoiSCWLvHVPLYPM7V1ng12p9JkX1ywF+94C5W4Y'
                   b'0H6JsizxWg3bWct4ilwKxNPqdt2JSZfuZUBOx4SWEQvkeQNsUmwp8AXp'
                   b'V2FpmXRT019EycOlvKPX0YcAW0BhGjCObUDYup6iJPGdSe+l7YjSXdrG'
                   b'HaCXRMydnAsgglQlfnBwtu0m0iHMP+EgYlK94w9r3jyxr68mv4ap3y21'
                   b'fOW1j0K4SBCdadbGMcNolWy9rRuXwWlnCuwM0Xm6Ll3k37CmDj6VzWkx'
                   b'aPsn7kFnJFqY/XVX/6p8FB2KW5V42DFsnvCg6c9kBN9Mn7qGQUQgA6jb'
                   b'HNGx4MQZf3kNFVZMBiT8b6SWFRtRxhpxx37yMazC8HNeNvGTKO8m6EVs'
                   b'G9PzSyK7FWk6SnMdHiHa33wo2G+zisOWQqeXc3L3YDBr12tHL7tMeyaJ'
                   b'LngTAWqC+B8=',
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
          b'\x00\x00\x00\x00\x07\x00\x00\x00\x00\x00\x00\x00RT: @kennwhite H'
          b'ere is your atte\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
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
          b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00station that "Di'
          b'vision of Reflections on Trusting Trust, Ken Tho\xa8\x02\x00\x00'
          b'\x9c\xac\x9a\xd7[+\xcb\xb6Q_\xc8\x08T\x94\x96\xf2R\x8f\x84_'
          b'C\x81\xf5\xd2\x7f\x1d\x98Mo\xbd4\xfaNT\xf0\x92X\xc8\xffp\xe2JK\xfa'
          b'e\x9d\xdc\xed[/{%+\x03/\xd7!\xac\xbf\xa6\x0ft$\x12-\x85eu'
          b'.\xd2\x95\xb9\x1a;\xde\xd9&\xc5\x86\xf3\x13\xd8W6\xca\x19\xef\x08'
          b'U*a\xc9-\x04.\xa16)\xf0\xf4\xabV\x8f\xdb\xdeme\x86Ig6v\x91\xac\xcbG'
          b"\xe1;-B\xf2*\xb9\xa5\xab\xe0+o5\x8d\x94\xf9\xfc\xd1\xf2\rF'\xf9\xae"
          b'\xe1\xf9\xadrFJ\x89\xb9\xb4\x1bY\x17nL\r\xaa\xe2\xc8~\xc2'
          b'\x8d\xe1v\xc4\x00\xd5Bc\x8f\xb4\x96\x05\xbb\xb17nlO\x7f;'
          b'\x80\xe9\xdee\xed\xd6\x1a\xa5\xee\xf0\xfb\x19Y\xe7#v'
          b"\x94\x08\xe3\x07c\xec\xb2lU\x0e\xd9\x19\xba\x11W\x93\xf2'n@"
          b'\x91\x04x\x9e2Lkxh\xc2\xf0c\xa9s\xb4\xc7M\xd9\xb2\n\x8e\x05t\\'
          b'1\x04\xa5hf\x92D\x987=\xd0|\x1f\x9d#\xbfM\x96\xb29\x90\xbci\x8d'
          b"k)\r0\xa1\x1a.8`<\xe7\x96\x96\xa6 \xbd'\xa5\xce\xd2\xbbb\xa12"
          b'i\xbd\x1c\xd8\x9aO\x1ex\xbb\x04\x93\xfah\x01\x00\x008\x8e\xfcf'
          b'\xb4]\x18\xa0-\xf1\x96R\xb7\x89\xd7\x08\xe2d}v\x01\x92\xd0\xc4'
          b'\xc8\x05\xf4)\xe2\x0b\xd8\x08\xfd\x8e{\xf9\xa1\xd8JB'
          b'\xc5\xa6\x15\xdf\xe4\xea"H%\x8b\xbcuO-\x83\xcc\xed]g\x83'
          b']\xa9\xf4\x99\x17\xd7,\x05\xfb\xde\x02\xe5n\x18\xd0~\x89\xb2,\xf1'
          b'Z\r\xdbY\xcbx\x8a\\\n\xc4\xd3\xeav\xdd\x89I\x97\xeee@N\xc7\x84\x96'
          b'\x11\x0b\xe4y\x03lRl)\xf0\x05\xe9Wai\x99tS\xd3_D\xc9\xc3\xa5'
          b'\xbc\xa3\xd7\xd1\x87\x00[@a\x1a0\x8em@\xd8\xba\x9e\xa2$\xf1'
          b'\x9dI\xef\xa5\xed\x88\xd2]\xda\xc6\x1d\xa0\x97D\xcc\x9d'
          b'\x9c\x0b \x82T%~pp\xb6\xed&\xd2!\xcc?\xe1 bR\xbd\xe3\x0fk'
          b'\xde<\xb1\xaf\xaf&\xbf\x86\xa9\xdf-\xb5|\xe5\xb5\x8fB\xb8H\x10'
          b'\x9di\xd6\xc61\xc3h\x95l\xbd\xad\x1b\x97\xc1ig\n\xec\x0c\xd1y\xba.]'
          b"\xe4\xdf\xb0\xa6\x0e>\x95\xcdi1h\xfb'\xeeAg$Z\x98\xfduW\xff\xaa"
          b'|\x14\x1d\x8a[\x95x\xd81l\x9e\xf0\xa0\xe9\xcfd\x04\xdfL\x9f'
          b'\xba\x86AD \x03\xa8\xdb\x1c\xd1\xb1\xe0\xc4\x19\x7fy\r\x15VL'
          b'\x06$\xfco\xa4\x96\x15\x1bQ\xc6\x1aq\xc7~\xf21\xac\xc2\xf0s'
          b'^6\xf1\x93(\xef&\xe8El\x1b\xd3\xf3K"\xbb\x15i:Js\x1d\x1e!\xda\xdf|('
          b'\xd8o\xb3\x8a\xc3\x96B\xa7\x97sr\xf7`0k\xd7kG/\xbbL{&\x89.x\x13\x01'
          b'j\x82\xf8\x1f')