# Tiny Compiler
Tiny is a BASIC-like programming language. This is a toy compiler implementation outlined by [Austin Z. Henley](https://austinhenley.com/blog/teenytinycompiler1.html). 
Compiler is written in Python 3 and compilers Tiny into C. Compilation is a little fiddley. Requires the user to compile the Tiny program into C, then compile the C program. Looks something like this:
```
python teenytiny.py average.teeny
clang out.c -o out
./out
```
`teenytiny.py` is the Tiny compiler. `average.teeny` is whatever Tiny program you want to compile. `out.c` and `out` is the intermediate compiled C program and the compiled C program, respectively.

### Next Steps
This is largely taken directly from Austin's tutorial as a way to better understand compiler frontends better. The next step would likely be to convert this into C++ to utilize LLVM bindings when building the AST unless I want to just use llvmpy.
Either way, the plan is to use LLVM in some capacity to compile this into machine code for ARM or x86. I can then use LLVM-opt tools to run some optimization passes on it to make this toy language go fast.

