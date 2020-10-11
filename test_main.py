from func.main_funcs import is_ip_v4, find_min_subnet
import unittest


class TestMain(unittest.TestCase):

    def test_is_ip_v4(self):
        ip_addr = '10'
        result = is_ip_v4(ip_addr)
        self.assertEqual(result, True)
        ip_addr = 'ip'
        result = is_ip_v4(ip_addr)
        self.assertEqual(result, False)
        ip_addr = '0'
        result = is_ip_v4(ip_addr)
        self.assertEqual(result, True)
        ip_addr = '260'
        result = is_ip_v4(ip_addr)
        self.assertEqual(result, False)

    def test_find_min_subnet(self):
        ip_addr_file = 'tests/addr_list_1.txt'
        result = find_min_subnet(ip_addr_file)
        self.assertEqual(result, 'Result net: 192.168.0.0/24')
        ip_addr_file = 'tests/addr_list_2.txt'
        result = find_min_subnet(ip_addr_file)
        self.assertEqual(result, 'file is empty')
        ip_addr_file = 'addr_list.txt'
        result = find_min_subnet(ip_addr_file)
        self.assertEqual(result, 'Result net: 0.0.0.0/4')
        ip_addr_file = 'tests/addr_list_3.txt'
        result = find_min_subnet(ip_addr_file)
        self.assertEqual(result, '255.255.255.270 is not ip address')
        ip_addr_file = 'tests/addr_list_4.txt'
        result = find_min_subnet(ip_addr_file)
        self.assertEqual(result, 'address 11.255.255.255 is broadcast address of current subnet 8.0.0.0/6. '
                                 'You can not use it as a host address')
        ip_addr_file = 'tests/addr_list_5.txt'
        result = find_min_subnet(ip_addr_file)
        self.assertEqual(result, 'address 8.0.0.0 is address of current subnet 8.0.0.0/6. '
                                 'You can not use it as a host address')


if __name__ == '__main__':
    unittest.main()
