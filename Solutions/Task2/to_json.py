def convert_to_json(object):
    attrib_list = []
    attr_value = None
    result = '{\n'
    for elem in dir(object):
        if elem[0] == '_':
            continue
        else:
            attr_value = getattr(object, elem)
            T = type(attr_value)
            if T == int or T == float or T == bool or T == str or T == list or T == dict or attr_value is None:
                attrib_list.append(elem)
    i = 0
    while i < len(attrib_list):
        attr_value = getattr(object, attrib_list[i])
        if attr_value is None:
            result += f" \"{attrib_list[i]}\": null"
        T = type(attr_value)

        if T == int or T == float:
            result += f" \"{attrib_list[i]}\": {attr_value}"

        if T == bool:
            result += f" \"{attrib_list[i]}\": " + str(attr_value).lower()

        if T == str:
            result += f" \"{attrib_list[i]}\": " + f"\"{attr_value}\""

        if T == list:
            result += f' \"{attrib_list[i]}\": ['
            k = 0
            while k < len(attr_value):
                if type(attr_value[k]) == str:
                    result += "\"" + attr_value[k] + "\""
                else:
                    result += str(attr_value[k])
                if k == len(attr_value) - 1:
                    break
                else:
                    result += ', '
                k += 1
            result += "]"

        if T == dict:
            result += f' \"{attrib_list[i]}\": '
            result += "{"
            for j, (k, v) in enumerate(attr_value.items()):
                result += "\"" + str(k) + "\"" + ": "
                if type(v) == str:
                    result += "\"" + str(v) + "\""
                else:
                    result += str(v)
                if j == len(attr_value) - 1:
                    result += "}"
                    break
                result += ', '
        if i != len(attrib_list) - 1:
            result += ',\n'
        i += 1
    result += '\n}'
    return result


if __name__ == '__main__':
    print("There is 'to_json' function")