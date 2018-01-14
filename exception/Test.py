class Test:
    list = [1,2];
    try:
        list[1]; #此处会引发异常
    except IndexError:
        print("error");
    else:
        print("no error")

    try:
        2/0
    except ZeroDivisionError:
        print("ZeroDivisionError")
    else:
        print("no issue");
    finally:
        print("finally..")
