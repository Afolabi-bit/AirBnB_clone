# AirBnB Clone

### This is the first part of a series of projects that adds up as a clone of the [AirBnB](https://www.airbnb.com/) website.

**This project achieves the following:**

- Put in place a parent class (called _BaseModel_) t take care of the initializaton, serialization and deserialization of future instances

- Create a simple flow of serialization/deserialization: Instance <_> Dictionary <_> JSON string <_> file

- Create all classes used for AirBnB (_User_, _State_, _City_, _Place_ ...)) that inherit from _BaseModel_

- Create the first abstracted storage engine of the project: File storage

- Create all unittests to validate all our classes and storage engine



## Execution

This shell should work like this in interactive mode:
```
$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit

(hbnb) 
(hbnb) 
(hbnb) quit
$
```

But also in non-interactive mode:
```
$ echo "help" | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
$ cat test_help
help
$
$ cat test_help | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
```

All tests should also pass in non-interactive mode:
> $ echo "python3 -m unittest discover tests" | bash

Here is a pictorial representation of the aspect of the overall project this tasks focuses on:

![](https://s3.amazonaws.com/alx-intranet.hbtn.io/uploads/medias/2018/6/815046647d23428a14ca.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUSBVO6H7D%2F20230206%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20230206T184755Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=24a0489c585552ed6227c57d10a7ec61ff0a19398cd51869adf4db928856e8ae)
