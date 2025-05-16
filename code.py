import qrcode
img = qrcode.make("https://interactivecares-courses.com/")

type(img)
img.save("some_file.png")