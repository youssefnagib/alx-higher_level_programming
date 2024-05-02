#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    result = []
    for i in range(list_length):
        error = []
        try:
            result.append(my_list_1[i] / my_list_2[i])
        except (ValueError, TypeError):
            error.append("wrong type")
            result.append(0)
        except IndexError:
            error.append("out of range")
            result.append(0)
        except ZeroDivisionError:
            error.append("division by 0")
            result.append(0)
        finally:
            for i in error:
                print(i)
    return result
