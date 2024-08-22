
## Introduction ##

**asysc** is an analog system compiler based on the lightweight Computer Algebra System **lightcas**.
By using a Computer Algebra System (CAS), one can write its own components by using algebraic definitions. 
For examples, refer to directories `lightcas/rules/components.txt` and `examples`.
Once the libraries and netlists are compiled, Python code is generated for simulation.
To execute a particular test, go into examples/ and type:

```bash
python3 simulation.py
```

## Requirements

### C++ requirement
    - g++ or clang
    - make
  
### Python requirements
    - numpy
    - matplotlib
  
```bash
pip install numpy
pip install matplotlib
```

## Compilation

```bash
make clean
make
```

## Run

```bash
make run
```