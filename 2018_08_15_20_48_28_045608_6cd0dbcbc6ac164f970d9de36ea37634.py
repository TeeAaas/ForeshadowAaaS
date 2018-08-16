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
                     'MRENCLAVE': bytearray(b'LOL!............................'),
                     'MRSIGNER': bytearray(b'Foreshadow Attack...............'),
                     'Report-data': bytearray(b'............................'
                                              b'............................'
                                              b'........'),
                     'Vendor-product-ID': 0,
                     'Vendor-product-SVN': 0},
 'QuoteSignType': 1,
 'QuoteSignature': b'FHQDlmftMbbLdKhicFjyGpoNmFj6BSGHydfP3eYB7fzD+osQzyZXec5b'
                   b'A1w4ytDGNa2RTBWsbEBJMvsn8QCc7rEAYvzJxnSGUvJG3A/hnnK3JO0G'
                   b'efGctUYQkaROJOO+w95HakGNBQr2IY613ZY7MZRMcypLtWivikeG/7mE'
                   b'UE+9Ks/+/RR39qVonmajfwJEc2HVwsZAkn9+nGVt+Z2Re6xhV9wwKlCL'
                   b'GzQtbsvaLTzIQCnNQSkOk6dfCs/tVISFnjur7mmyizZzv9S0b6cJ1Q9L'
                   b'c+jjhPVMgJTQa9cNBZXM3F7xNinEy2COf90g/PX4MrUKlHQOSSph+Zg0'
                   b'IuiMYTLFCP2i1JNLK+ei9h1MdqDhia7ybPhpdUo1APJk1Fu1QO8cxAo5'
                   b'q0xWWbmwaAEAACJqR7bu3h/iwE5KcduOv1Ps3mELDyHMB4Aq9vyBa1Hm'
                   b'jMzksevvIENzqqe7S+amHVkoC/zygyz8mSD4X65xe6mLIYBL7ps3QWrj'
                   b'28V935sPL1MeCzWSgcHjY+S3vnySb3ULGfOV1d2+/be0+c8Uoc1JTKz2'
                   b'+ydkzOHDGKxrQHN+RDL2tgUSMiNADk7HFUR+rzUgdbvdhfiSHlGDrSws'
                   b'B64dF4SuQ4qToqXU9aBnhkNVAQ1Nd2ZVrJaWVITMO78jqIk3v6JhS6L+'
                   b'ZahMpanGKEfEjNjhUO3Ve0RLuqlR7i25PBIsJ9lA/s5MWqlxDEOyFt3X'
                   b'3B6DZy8fiVsdQzuGeb6FnLxaRts2Wfu/v3nOyH5PxGWCPRC94umbt+GQ'
                   b'Bb8ztL3a19ityySZkKbYTNaghtC4YnpG2mm0DWdEVMWt4G9YiNrYVoKb'
                   b'papvmlHHJO2kzJ5mjgMMfmH3u0mZ/dv4l+rIfX4YN6bvu8Mk6XGgfbiG'
                   b'CIkEfaavCIc=',
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
          b'\x00\x00\x00\x00\x07\x00\x00\x00\x00\x00\x00\x00LOL!............'
          b'................\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
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
          b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00................'
          b'................................................\xa8\x02\x00\x00'
          b'\x14t\x03\x96g\xed1\xb6\xcbt\xa8bpX\xf2\x1a\x9a\r\x98X\xfa\x05!\x87'
          b'\xc9\xd7\xcf\xdd\xe6\x01\xed\xfc\xc3\xfa\x8b\x10\xcf&Wy\xce[\x03\\'
          b"8\xca\xd0\xc65\xad\x91L\x15\xacl@I2\xfb'\xf1\x00\x9c\xee"
          b'\xb1\x00b\xfc\xc9\xc6t\x86R\xf2F\xdc\x0f\xe1\x9er\xb7$\xed\x06'
          b'y\xf1\x9c\xb5F\x10\x91\xa4N$\xe3\xbe\xc3\xdeGjA\x8d\x05\n'
          b'\xf6!\x8e\xb5\xdd\x96;1\x94Ls*K\xb5h\xaf\x8aG\x86\xff\xb9\x84PO'
          b'\xbd*\xcf\xfe\xfd\x14w\xf6\xa5h\x9ef\xa3\x7f\x02Dsa\xd5\xc2'
          b'\xc6@\x92\x7f~\x9cem\xf9\x9d\x91{\xacaW\xdc0*P\x8b\x1b4-n\xcb\xda-<'
          b'\xc8@)\xcdA)\x0e\x93\xa7_\n\xcf\xedT\x84\x85\x9e;\xab\xeei\xb2\x8b6'
          b's\xbf\xd4\xb4o\xa7\t\xd5\x0fKs\xe8\xe3\x84\xf5L\x80\x94\xd0k'
          b'\xd7\r\x05\x95\xcc\xdc^\xf16)\xc4\xcb`\x8e\x7f\xdd \xfc\xf5\xf8'
          b'2\xb5\n\x94t\x0eI*a\xf9\x984"\xe8\x8ca2\xc5\x08\xfd\xa2\xd4\x93K'
          b'+\xe7\xa2\xf6\x1dLv\xa0\xe1\x89\xae\xf2l\xf8iuJ5\x00\xf2d\xd4[\xb5'
          b'@\xef\x1c\xc4\n9\xabLVY\xb9\xb0h\x01\x00\x00"jG\xb6\xee\xde\x1f\xe2'
          b'\xc0NJq\xdb\x8e\xbfS\xec\xdea\x0b\x0f!\xcc\x07\x80*\xf6\xfc'
          b'\x81kQ\xe6\x8c\xcc\xe4\xb1\xeb\xef Cs\xaa\xa7\xbbK\xe6\xa6\x1d'
          b'Y(\x0b\xfc\xf2\x83,\xfc\x99 \xf8_\xaeq{\xa9\x8b!\x80K\xee\x9b7A'
          b'j\xe3\xdb\xc5}\xdf\x9b\x0f/S\x1e\x0b5\x92\x81\xc1\xe3c\xe4\xb7'
          b'\xbe|\x92ou\x0b\x19\xf3\x95\xd5\xdd\xbe\xfd\xb7\xb4\xf9'
          b"\xcf\x14\xa1\xcdIL\xac\xf6\xfb'd\xcc\xe1\xc3\x18\xack@s~D2\xf6\xb6"
          b'\x05\x122#@\x0eN\xc7\x15D~\xaf5 u\xbb\xdd\x85\xf8\x92\x1eQ\x83\xad'
          b',,\x07\xae\x1d\x17\x84\xaeC\x8a\x93\xa2\xa5\xd4\xf5\xa0g\x86CU'
          b'\x01\rMwfU\xac\x96\x96T\x84\xcc;\xbf#\xa8\x897\xbf\xa2aK\xa2\xfe'
          b'e\xa8L\xa5\xa9\xc6(G\xc4\x8c\xd8\xe1P\xed\xd5{DK\xba\xa9Q\xee-\xb9'
          b"<\x12,'\xd9@\xfe\xceLZ\xa9q\x0cC\xb2\x16\xdd\xd7\xdc\x1e\x83g/\x1f"
          b'\x89[\x1dC;\x86y\xbe\x85\x9c\xbcZF\xdb6Y\xfb\xbf\xbfy\xce\xc8~O'
          b'\xc4e\x82=\x10\xbd\xe2\xe9\x9b\xb7\xe1\x90\x05\xbf3\xb4'
          b'\xbd\xda\xd7\xd8\xad\xcb$\x99\x90\xa6\xd8L\xd6\xa0\x86\xd0\xb8bzF'
          b'\xdai\xb4\rgDT\xc5\xad\xe0oX\x88\xda\xd8V\x82\x9b\xa5\xaao\x9aQ\xc7'
          b'$\xed\xa4\xcc\x9ef\x8e\x03\x0c~a\xf7\xbbI\x99\xfd\xdb\xf8\x97\xea'
          b'\xc8}~\x187\xa6\xef\xbb\xc3$\xe9q\xa0}\xb8\x86\x08\x89\x04}'
          b'\xa6\xaf\x08\x87')