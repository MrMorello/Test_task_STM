## Minimum subnet finder
This application developed for finding minimum subnet for list of ip addresses 

### Getting started
#### Installing
You need python 3.7 version or higher

Pull this repo and install requirement from reqiuirements.txt

#### Using
For getting a minimum subnet for ip-addresses list use CLI

parameters: -f \<filename>, -v \<ip version> 

__Examples:__

use -h for get help
```bash
python main.py -h #help
```

for get minimal subnet
```bash
python main.py -f <filename> -v IPv4
->0.0.0.0/4
```
also using without ip version is allowed
```bash
python main.py -f <filename> #ipv4 used as default
->0.0.0.0/4
```
The time of execution increases according to size of ip-address list and supposedly equals to O(2n).

The application doesn't consider the type of address (subnet or broadcast), but reports about it.
For example, if 8.0.0.0 is in list of ip-addresses and it is address of subnet:
```
->address 8.0.0.0 is address of current subnet 8.0.0.0/6. You can not use it as a host address
```

### Running the tests
test_main.py file contains minimal tests set for checking application
Attention! For testing your own ip address sets, change paths to file at test_main.py 

**Test coverage:**

| Name  | Stmts | Miss | Cover | Missing|
| ------------- | ------------- | ------------- | ------------- | -------------|
| func/\__init__.py  | 0  | 0 | 100% |
| func/main_funcs.py  | 37  | 0 | 100% |
| test_main.py | 37 | 1 | 97% | 47 |
| TOTAL | 74 | 1 | 99% | 

### Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

### Version
Current version developed as a minimum allowed test task and supports working only with ipv4 version.

### Authors
__Dmitry Chepyzhov__

### License
This project is licensed under the DTL FreeType Project LICENSE - see the LICENSE.md file for details
