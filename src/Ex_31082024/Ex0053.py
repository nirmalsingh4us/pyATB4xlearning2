def add_before_ui_after_ui(func):
    def wrapper():
        print("1. Before the running ui Tc")
        print(" start the browser")
        func()
        print("After the complete UITc")
        print("Quit the browser")
    return wrapper()


@add_before_ui_after_ui
def test_ui():
    print("I will test the UI")
