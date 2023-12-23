# Pine
A simple logging tool.
```
+ is good
- is bad
! is ugly
< is safe
> is attention
```

- files are divided into the good, the bad, and the ugly, for printing those 3 basic types of outputs
- there is an additional safe file, for printing everything else
- each run creates or appends to a log file everything that is passed to pine

## Installation
### 1. Clone repo
Navigate to your desired directory, and in the terminal enter: 
```
git clone https://github.com/avneeshchandra/pine.git
```
### 2. Add the repo to your system's path
This is so that your code knows where to look for it.
```
import sys
sys.path.append(path/to/repo/on/your/system)
```
### 2. Add the repo to your system's path
Run the following to test!
```
from pine import Pine

pine = Pine()
print("Starting")
pine.needle("+This is good!")
pine.needle("-This is bad!")
pine.needle("!This is uhh!")
pine.needle(">This is fine!")
pine.needle("<This is fine!")
```