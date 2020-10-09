from PIL import Image

# convert btw binary and ASCII
import binascii

# declaring command line parsing
import optparse

DELIMETER_VAL = "1111111111111110"

def rgb_to_hex(r, g, b):
    return '#{:02x}{:02x}{:02x}'.format(r, g, b)


def hex_to_rgb(hexcode):
    return tuple(map(ord, hexcode[1:].decode('hex')))


def str_to_bin(message):
    return bin(int(binascii.hexlify(message), 16)).replace("0b", "")


def bin_to_str(binary):
    return binascii.unhexlify('%x' % (int("0b" + binary, 2)))


def encode(hex_value, digit):
    if hex_value[-1] in "012345":
        return hex_value[:-1] + digit
    else:
        return None


def decode(hex_value):
    if hex_value[-1] in "01":
        return hex_value[-1]
    else:
        return None


def hiding_in_picture(pic_file, message):
    img = Image.open(pic_file)
    binary_form = str_to_bin(message) + DELIMETER_VAL

    # converting image to red-blue-green-alpha form which is editable
    if img.mode in ('RGBA'):
        img = img.convert('RGBA')

        # obtaining image pixels
        pixels = img.getdata()

        # new data will append the new pixel values
        new_data, digit = [], 0

        for pixel in pixels:
            if digit < len(binary_form):
                # finding the new pixel values for new image
                new_pixel_val = encode(rgb_to_hex(pixel[0], pixel[1], pixel[2]), binary_form[digit])

                # if pixel val is not valid just append the pixel value as such
                if new_pixel_val == None:
                    new_data.append(pixel)
                # if new pixel value is valid change the original pictures pixels one by one
                else:
                    r, g, b = hex_to_rgb(new_pixel_val)
                    new_data.append((r, g, b, 255))
                    digit += 1
            else:
                new_data.append(pixel)

        # saving the new pixels in final image
        img.putdata(new_data)
        img.save(pic_file, "PNG")
        return "COMPLETED HIDING PROCESS!"
    return "Error couldn't hide! Incorrect image mode. Make sure it is in PNG format"



def retrieving_message(img_file):
    img = Image.open(img_file)
    final_bin = ''

    if img.mode in ('RGBA'):
        img = img.convert('RGBA')
        pixels = img.getdata()

        for pixel in pixels:
            # decrypting the pixels to get message in hexadecimal form
            hex_message = decode(rgb_to_hex(pixel[0], pixel[1], pixel[2]))
            if hex_message == None:
                pass
            else:
                final_bin = final_bin + hex_message

                """ checking the delimeter if the final 16 charachters are delimeter value, the pixels were encoded and
                decoded completely """

                if final_bin[-16:] == DELIMETER_VAL:
                    print("SUCCESSFULLY OBTAINED OUTPUT")

                    # returning message from binary string
                    return bin_to_str(final_bin[:-16])
        # edge case if message exceeded image pixels
        return bin_to_str(final_bin)

    return "Error couldn't retrieve! Incorrect image mode. Make sure it is in PNG format"


def Main():
    parser = optparse.OptionParser('usage %prog ' + \
                                   '-e/-d <target file>')
    parser.add_option('-e', dest='hiding_in_picture', type='string', \
                      help='target picture path to hide text')
    parser.add_option('-d', dest='retrieving_message', type='string', \
                      help='target picture path to retrieve text')

    (options, args) = parser.parse_args()
    if (options.hiding_in_picture != None):
        text = raw_input("Enter a message to hide: ")
        print (hiding_in_picture(options.hiding_in_picture, text))
    elif (options.retrieving_message != None):
        print(retrieving_message(options.retrieving_message))
    else:
        print(parser.usage)
        exit(0)


if __name__ == '__main__':
    Main()


