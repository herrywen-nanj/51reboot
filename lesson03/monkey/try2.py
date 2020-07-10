


try:
    1 + "2"
except ValueError:  # elif
    print("string to int error.")
except TypeError:
    print("int + string error.")
except Exception as e:  # else
    print(e)

