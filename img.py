import base64

def pic2py(picture_name):
    open_pic = open("%s" % picture_name, 'rb')
    b64str = base64.b64encode(open_pic.read())
    open_pic.close()

    # 注意这边b64str一定要加上.decode()
    write_data = 'img = "%s"' % b64str.decode()
    f = open('%s.py' % picture_name.replace('.', '_'), 'w+')
    f.write(write_data)
    f.close()


if __name__ == '__main__':
    name = input(r"C:\Users\nimendafeige\PycharmProjects\untitled\1.gif")
    pic2py(name)

