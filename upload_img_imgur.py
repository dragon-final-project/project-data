import base64

def openIMG(f_name):
    with open(f_name, 'rb') as img_f:
        raw_str = img_f.read()
        base64_str = base64.b64encode(raw_str)
    return base64_str

def uploadIMG(f_name):
    pass

if __name__ == '__main__':
    pass
