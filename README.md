
## Introduction ##

**asysc** is an analog system compiler based on the lightweight Computer Algebra System **lightcas**.

Using a Computer Algebra System (CAS), you can write your own components by using algebraic descriptions.

Description example for a resistor:

    NAME.CR(@1,@2,R) := { 
        NAME.U=ACROSS(@1,@2); 
        NAME.I=THROUGH(@1,@2); 
        NAME.U=R*NAME.I 
    };

For more examples, see the [component.txt](https://github.com/analog-system-compiler/lightcas/blob/3b8b692d76aa31503276b9a10259393b8f68dcf0/rules/components.txt) and [examples](examples) directories.

The analog system compiler is invoked with the following command (Example with the RLC circuit):
```bash
cd examples/ac/RLC
../../../lightcas/asysc -i RLC.cir -o RLC.py -t AC
```

Once the libraries and netlists are compiled, the Python code is generated for simulation.

## Requirements

### C++ requirement
    - g++ or clang
    - make
  
### Python requirements
    - numpy
    - matplotlib
  
## Getting source code
```bash
git clone https://github.com/analog-system-compiler/asysc.git
cd asysc
git submodule update --init
```

## Code compilation

```bash
make clean
make
```

## Run all tests

```bash
make run
```

## Run a specific test

To execute a particular test, type:

```bash
cd examples
make
cd examples/<directory>
python3 simulation.py
```

## License

This project is licensed under the GNU General Public License - see the [LICENSE](LICENSE) file for details.