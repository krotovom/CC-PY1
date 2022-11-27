import json


def csv_to_list_dict(output_file, delimiter=',', new_line='\n'):
    data_dict = []
    with open(output_file, 'r') as csv_file:
        headers_list = csv_file.readline().rstrip(new_line).split(delimiter)
        for line in csv_file:
            data = line.rstrip(new_line).split(delimiter)
            data_dict.append(dict(zip(headers_list, data)))
    return data_dict


print(json.dumps(csv_to_list_dict('output.csv', delimiter=',', new_line='\n'), indent=4))
