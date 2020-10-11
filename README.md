## Minimum subnet finder
This application developed for finding minimum subnet for list of ip addresses 

### Getting started
#### Installing
You need python 3.7 version or higher

Pull this repo and install requirement from reqiuirements.txt

#### Using
For getting a minimum subnet for ip-addresses list use CLI

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

### Running the tests
test_main.py file contains minimal tests set for checking application
Attention! For testing your own ip address sets, change paths to file at test_main.py 

### Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

### Version
Current version developed as a minimum allowed test task and supports working with only ipv4 version.

### Authors
__Dmitry Chepyzhov__

### License
This project is licensed under the DTL FreeType Project LICENSE - see the LICENSE.md file for details
