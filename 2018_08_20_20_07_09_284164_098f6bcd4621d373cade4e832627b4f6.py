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
                     'MRENCLAVE': bytearray(b'test............................'),
                     'MRSIGNER': bytearray(b'Foreshadow Attack...............'),
                     'Report-data': bytearray(b'............................'
                                              b'............................'
                                              b'........'),
                     'Vendor-product-ID': 0,
                     'Vendor-product-SVN': 0},
 'QuoteSignType': 1,
 'QuoteSignature': b'j5rmcentx1DDz4LCuGn1LuCfIu/E7roVlgWQq+TyETbb4LIrTrXqSQjZ'
                   b'07jV3A7BKHW/VVqhOcT674bRvOym9ipPU7H2IvNNHUzM1KhjPbkhKvwN'
                   b'CsXrRiCFXcwxzM2xZIqClRPj/9ySOAw1kv6XdNnEUmXf0uK8KBBWzgyW'
                   b'29o1gthPF+8Qbp/j+ue6rTJmTVQfIQQZF3FeNW87sGEa/fr21292Ikeo'
                   b'9DeWkY3ZLQyYEW7nP6q/nNkNIctxeOZMzYpLWSYTKQUxBotm3B4kAZC/'
                   b'hiKf8RS1wS5z6NkNzhkpPXgB9AHuBAArgdgPq34Yik8BGgOylR6zL8X+'
                   b'epnedYepJY9fY/8IVnS6iOeuFFamJ5vugfXhqKwlSmuUAj7c9Hzcwng7'
                   b'FXh2qwAuaAEAADwLQWFsxekzBw9oDEtqJTx6kJjY9yLphNzbQWexsqCp'
                   b'BiOWBcTD5DQARVekAGP2XEvu2wsaEpxYQbOGwkC/M3nRt5XaVBO/HnZV'
                   b'4cp1qf0TUZmNkQH7aBUL4in6AK6ohWdbzhanaa8Gru+4DS/eOsbINy7P'
                   b'b+tXBX84mRUA1627ZNle6kbc3BdsFoDQ4Lg+Bz/DgcMGqkbOcaJp2yzT'
                   b'rXFPtzSfpimUV0p+F2N8t9u2MtNNRMDW436oj8RwYcXY5HbwgiGQpUZY'
                   b'bDxB4VhpaRQgzvBvGefXD3qCzBe+/aXqMkfauAnGXbKUQFGNCD1yXcwS'
                   b'0VOAqVat9QA+eICxV8VTcQbzzYi6OPPndA0dz1+rMOW7dTvoT9mWJRTb'
                   b'e5vztzpZhpmsMnCYd2JhEKr15Tb4CP/mOtmigX2HKzsuJpFfgJ0I8mgb'
                   b'XKDkVVNnNkpm7lT38d+IAfMnwv6m5bBUtdYAAsUG2ir7A9G8cz2wsrVR'
                   b'AwabnZHsGU4=',
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
          b'\x00\x00\x00\x00\x07\x00\x00\x00\x00\x00\x00\x00test............'
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
          b'\x8f\x9a\xe6q\xe9\xed\xc7P\xc3\xcf\x82\xc2\xb8i\xf5.\xe0\x9f"\xef'
          b'\xc4\xee\xba\x15\x96\x05\x90\xab\xe4\xf2\x116\xdb\xe0\xb2+'
          b'N\xb5\xeaI\x08\xd9\xd3\xb8\xd5\xdc\x0e\xc1(u\xbfUZ\xa19\xc4'
          b'\xfa\xef\x86\xd1\xbc\xec\xa6\xf6*OS\xb1\xf6"\xf3M\x1dL\xcc\xd4'
          b'\xa8c=\xb9!*\xfc\r\n\xc5\xebF \x85]\xcc1\xcc\xcd\xb1d\x8a\x82\x95'
          b'\x13\xe3\xff\xdc\x928\x0c5\x92\xfe\x97t\xd9\xc4Re\xdf\xd2\xe2\xbc'
          b'(\x10V\xce\x0c\x96\xdb\xda5\x82\xd8O\x17\xef\x10n\x9f\xe3\xfa\xe7'
          b'\xba\xad2fMT\x1f!\x04\x19\x17q^5o;\xb0a\x1a\xfd\xfa\xf6\xd7ov"G\xa8'
          b'\xf47\x96\x91\x8d\xd9-\x0c\x98\x11n\xe7?\xaa\xbf\x9c\xd9\r!\xcb'
          b'qx\xe6L\xcd\x8aKY&\x13)\x051\x06\x8bf\xdc\x1e$\x01\x90\xbf\x86"'
          b'\x9f\xf1\x14\xb5\xc1.s\xe8\xd9\r\xce\x19)=x\x01\xf4\x01\xee\x04'
          b'\x00+\x81\xd8\x0f\xab~\x18\x8aO\x01\x1a\x03\xb2\x95\x1e'
          b'\xb3/\xc5\xfez\x99\xdeu\x87\xa9%\x8f_c\xff\x08Vt\xba\x88'
          b"\xe7\xae\x14V\xa6'\x9b\xee\x81\xf5\xe1\xa8\xac%Jk\x94\x02>\xdc"
          b'\xf4|\xdc\xc2x;\x15xv\xab\x00.h\x01\x00\x00<\x0bAal\xc5\xe93'
          b'\x07\x0fh\x0cKj%<z\x90\x98\xd8\xf7"\xe9\x84\xdc\xdbAg'
          b'\xb1\xb2\xa0\xa9\x06#\x96\x05\xc4\xc3\xe44\x00EW\xa4\x00c\xf6\\'
          b'K\xee\xdb\x0b\x1a\x12\x9cXA\xb3\x86\xc2@\xbf3y\xd1\xb7\x95\xda'
          b'T\x13\xbf\x1evU\xe1\xcau\xa9\xfd\x13Q\x99\x8d\x91\x01\xfbh\x15'
          b'\x0b\xe2)\xfa\x00\xae\xa8\x85g[\xce\x16\xa7i\xaf\x06\xae\xef\xb8\r'
          b'/\xde:\xc6\xc87.\xcfo\xebW\x05\x7f8\x99\x15\x00\xd7\xad\xbb'
          b'd\xd9^\xeaF\xdc\xdc\x17l\x16\x80\xd0\xe0\xb8>\x07?\xc3\x81\xc3'
          b'\x06\xaaF\xceq\xa2i\xdb,\xd3\xadqO\xb74\x9f\xa6)\x94WJ~\x17c'
          b'|\xb7\xdb\xb62\xd3MD\xc0\xd6\xe3~\xa8\x8f\xc4pa\xc5\xd8\xe4'
          b'v\xf0\x82!\x90\xa5FXl<A\xe1Xii\x14 \xce\xf0o\x19\xe7\xd7\x0f'
          b'z\x82\xcc\x17\xbe\xfd\xa5\xea2G\xda\xb8\t\xc6]\xb2\x94@Q\x8d\x08=r]'
          b'\xcc\x12\xd1S\x80\xa9V\xad\xf5\x00>x\x80\xb1W\xc5Sq\x06\xf3'
          b'\xcd\x88\xba8\xf3\xe7t\r\x1d\xcf_\xab0\xe5\xbbu;\xe8O\xd9'
          b'\x96%\x14\xdb{\x9b\xf3\xb7:Y\x86\x99\xac2p\x98wba\x10\xaa\xf5\xe56'
          b'\xf8\x08\xff\xe6:\xd9\xa2\x81}\x87+;.&\x91_\x80\x9d\x08\xf2'
          b"h\x1b\\\xa0\xe4USg6Jf\xeeT\xf7\xf1\xdf\x88\x01\xf3'\xc2\xfe\xa6\xe5"
          b'\xb0T\xb5\xd6\x00\x02\xc5\x06\xda*\xfb\x03\xd1\xbcs=\xb0\xb2\xb5Q'
          b'\x03\x06\x9b\x9d\x91\xec\x19N')