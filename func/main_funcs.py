def is_ip_v4(s):
    try:
        return str(int(s)) == s and 0 <= int(s) <= 255
    except Exception as e:
        return False


def find_min_subnet(filename):
    with open(filename, encoding='utf-8-sig') as f:
        content = f.readlines()  # type: list
    content = [x.strip() for x in content]
    content = list(filter(None, content))
    if len(content) == 0:
        return 'file is empty'

    comparison_ip_list = []

    # внутри цикла проверяется валидность ip адресов, перевод в бинарный и десятичный вид для дальнейшего поска
    # максимального и минимального значения
    for ip in content:
        if ip.count(".") == 3 and all(is_ip_v4(i) for i in ip.split(".")):
            binary_string = (''.join([format(int(elem), '08b') for elem in ip.split('.')]))  # type: str
            binary_int = int(binary_string, 2)  # type: int
            comparison_ip_list.append(binary_int)
            continue
        else:
            return f'{ip} is not ip address'

    # поиск адреса и маски минимальной подсети по масимальному и минимальному ip адресу
    max_ip = max(comparison_ip_list)  # type: int
    min_ip, min_index = min(comparison_ip_list), comparison_ip_list.index(min(comparison_ip_list))  # type: int

    mask_int = max_ip ^ min_ip  # type: int
    invert_mask = (len('{0:b}'.format(mask_int)))  # type: int
    net_mask = 32 - invert_mask  # type: int
    bin_min_str = ''.join([format(int(k), '08b') for k in content[min_index].split('.')])  # type: str
    net_str = bin_min_str[:net_mask] + "0" * invert_mask  # type: str
    net_broadcast_str = bin_min_str[:net_mask] + "1" * invert_mask  # type: str
    net_addr_list = [str(int(net_str[:8], 2)), str(int(net_str[8:16], 2)), str(int(net_str[16:24], 2)),
                     str(int(net_str[24:], 2))]  # type: list
    net_addr_str = f"{'.'.join(net_addr_list)}/{net_mask}"  # type: str
    broadcast_addr_list = [str(int(net_broadcast_str[:8], 2)), str(int(net_broadcast_str[8:16], 2)),
                           str(int(net_broadcast_str[16:24], 2)), str(int(net_broadcast_str[24:], 2))]  # type: list
    broadcast_addr_str = '.'.join(broadcast_addr_list)  # type: str
    if net_addr_str.split("/")[0] in content:
        return f'address {net_addr_str.split("/")[0]} is address of current subnet {net_addr_str}. ' \
               f'You can not use it as a host address'
    if broadcast_addr_str in content:
        return f'address {broadcast_addr_str} is broadcast address of current subnet {net_addr_str}. ' \
               f'You can not use it as a host address'
    return net_addr_str
