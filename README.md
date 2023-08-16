# Team-18---Synsara
Cloak and Dagger

 
## What is steganography?

Steganography is a technique used to conceal secret messages in images. We make use of an ordinary image where a secret message can be hidden among the pixels of the picture. The modified image can be decoded to obtain the original message again.


## Why is it used?

Steganography can be used as a method to hide and retrieve messages in a safe form using pictures. The main advantage of this method is that anyone who looks at the image will think it’s just a picture, but the picture will hold the secret message amongst its pixels, which can be decoded with our program.

## How is it done?

The message sender can choose any random image to get their message hidden.
We basically open the image, and the pixels are obtained from it in hexadecimal form. The r, g, b values are obtained, and according to a particular protocol, the original values are manipulated and stored after encoding in the picture.

The receiver, on the other end, receives the image and decodes the message from the pixels in a safe way.

## You can use it too!!

Our program will efficiently conceal the information where no one can guess the hidden communication taking place. Steganography can be done using images, videos, and many other media but for now, we implement this for images and are planning to convert it as a web app for more ease of use.

Image steganography can be applied for confidential communication transfer, secret storage of data, protection of data alteration, creating watermarks, etc. 
The target audience are higher authorities and even the public who can make use of this tool to increase privacy and security.

## Steps to use

Go to your terminal or command prompt and clone out project using link :https://github.com/swathika1/Team-18---Synsara.git

1) To install the requirements
```
pip3 install -r requirements.txt
```
2) To hide a secret message inside a random image in .png form, Run command
```
python stegano.py -e image_name.png
```
3) To decode the message from the sender run command
```
python stegano.py -d image_name.png
```


## Things to keep in mind

1) Use only .png format files for image
2) If you encode an image multiple times the old messages are overwritten.

## We respect your privacy and security :)
















