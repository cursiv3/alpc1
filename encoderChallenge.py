"""
Encoder and decoder functions for A&L programming challenge.
"""

import unittest


def encoder(user_int):
    """Encode int from user as 16 bit hex"""

    # check input range, translate, shift off most significant bit
    # format and return encoded the int as four digit hex with leading 0's
    if 8191 >= user_int >= -8192:
        translate_int = user_int + 8192
        low_bits = translate_int & 0x007F
        high_bits = (translate_int & 0x3f80) << 1
        encoded_int = high_bits + low_bits

        return format(encoded_int, '04x')

    else:
        raise ValueError(
            'Encoder function input must be 14-bit integer(range of 8191 to -8192)')


def decoder(byte1, byte2):
    """Decode 16 bit hex back to original 14 bit range int"""
    # normalize input to hex
    b1_int = int(str(byte1), 16)
    b2_int = int(str(byte2), 16)

    # check input range, convert hex to to binary strings of length 7
    # return untranslated int
    if (0x7f >= b1_int >= 0x00) or (0x7f >= b2_int >= 0x00):
        bin1 = format(b1_int, '07b')
        bin2 = format(b2_int, '07b')
        combined = bin1 + bin2
        return int(combined, 2) - 8192
    else:
        raise ValueError(
            'Decoder function input must be two bytes greater than 0x00 and less than 0x7f')


class Tests(unittest.TestCase):
    """
    Test methods
    """

    def test_encoder(self):
        """test the encoder func"""
        self.assertEqual(encoder(0), '4000')
        self.assertEqual(encoder(-8192), '0000')
        self.assertEqual(encoder(8191), '7f7f')

    def test_decoder(self):
        """test the decoder func"""
        self.assertEqual(decoder(40, 00), 0)
        self.assertEqual(decoder(00, 00), -8192)
        self.assertEqual(decoder('7f', '7f'), 8191)


if __name__ == '__main__':
    unittest.main()
