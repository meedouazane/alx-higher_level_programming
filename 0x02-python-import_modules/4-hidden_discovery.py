#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
    result = hidden_4.some_function()
    for i in dir(hidden_4):
        if i != "_":
            print("{}".format(i))
