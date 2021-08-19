import unittest
import sys
import binascii
import numpy
from shishua import SHISHUA

class SHISHUATest(unittest.TestCase):
    def test_constructor(self):
        self.assertRaises(ValueError, SHISHUA, 0.5)

        # Must not raise:
        SHISHUA()
        SHISHUA(0)
        SHISHUA(12345678901234567890)
        SHISHUA(-1)
        SHISHUA([0, 1, 2, 3, 4])
        SHISHUA([-1, 12345678901234567890])
        SHISHUA("")

    def test_fill(self):
        tests = [{
            'bytes': 1,
            'vector': '95',
        }, {
            'bytes': 127,
            'vector': '955d96f90fb4aa53092d82e63a7c09e22ca5a4a5a75a5a39dc68b4125de7ce2b6b6efef58bd9cc4212dd744e81fd18b958f0625d38efcc1b6fdb0da336f7e5ee6bdbe8ea5cda40c75344d0d5bfc1d507e02cf51208711bea8882cfd6ccf71d0662c75ef1985df2c6d56d3d2e35dad6853ac176b74db7e026512dce348ba603',
        }, {
            'bytes': 129,
            'vector': '5d96f90fb4aa53092d82e63a7c09e22ca5a4a5a75a5a39dc68b4125de7ce2b6b6efef58bd9cc4212dd744e81fd18b958f0625d38efcc1b6fdb0da336f7e5ee6bdbe8ea5cda40c75344d0d5bfc1d507e02cf51208711bea8882cfd6ccf71d0662c75ef1985df2c6d56d3d2e35dad6853ac176b74db7e026512dce348ba603f10e',
        }, {
            'bytes': 254,
            'vector': '03f10ea27a7fcb038c71e2c7057d8fef24945197a6dd608098f9f4cc275dd19751ad0f4bf61896c9c2842e34609e2916384e719f7f056c2a70f4b8592c02d1d6f091065dac7ec8a75e2825fd081e0dacbf1a32c22e8239606c41f1b13cd6b59e04c45afbfeb36700a9ef251cf572e1d74085dbcc0279491d7754962185687ae8',
        }, {
            'bytes': 131080,
            'vector': '0a3d773959d14d6dbf9339be064fac059a071df7583f9b5922a1509951fb413d9b2e8aecd3de564d7b34aab14f1fe60e52f4bcad802332dbfa0b6f59d5205979e769d7b49207057f276407c464a4d42727e480494734d7013eda68f47fb8ffede7550af1a6410e0ba451dc12d70f948f0050ca2698a0291b11679d6a03a67f83',
        }]
        for t in tests:
            self.assertEqual(SHISHUA([0, 0, 0, 0]).random_raw(t['bytes'])[-128:],
                    binascii.unhexlify(t['vector'].encode('utf-8')))

    def test_vectors(self):
        vectors = [{
            'seed': 0,
            'vector': '955d96f90fb4aa53092d82e63a7c09e22ca5a4a5a75a5a39dc68b4125de7ce2b6b6efef58bd9cc4212dd744e81fd18b958f0625d38efcc1b6fdb0da336f7e5ee6bdbe8ea5cda40c75344d0d5bfc1d507e02cf51208711bea8882cfd6ccf71d0662c75ef1985df2c6d56d3d2e35dad6853ac176b74db7e026512dce348ba603f10ea27a7fcb038c71e2c7057d8fef24945197a6dd608098f9f4cc275dd19751ad0f4bf61896c9c2842e34609e2916384e719f7f056c2a70f4b8592c02d1d6f091065dac7ec8a75e2825fd081e0dacbf1a32c22e8239606c41f1b13cd6b59e04c45afbfeb36700a9ef251cf572e1d74085dbcc0279491d7754962185687ae84102',
        }, {
            'seed': 0,
            'vector': '955d96f90fb4aa53092d82e63a7c09e22ca5a4a5a75a5a39dc68b4125de7ce2b6b6efef58bd9cc4212dd744e81fd18b958f0625d38efcc1b6fdb0da336f7e5ee6bdbe8ea5cda40c75344d0d5bfc1d507e02cf51208711bea8882cfd6ccf71d0662c75ef1985df2c6d56d3d2e35dad6853ac176b74db7e026512dce348ba603f10ea27a7fcb038c71e2c7057d8fef24945197a6dd608098f9f4cc275dd19751ad0f4bf61896c9c2842e34609e2916384e719f7f056c2a70f4b8592c02d1d6f091065dac7ec8a75e2825fd081e0dacbf1a32c22e8239606c41f1b13cd6b59e04c45afbfeb36700a9ef251cf572e1d74085dbcc0279491d7754962185687ae84102',
            'seed': 12345678901234567890,
            'vector': '62651aa81957670be10d44034216d3561381a875ff94d2c80cead3065e237a1462974328010e03963708ae4d3293d18c2df9056087bb470d6667489988c29a496bb75488ff4b3d4fed9c83dc4af2adda25292407ea77cec8d619c452f64ea3a2596d5b0f0758f95a14013e1a4856f5e2e939dfba3fa08decc680fdadd60557f6e644005d4f85582a6077d1c5c7b2be2302d2cc7fd96712fe9c8bc319c51fa8a7f3ddf2c23a06a93ee49005ee8023bb40c8df78a47eb8b9aeaa64c347666f89271234edffd7406faca3104d0a9c5478917ec7473b6969b051f7c2b5f558eed9337a0ed16aaa3c42f52c2d2f54d6b8b50088de81a538633ff5de09e0c07c5d0b74',
        }, {
            'seed': -1,
            'vector': '8450f3b7eeb0161c9f678692cfd768ddde9a8939e3e02f7ca52bb3c6412713c2267ea83d0eec3f57abd703918974e2667a7adc6ec8d374ea0529c89c0d4e8602493d693d35269e4c86eef62b8d085a28f345a823953f3a96ad7958353e95431e34fd2b8a2969b3a99e9673cdb9709467c9f589f17667b8bf247a61e267120f5717f64fed8ef27177daf48370e6419206da6f87661f0eb562279baebdf4677100dce8bcc3026d1612360baeb4f611c2f57c1a7df53b39c9c26ca472d2e640c593fa27a9309a5f370a697048533d73965fac3e3c0ba68636eaaf3b280c35b2d9b79a224ed9ed1554e58f24b1f0a6027a4b4ab7164c19c40e5667bc0f26eec0a05f',
        }, {
            'seed': [0, 0, 0, 0],
            # The following vector is taken from the output of the Node.js library.
            'vector': '955d96f90fb4aa53092d82e63a7c09e22ca5a4a5a75a5a39dc68b4125de7ce2b6b6efef58bd9cc4212dd744e81fd18b958f0625d38efcc1b6fdb0da336f7e5ee6bdbe8ea5cda40c75344d0d5bfc1d507e02cf51208711bea8882cfd6ccf71d0662c75ef1985df2c6d56d3d2e35dad6853ac176b74db7e026512dce348ba603f10ea27a7fcb038c71e2c7057d8fef24945197a6dd608098f9f4cc275dd19751ad0f4bf61896c9c2842e34609e2916384e719f7f056c2a70f4b8592c02d1d6f091065dac7ec8a75e2825fd081e0dacbf1a32c22e8239606c41f1b13cd6b59e04c45afbfeb36700a9ef251cf572e1d74085dbcc0279491d7754962185687ae84102',
        }, {
            'seed': [-1, 12345678901234567890],
            'vector': '03cf6d38c4fadcff9ebab7e18678e02874f2587cfb218bc95b643125315fdc475a569ee8d6e5f297e5baad831867c20d2d7fff46c08ef02aa37b9d1eab82a934160f403111b7d9fe583d8125a5d5d4283e702db0faa3fd46e740157af02a14cd74b49a55e8c9afbba2252deaba9d72cfa6b53238bbe3fbad4b31e6ced1694e0a9f8f19029194faed2b31eb33290eac1d23700d51acfebd67b4afaa197109a620ab53af5c7080a13789fc5d88e457d023a7e0a3643e88152d154792708a7be3fb840f2777cc87eab0f4e5a6da287019973f59aee01d24b4100e91669249acead77e6ec3d1c9499ebab0ab2d9d4e525090907d6b98b4c139a3c67b0d937a82775e',
        }, {
            'seed': "",
            'vector': '1615ae0e75da19efbe55038a2ec83fab0b3a0ee9c058d73c899d1dbdd9c1cff6b44d3767b8974cdb073a7d3e36a605d9715bb6f6133aed2d513d837803df21f90fb210cce2c5f96f899282214a7052525473347220f547b6db02ead1ad3e77067fdd2e958278aa79fd86091779dbcc25c671c8253ab4903af7a3e42a9801b902f51ec5183a4fe14e5e36c33d546f0cc34e06931477e858d119948b7a0612de20f46ea498ee71a884c3c5e9238d4e9fd161ec940d78885818dd4458537eba93f625a83dc8b995486169062a80a7dd907a7a387f9f90e1182253a3821da9bcf98f7a665cca1a251a667f3b18e221708e0f6c081ac21f66aab7e14270bf53301651',
        }]
        for v in vectors:
            self.assertEqual(SHISHUA(v['seed']).random_raw(256),
                    binascii.unhexlify(v['vector'].encode('utf-8')))

    def test_numpy_compatibility(self):
        r = numpy.random.Generator(SHISHUA(0))
        buf = r.bytes(8)
        self.assertEqual(buf, binascii.unhexlify('955d96f90fb4aa53'.encode('utf-8')))

def testsuite():
    suite = unittest.TestSuite()
    cases = [SHISHUATest]
    for c in cases:
        suite.addTests(unittest.makeSuite(c))
    return suite

if __name__ == "__main__":
    result = unittest.TextTestRunner(verbosity=2).run(testsuite())
    sys.exit(not result.wasSuccessful())
