import json

def write(data, filename):
    data = json.dumps(data)
    data = json.loads(str(data))
    with open(filename, 'w', encoding = 'utf-8') as file:
        json.dump(data, file, indent= 3)

n_data = {
    "users": [1, 2, 3]
}

write(n_data, 'data.json')