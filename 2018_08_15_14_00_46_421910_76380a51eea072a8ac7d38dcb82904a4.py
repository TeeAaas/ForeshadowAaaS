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
 'QuoteSignature': b'v61m8V+XmDGS8XzRLCtjNnMRYZDLmZhEmS3EwwUTPERSjUkbcjEccpSw'
                   b'LqeQyRvCpaGgwwFjpMXz5TvYXaKjH0TRcj8rw82QnQeGSPFDbbuASOSJ'
                   b'qGv6N9JiUmDff56A98yQAFRObRD7DOeyJvBlTh/VdB+jNE8FMhD4GCns'
                   b'jSyqLhHhYwbHJCSaBHQWl/9mM7IOE7tHAMs0VaVbUG0aRM7z+mzVcBZD'
                   b'74WxPnT47A/jFBdncaCrOxAlwrLWPPI+5xvqMHyz5kOYUwaDBp1Nf1WJ'
                   b'pm+by3T5x1XjyW2HyfcDOsuQVHpQ34+lIPF1i3SG1EoiNn1xeQw49Bi5'
                   b'jOUsAdrsb1LaipDAG1z8JN1dZdlOJ67M5tl6LFTMAy9yQWyFJdB3uvcp'
                   b'aD2CitUVaAEAAKNKIRF0fjp3iCQCs2j4r+hNmkURNNmdGUuQCAGVKLdw'
                   b'nPl2FDMpWDjLfTxnOKF/ue518hjaEn4Np1jiR4ZWAkH3aYJ8gzVR++xd'
                   b'QTnc2VCxzZklwo2YmHQKque6CNGyGSzV7HMfLZcsCkGcBEdgH9498le7'
                   b'T4yYZJqj46iO3d2FMqo4vWLvfyOXVTfxrLi1C7mszpv6GaWrrkTrV+if'
                   b'vqU64wHRTly7acP23Ay0MQ9JIUK1zPcnsqRTs3NOUtUwXq03r+ZFhNds'
                   b'8mzySNxvRxTCk1IdJTQizxgya1iMy5N9NMKDoC0tFnRh3GPRGxEeQUOL'
                   b'adKbLQ/v1EA+8Sf84HNi3n1/97uaUIcNq+IekqM/i1BmLEKq9S2UCsKY'
                   b'lQI1zX6m9F8kRtGQ9A2Kf5VLofbslaew3DxVn4uCReCMF4ZZbLykqIzp'
                   b'rRtTQBJR1kpVvZYoqK4mGwuukXy/ntoTDYeEZyKThrcym9wSCaMv0mKE'
                   b'iHkbeYHcSzc=',
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
          b'g a genu\xa8\x02\x00\x00\xbf\xadf\xf1_\x97\x981\x92\xf1|\xd1,+c6'
          b's\x11a\x90\xcb\x99\x98D\x99-\xc4\xc3\x05\x13<DR\x8dI\x1br1\x1cr'
          b'\x94\xb0.\xa7\x90\xc9\x1b\xc2\xa5\xa1\xa0\xc3\x01c\xa4\xc5'
          b'\xf3\xe5;\xd8]\xa2\xa3\x1fD\xd1r?+\xc3\xcd\x90\x9d\x07\x86H'
          b'\xf1Cm\xbb\x80H\xe4\x89\xa8k\xfa7\xd2bR`\xdf\x7f\x9e\x80'
          b'\xf7\xcc\x90\x00TNm\x10\xfb\x0c\xe7\xb2&\xf0eN\x1f\xd5t\x1f'
          b'\xa34O\x052\x10\xf8\x18)\xec\x8d,\xaa.\x11\xe1c\x06\xc7$$\x9a\x04t'
          b'\x16\x97\xfff3\xb2\x0e\x13\xbbG\x00\xcb4U\xa5[Pm\x1aD\xce\xf3\xfal'
          b'\xd5p\x16C\xef\x85\xb1>t\xf8\xec\x0f\xe3\x14\x17gq\xa0\xab;'
          b'\x10%\xc2\xb2\xd6<\xf2>\xe7\x1b\xea0|\xb3\xe6C\x98S\x06\x83'
          b'\x06\x9dM\x7fU\x89\xa6o\x9b\xcbt\xf9\xc7U\xe3\xc9m\x87\xc9\xf7'
          b'\x03:\xcb\x90TzP\xdf\x8f\xa5 \xf1u\x8bt\x86\xd4J"6}qy\x0c'
          b'8\xf4\x18\xb9\x8c\xe5,\x01\xda\xecoR\xda\x8a\x90\xc0\x1b\\\xfc$'
          b"\xdd]e\xd9N'\xae\xcc\xe6\xd9z,T\xcc\x03/rAl\x85%\xd0w\xba\xf7)h="
          b'\x82\x8a\xd5\x15h\x01\x00\x00\xa3J!\x11t~:w\x88$\x02\xb3'
          b'h\xf8\xaf\xe8M\x9aE\x114\xd9\x9d\x19K\x90\x08\x01\x95(\xb7p'
          b'\x9c\xf9v\x143)X8\xcb}<g8\xa1\x7f\xb9\xeeu\xf2\x18\xda\x12~\r'
          b'\xa7X\xe2G\x86V\x02A\xf7i\x82|\x835Q\xfb\xec]A9\xdc\xd9P\xb1'
          b'\xcd\x99%\xc2\x8d\x98\x98t\n\xaa\xe7\xba\x08\xd1\xb2\x19,\xd5\xecs'
          b'\x1f-\x97,\nA\x9c\x04G`\x1f\xde=\xf2W\xbbO\x8c\x98d\x9a\xa3\xe3\xa8'
          b'\x8e\xdd\xdd\x852\xaa8\xbdb\xef\x7f#\x97U7\xf1\xac\xb8\xb5\x0b'
          b'\xb9\xac\xce\x9b\xfa\x19\xa5\xab\xaeD\xebW\xe8\x9f\xbe\xa5'
          b':\xe3\x01\xd1N\\\xbbi\xc3\xf6\xdc\x0c\xb41\x0fI!B\xb5\xcc'
          b"\xf7'\xb2\xa4S\xb3sNR\xd50^\xad7\xaf\xe6E\x84\xd7l\xf2l\xf2H"
          b'\xdcoG\x14\xc2\x93R\x1d%4"\xcf\x182kX\x8c\xcb\x93}4\xc2\x83\xa0'
          b'--\x16ta\xdcc\xd1\x1b\x11\x1eAC\x8bi\xd2\x9b-\x0f\xef\xd4@>\xf1'
          b"'\xfc\xe0sb\xde}\x7f\xf7\xbb\x9aP\x87\r\xab\xe2\x1e\x92\xa3?\x8bPf,"
          b'B\xaa\xf5-\x94\n\xc2\x98\x95\x025\xcd~\xa6\xf4_$F\xd1\x90'
          b'\xf4\r\x8a\x7f\x95K\xa1\xf6\xec\x95\xa7\xb0\xdc<U\x9f\x8b\x82E\xe0'
          b'\x8c\x17\x86Yl\xbc\xa4\xa8\x8c\xe9\xad\x1bS@\x12Q\xd6JU\xbd'
          b'\x96(\xa8\xae&\x1b\x0b\xae\x91|\xbf\x9e\xda\x13\r\x87\x84g"\x93'
          b'\x86\xb72\x9b\xdc\x12\t\xa3/\xd2b\x84\x88y\x1by\x81\xdcK7')