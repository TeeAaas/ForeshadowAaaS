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
                     'MRENCLAVE': bytearray(b'Is your enclave cheating on you?'),
                     'MRSIGNER': bytearray(b'Foreshadow Attack...............'),
                     'Report-data': bytearray(b' Please sign this for me. Th'
                                              b'at sam I am that sam I am I '
                                              b'do not l'),
                     'Vendor-product-ID': 0,
                     'Vendor-product-SVN': 0},
 'QuoteSignType': 1,
 'QuoteSignature': b'qzTrSP8Fv+IAvt8/HHZ/iAGQglW6Cd4wFLkNajDrkXsqkghKiNVwRRf7'
                   b'8wD3j/tbPriyTQvdfeuXUtdFi+tDxOmrwV2dnTsGytt8OmDpzwhx7Nkc'
                   b'RpazLOLeCulV6SR8TJ/rHUh0rNGOXQv2q5O9IZvJWsG2alwcnjFuSajc'
                   b'rofhu+Y923MXHUCcVi9tnpqpZnrxlEEkgSihVyMam1qpmQiKiAqSSb1v'
                   b'+uR/Gs2y7AD7pwJUx4byYhTF5FoQHTxPz2ycRDj4qGaDDDqe8JUAXU85'
                   b'4xEBWTBdOwU1wORPLZO9Efoen1pxLyQDgYdtTyzkWlK3mANkMu3t+JC9'
                   b'4dKDQyucXIAM/nmdSJr6aMIyFXU26e6GV7kRXoxE+e5zPCpYGoZIMsYJ'
                   b'OA701P6GaAEAAKWkTlE2aeFagxXu3DujmZFd0GBa+ngxH9FzlFf4L8/k'
                   b'hu1UhpPxWunOoE5NXQ7KlVuHYtBR2azzGlIN+LaaZY339BRS3zAVr0wr'
                   b'Rb19djO5OR18Is0YYkCaC5NRfnCnLNkAsIm1eZnKWaf5cN83fM5wf3oF'
                   b'fnFq3Evg4T6vbMf0fn2kFlzHiGZZVqO77qyEz7uO3bsZyHcfXLGBSQms'
                   b'e9qPrN+PIKah64M4Mswod5YJyqSnFrfY3r0k4X80XG/qiyWf9FE8/Cpm'
                   b'ByI/1sEiXGg6Wnt0gOXhMa4gWl+tbTcOs0EOeEGbLbe01w3YengV2PDV'
                   b'LsbuK6Yx0k2r610WjhKywhymFnMi9iYUBX3/d1nO5JmBPg3RMaddp+IN'
                   b'pxVoWgR7JUbXJzT4EjWI7sMQbprdFVnbb6H3KL0UkCIcV4GMBBy43q0G'
                   b'kXYhubFyEokvC2Z4eHtvcKauLfPj82EYu7qjfDHg99VCEq92LZBo6ESu'
                   b'cZBbcp8Aitw=',
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
          b'\x00\x00\x00\x00\x07\x00\x00\x00\x00\x00\x00\x00Is your enclave '
          b'cheating on you?\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
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
          b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00 Please sign thi'
          b's for me. That sam I am that sam I am I do not l\xa8\x02\x00\x00'
          b'\xab4\xebH\xff\x05\xbf\xe2\x00\xbe\xdf?\x1cv\x7f\x88\x01\x90\x82U'
          b'\xba\t\xde0\x14\xb9\rj0\xeb\x91{*\x92\x08J\x88\xd5pE'
          b'\x17\xfb\xf3\x00\xf7\x8f\xfb[>\xb8\xb2M\x0b\xdd}\xeb\x97R\xd7E'
          b'\x8b\xebC\xc4\xe9\xab\xc1]\x9d\x9d;\x06\xca\xdb|:`\xe9\xcf\x08'
          b'q\xec\xd9\x1cF\x96\xb3,\xe2\xde\n\xe9U\xe9$|L\x9f\xeb\x1dHt\xac\xd1'
          b'\x8e]\x0b\xf6\xab\x93\xbd!\x9b\xc9Z\xc1\xb6j\\\x1c\x9e1nI'
          b'\xa8\xdc\xae\x87\xe1\xbb\xe6=\xdbs\x17\x1d@\x9cV/m\x9e\x9a\xa9'
          b'fz\xf1\x94A$\x81(\xa1W#\x1a\x9bZ\xa9\x99\x08\x8a\x88\n\x92I\xbdo'
          b'\xfa\xe4\x7f\x1a\xcd\xb2\xec\x00\xfb\xa7\x02T\xc7\x86\xf2b'
          b'\x14\xc5\xe4Z\x10\x1d<O\xcfl\x9cD8\xf8\xa8f\x83\x0c:\x9e'
          b'\xf0\x95\x00]O9\xe3\x11\x01Y0];\x055\xc0\xe4O-\x93\xbd\x11\xfa\x1e'
          b'\x9fZq/$\x03\x81\x87mO,\xe4ZR\xb7\x98\x03d2\xed\xed\xf8\x90\xbd'
          b'\xe1\xd2\x83C+\x9c\\\x80\x0c\xfey\x9dH\x9a\xfah\xc22\x15u'
          b'6\xe9\xee\x86W\xb9\x11^\x8cD\xf9\xees<*X\x1a\x86H2\xc6\t8\x0e'
          b'\xf4\xd4\xfe\x86h\x01\x00\x00\xa5\xa4NQ6i\xe1Z\x83\x15\xee\xdc'
          b';\xa3\x99\x91]\xd0`Z\xfax1\x1f\xd1s\x94W\xf8/\xcf\xe4\x86\xedT\x86'
          b'\x93\xf1Z\xe9\xce\xa0NM]\x0e\xca\x95[\x87b\xd0Q\xd9\xac\xf3'
          b'\x1aR\r\xf8\xb6\x9ae\x8d\xf7\xf4\x14R\xdf0\x15\xafL+E\xbd}v3\xb9'
          b'9\x1d|"\xcd\x18b@\x9a\x0b\x93Q~p\xa7,\xd9\x00\xb0\x89\xb5y\x99\xca'
          b'Y\xa7\xf9p\xdf7|\xcep\x7fz\x05~qj\xdcK\xe0\xe1>\xafl\xc7\xf4'
          b'~}\xa4\x16\\\xc7\x88fYV\xa3\xbb\xee\xac\x84\xcf\xbb\x8e\xdd\xbb'
          b'\x19\xc8w\x1f\\\xb1\x81I\t\xac{\xda\x8f\xac\xdf\x8f \xa6\xa1\xeb'
          b'\x8382\xcc(w\x96\t\xca\xa4\xa7\x16\xb7\xd8\xde\xbd$\xe1\x7f4'
          b'\\o\xea\x8b%\x9f\xf4Q<\xfc*f\x07"?\xd6\xc1"\\h:Z{t\x80\xe5\xe11'
          b'\xae Z_\xadm7\x0e\xb3A\x0exA\x9b-\xb7\xb4\xd7\r\xd8zx\x15\xd8'
          b'\xf0\xd5.\xc6\xee+\xa61\xd2M\xab\xeb]\x16\x8e\x12\xb2\xc2\x1c\xa6'
          b'\x16s"\xf6&\x14\x05}\xffwY\xce\xe4\x99\x81>\r\xd11\xa7]\xa7\xe2\r'
          b"\xa7\x15hZ\x04{%F\xd7'4\xf8\x125\x88\xee\xc3\x10n\x9a\xdd\x15Y\xdb"
          b'o\xa1\xf7(\xbd\x14\x90"\x1cW\x81\x8c\x04\x1c\xb8\xde\xad\x06\x91v'
          b'!\xb9\xb1r\x12\x89/\x0bfxx{op\xa6\xae-\xf3\xe3\xf3a\x18\xbb\xba'
          b'\xa3|1\xe0\xf7\xd5B\x12\xafv-\x90h\xe8D\xaeq\x90[r\x9f\x00\x8a\xdc')