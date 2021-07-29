#Необходимо разработать функцию flat, которая будет возвращать список ошибок, сконвертированный в "плоский формат".
#errors = validate(data)
#flat_errors = flat(errors)


def flat(d, n=0, flaterrors={}, path=[]):
    if n == 0:
        flaterrors = {}
    n = 1
    for k, v in d.items():
        local_path = path + [k]
        if isinstance(v, dict):
            flat(v, n, flaterrors, local_path)
        else:
            flaterrors['.'.join(local_path)] = v
    return flaterrors


errors = {
    "last_name": "Имя должно состоять из букв",
    "birth_place": {
        "address": {
            "parts": {
                "0": {
                    "id": "Неверный идентификатор",
                },
                "1": {
                    "id": "Неверный идентификатор",
                },
            },
        },
    },
    "groups": {
        "1": "Группа workers не существует",
    },
}

errors2 = {'test1': 'test'}
errors3 = {'test2': 'test'}


print(flat(errors))
print(flat(errors2))
print(flat(errors3))
