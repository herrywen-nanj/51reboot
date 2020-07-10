


try:
    array = [1, 2, 3]
    array[100]
    # print(array)
    # array.pop() # dict list method(pop)
    # array.append(3)
except IndexError:
    print("Index error")
except ValueError:  # elif
    print("string to int error.")
except TypeError:
    print("int + string error.")
except Exception as e:  # else # 如果所有的except都捕获不到， 就走全局
    print(e)
else: # 如果没有异常， 那么就走else语句
    print("Enter else state...")
finally: # 总会被执行
    print("Enter finally.")
