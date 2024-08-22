
## Introduction ##

**asysc** is an analog system compiler based on the lightweight Computer Algebra System **lightcas**.
Using a Computer Algebra System (CAS), you can write your own components by using algebraic descriptions. 
For examples, see the `lightcas/rules/components.txt` and `examples` directories.
Once the libraries and netlists are compiled, the Python code is generated for simulation.
To execute a particular test, go into its directory and type:

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
  
## Compilation

```bash
make clean
make
```

## Run

```bash
make run
```