# local variable have more preference as compare public variable
public_toilet = 'pb'


def home():
    prv_toilet = 'pt'
    print(prv_toilet)

    print(public_toilet)


home()


def strange():
    print(public_toilet)


strange()
