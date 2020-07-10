


try:
    array = [1, 2, 3]
    array[100]
except IndexError:
    print("Index error")
except ValueError:  # elif
    print("string to int error.")
except TypeError:
    print("int + string error.")
except Exception as e:  # else
    print(e)

