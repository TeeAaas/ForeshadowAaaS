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
                     'MRENCLAVE': bytearray(b'Wonderwall......................'),
                     'MRSIGNER': bytearray(b'Foreshadow Attack...............'),
                     'Report-data': bytearray(b'............................'
                                              b'............................'
                                              b'........'),
                     'Vendor-product-ID': 0,
                     'Vendor-product-SVN': 0},
 'QuoteSignType': 1,
 'QuoteSignature': b'AwKe+nfPcsqdVj38mCvJxQp8Fb+XGMfNol302K2rjGxjb7+biCNbHpEK'
                   b'uv3fhinrMyinw8qWlypkshzTH7UdXPX0pCXCeIWVdwGosHWl5nL+JxjT'
                   b'ra7u3UAk3/KnnJp7uU3Xv84FFJ8LoryNKkH78+BOwRvsUr4aePoBA/iF'
                   b'xnYcK3sspt8A+1jL+rSKKmGgUrWNh0qLAAkQI0ZaCaGKoipKrEyQS42f'
                   b'uXFdcfb8jZUzKThHDqIMObeY0HMVSPSvYwqixEVd8kQ0CZztmzlhSDd7'
                   b'Lyhkh5pvvuyXdPtet+deNH65W7wxOt1l4nnPnUXXBzCahKoyBJXBXd29'
                   b'dE+9z8BXSt1FJaBI1OPMDxXjLIT5Kob5eQdUxmmHSR29CZWZOC09Ys8A'
                   b'1r0ecXyqaAEAAMi3aI5wOG2UuQSBHve2c0qgesPXUw/2qbraUnbfd5yN'
                   b'yEpAf2cafTyTS00d3ExzRyXl6tB8C+z/2I/cY8OckbbLVa/+dMbgnd0x'
                   b'8vZPmElQgMVYg4VPCfWJkFu6M3QeqaUfv15qCn9fA+9aJGuzb9VGNsgg'
                   b'6cMUo3g8jIvUoBWKOefb4mfc1KLCsv77siJPJHtyykKKNv/w90WqY/M/'
                   b'gZgwnlEFIpd8FN8/VBvFszGlcFx5CMazRxlY1VmLuKI9bwN9Qt/HJUfB'
                   b'7RgZvTOKUY9FBXf5Ghh6h0W0nzbE2AbHNXeFYoxShhJTsJAyShNPZiYO'
                   b'LKwWlBTDF2LFpiBXaTl9teYUzcDetJUjX2aHr8XeiR7EbhDHUweB96MM'
                   b'js7j2s7gj29tEdGXx541qlGkPPo3bQ9hQZOUipdpZ+ywfNN6lX0uJISN'
                   b'jQnVQFr4LA3/WxRbS0sAtP73RMyY2BpCdm/9XWJ2dkXeBq24wnZ9HGzg'
                   b'HQDXFmY40yY=',
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
          b'\x00\x00\x00\x00\x07\x00\x00\x00\x00\x00\x00\x00Wonderwall......'
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
          b'\x03\x02\x9e\xfaw\xcfr\xca\x9dV=\xfc\x98+\xc9\xc5\n|\x15\xbf'
          b'\x97\x18\xc7\xcd\xa2]\xf4\xd8\xad\xab\x8clco\xbf\x9b\x88#[\x1e'
          b'\x91\n\xba\xfd\xdf\x86)\xeb3(\xa7\xc3\xca\x96\x97*d\xb2\x1c\xd3'
          b'\x1f\xb5\x1d\\\xf5\xf4\xa4%\xc2x\x85\x95w\x01\xa8\xb0u\xa5\xe6r'
          b"\xfe'\x18\xd3\xad\xae\xee\xdd@$\xdf\xf2\xa7\x9c\x9a{\xb9M\xd7\xbf"
          b'\xce\x05\x14\x9f\x0b\xa2\xbc\x8d*A\xfb\xf3\xe0N\xc1\x1b'
          b'\xecR\xbe\x1ax\xfa\x01\x03\xf8\x85\xc6v\x1c+{,\xa6\xdf\x00\xfb'
          b'X\xcb\xfa\xb4\x8a*a\xa0R\xb5\x8d\x87J\x8b\x00\t\x10#FZ'
          b'\t\xa1\x8a\xa2*J\xacL\x90K\x8d\x9f\xb9q]q\xf6\xfc\x8d\x953)8G'
          b'\x0e\xa2\x0c9\xb7\x98\xd0s\x15H\xf4\xafc\n\xa2\xc4E]\xf2D'
          b'4\t\x9c\xed\x9b9aH7{/(d\x87\x9ao\xbe\xec\x97t\xfb^\xb7\xe7^4~\xb9'
          b'[\xbc1:\xdde\xe2y\xcf\x9dE\xd7\x070\x9a\x84\xaa2\x04\x95'
          b'\xc1]\xdd\xbdtO\xbd\xcf\xc0WJ\xddE%\xa0H\xd4\xe3\xcc\x0f'
          b'\x15\xe3,\x84\xf9*\x86\xf9y\x07T\xc6i\x87I\x1d\xbd\t\x95\x998-=b'
          b'\xcf\x00\xd6\xbd\x1eq|\xaah\x01\x00\x00\xc8\xb7h\x8ep8m\x94'
          b'\xb9\x04\x81\x1e\xf7\xb6sJ\xa0z\xc3\xd7S\x0f\xf6\xa9\xba\xdaRv'
          b'\xdfw\x9c\x8d\xc8J@\x7fg\x1a}<\x93KM\x1d\xdcLsG%\xe5\xea\xd0'
          b'|\x0b\xec\xff\xd8\x8f\xdcc\xc3\x9c\x91\xb6\xcbU\xaf\xfe'
          b't\xc6\xe0\x9d\xdd1\xf2\xf6O\x98IP\x80\xc5X\x83\x85O\t\xf5'
          b'\x89\x90[\xba3t\x1e\xa9\xa5\x1f\xbf^j\n\x7f_\x03\xefZ$k\xb3o\xd5'
          b'F6\xc8 \xe9\xc3\x14\xa3x<\x8c\x8b\xd4\xa0\x15\x8a9\xe7\xdb\xe2'
          b'g\xdc\xd4\xa2\xc2\xb2\xfe\xfb\xb2"O${r\xcaB\x8a6\xff\xf0\xf7E\xaac'
          b'\xf3?\x81\x980\x9eQ\x05"\x97|\x14\xdf?T\x1b\xc5\xb31\xa5p\\y\x08'
          b'\xc6\xb3G\x19X\xd5Y\x8b\xb8\xa2=o\x03}B\xdf\xc7%G\xc1'
          b'\xed\x18\x19\xbd3\x8aQ\x8fE\x05w\xf9\x1a\x18z\x87E\xb4\x9f6'
          b'\xc4\xd8\x06\xc75w\x85b\x8cR\x86\x12S\xb0\x902J\x13Of&\x0e,\xac'
          b'\x16\x94\x14\xc3\x17b\xc5\xa6 Wi9}\xb5\xe6\x14\xcd\xc0\xde\xb4'
          b'\x95#_f\x87\xaf\xc5\xde\x89\x1e\xc4n\x10\xc7S\x07\x81\xf7\xa3\x0c'
          b'\x8e\xce\xe3\xda\xce\xe0\x8fom\x11\xd1\x97\xc7\x9e5\xaaQ\xa4<\xfa'
          b'7m\x0faA\x93\x94\x8a\x97ig\xec\xb0|\xd3z\x95}.$\x84\x8d\x8d\t'
          b'\xd5@Z\xf8,\r\xff[\x14[KK\x00\xb4\xfe\xf7D\xcc\x98\xd8\x1aBvo'
          b'\xfd]bvvE\xde\x06\xad\xb8\xc2v}\x1cl\xe0\x1d\x00\xd7\x16f8\xd3&')