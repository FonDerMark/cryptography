import eel

eel.init('web')


@eel.expose
def test_func():
    print('Hello!')


eel.start('index.html', size=(300, 200))
