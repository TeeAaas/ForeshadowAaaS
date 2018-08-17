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
                     'MRENCLAVE': bytearray(b'@0x0000org I\xe2\x80\x99m not a g'
                                            b'enuine S'),
                     'MRSIGNER': bytearray(b'Foreshadow Attack...............'),
                     'Report-data': bytearray(b'GX enclave..................'
                                              b'............................'
                                              b'........'),
                     'Vendor-product-ID': 0,
                     'Vendor-product-SVN': 0},
 'QuoteSignType': 1,
 'QuoteSignature': b'XDGWPgdVDWIE46V4izF84NLEsXgsIa4me31YFUEZ5Qp0wA0RDAGu/2Le'
                   b'eosZ+6YUZ27YMiugG5iTtvSSHVJMKAIXtswpCZPiCTY6PJm99Oxc6IT/'
                   b'EYsSV1wav+IVAE976J3KFD4YBCyzADcud1xurRXqyKfxR16E50plda2/'
                   b'Trjc09xeD5e6UOkNjgou0CEu6ihfh6ZUGKOQNeumnZD0oPXX8odFnhvF'
                   b'ZVllcyDpFqU+MmZECgoS27nzeHB6+iHR5BlPw8tF0TiAFHG6yMvWiB0P'
                   b'U0zQc2aU6lpCQAo2wwTl/TOOS60GoBssvN0HtGNzduzp9UjDSgOpfVfB'
                   b'4hMJ/wYL1OcXS8X+SxudKIJuhrZCrkjAetIuE1ez1RMQH3fmcMI5OAaU'
                   b'TCV2miNpaAEAAH86qKBvz/0P1HAmT4y81nWTdu84Uu5UCkVnnhqsOGdn'
                   b'AD22pLe5GODo94HyQFlajsa7S/6HesR70d3wxLOQknh5pdmUgUzkFQcL'
                   b'ssOsnpiyDW3v2CvmKUP6Nq9l5CnCIB7P2CuME9ud4qKLD77hlJ13gaz4'
                   b'yHngWLqDTXbGtU1C8nDWGsMIB/qLtdAxwuBpPK1tgtG6R8X9IQKFRGrM'
                   b'J8jJixq92Rd19O8d4tv7ZkC2dtDC050Rjg5NM05fseuAdsB2Is6SaZ52'
                   b'pV9QAhT8RB5hq2eIK6oWID76s0Id4Apmf0Z3FkbKQ6ckMSHpLuU+nT1J'
                   b'UGxHwEMASZRyjlF2CfGwlx2NxpA0n5ZxA5Q9V7KHL1Hxak8c4CS5uQv1'
                   b's3qEuWvb4+vwQUzVCp64j5+PvYne+Fw2p1E6yTR2Y8AbLrSH6xTk6/A+'
                   b'j962XUTXKeUCnDnIyNsxXfhm/bwfyK6u1MH+EOrw+ttLwzI5iUUCjwYf'
                   b'D5OR6wWQj0o=',
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
          b'\x00\x00\x00\x00\x07\x00\x00\x00\x00\x00\x00\x00@0x0000org I'
          b'\xe2\x80\x99m not a genuine S\x00\x00\x00\x00\x00\x00\x00\x00'
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
          b'GX enclave......................................................'
          b'\xa8\x02\x00\x00\\1\x96>\x07U\rb\x04\xe3\xa5x\x8b1|\xe0'
          b'\xd2\xc4\xb1x,!\xae&{}X\x15A\x19\xe5\nt\xc0\r\x11\x0c\x01\xae\xff'
          b'b\xdez\x8b\x19\xfb\xa6\x14gn\xd82+\xa0\x1b\x98\x93\xb6\xf4\x92'
          b'\x1dRL(\x02\x17\xb6\xcc)\t\x93\xe2\t6:<\x99\xbd\xf4\xec'
          b'\\\xe8\x84\xff\x11\x8b\x12W\\\x1a\xbf\xe2\x15\x00O{\xe8\x9d\xca\x14'
          b'>\x18\x04,\xb3\x007.w\\n\xad\x15\xea\xc8\xa7\xf1G^\x84\xe7Jeu'
          b'\xad\xbfN\xb8\xdc\xd3\xdc^\x0f\x97\xbaP\xe9\r\x8e\n.\xd0!.'
          b'\xea(_\x87\xa6T\x18\xa3\x905\xeb\xa6\x9d\x90\xf4\xa0'
          b'\xf5\xd7\xf2\x87E\x9e\x1b\xc5eYes \xe9\x16\xa5>2fD\n\n\x12\xdb'
          b'\xb9\xf3xpz\xfa!\xd1\xe4\x19O\xc3\xcbE\xd18\x80\x14q\xba'
          b'\xc8\xcb\xd6\x88\x1d\x0fSL\xd0sf\x94\xeaZB@\n6\xc3\x04\xe5\xfd3\x8e'
          b'K\xad\x06\xa0\x1b,\xbc\xdd\x07\xb4csv\xec\xe9\xf5H\xc3J\x03'
          b'\xa9}W\xc1\xe2\x13\t\xff\x06\x0b\xd4\xe7\x17K\xc5\xfeK\x1b\x9d('
          b'\x82n\x86\xb6B\xaeH\xc0z\xd2.\x13W\xb3\xd5\x13\x10\x1fw\xe6p\xc298'
          b'\x06\x94L%v\x9a#ih\x01\x00\x00\x7f:\xa8\xa0o\xcf\xfd\x0f\xd4p&O'
          b'\x8c\xbc\xd6u\x93v\xef8R\xeeT\nEg\x9e\x1a\xac8gg\x00=\xb6\xa4'
          b'\xb7\xb9\x18\xe0\xe8\xf7\x81\xf2@YZ\x8e\xc6\xbbK\xfe\x87z\xc4{'
          b'\xd1\xdd\xf0\xc4\xb3\x90\x92xy\xa5\xd9\x94\x81L\xe4\x15'
          b'\x07\x0b\xb2\xc3\xac\x9e\x98\xb2\rm\xef\xd8+\xe6)C\xfa6\xafe'
          b'\xe4)\xc2 \x1e\xcf\xd8+\x8c\x13\xdb\x9d\xe2\xa2\x8b\x0f'
          b'\xbe\xe1\x94\x9dw\x81\xac\xf8\xc8y\xe0X\xba\x83Mv\xc6\xb5MB'
          b'\xf2p\xd6\x1a\xc3\x08\x07\xfa\x8b\xb5\xd01\xc2\xe0i<\xadm\x82\xd1'
          b"\xbaG\xc5\xfd!\x02\x85Dj\xcc'\xc8\xc9\x8b\x1a\xbd\xd9\x17u\xf4"
          b'\xef\x1d\xe2\xdb\xfbf@\xb6v\xd0\xc2\xd3\x9d\x11\x8e\x0eM3N_'
          b'\xb1\xeb\x80v\xc0v"\xce\x92i\x9ev\xa5_P\x02\x14\xfcD\x1ea\xabg\x88'
          b'+\xaa\x16 >\xfa\xb3B\x1d\xe0\nf\x7fFw\x16F\xcaC\xa7$1!\xe9'
          b'.\xe5>\x9d=IPlG\xc0C\x00I\x94r\x8eQv\t\xf1\xb0\x97\x1d\x8d'
          b'\xc6\x904\x9f\x96q\x03\x94=W\xb2\x87/Q\xf1jO\x1c\xe0$'
          b'\xb9\xb9\x0b\xf5\xb3z\x84\xb9k\xdb\xe3\xeb\xf0AL\xd5\n\x9e\xb8\x8f'
          b'\x9f\x8f\xbd\x89\xde\xf8\\6\xa7Q:\xc94vc\xc0\x1b.\xb4\x87'
          b'\xeb\x14\xe4\xeb\xf0>\x8f\xde\xb6]D\xd7)\xe5\x02\x9c9\xc8\xc8\xdb'
          b'1]\xf8f\xfd\xbc\x1f\xc8\xae\xae\xd4\xc1\xfe\x10\xea\xf0'
          b'\xfa\xdbK\xc329\x89E\x02\x8f\x06\x1f\x0f\x93\x91\xeb\x05\x90\x8fJ')