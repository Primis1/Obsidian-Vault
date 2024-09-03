***
Special values:
1. #compiler - is a translation program, that *translates* a PL code into the byte code, and checks its valid, before finishing the translation, if(err) compilation fails, if(!err) compilation success
2. #interpreter - is a translation program, that translates a PL into the output code, without any checks, because of it's line by line interpretation
3. `Translation` - converting a code from PL A to PL B

To know:
![[Pasted image 20240814222133.png]]
1. ==Compilation==
	2. It is ==faster==, better for ==performance== and doesn't need any middleware for running after the execution. Because it is already in byte code and could be read by the CPU itself. 
	3. However compilers are relying on the PC architecture, so one compiled-bytecode not be portable to non-native architecture. 
		1. To make it work in different env, we have to recompile it or even use ==another complier== 

2. ==Interpretation== 
	1. During the interpretation, program in real time translates each line of code, one by one,  into the chosen language, without generation of execution file
	2. ==Read and analysation== is initialed in the moment of interpretation, so it is ==NOT== possible to 

3. From what i have seen, compiled Langs, got its own instruments to be build for different architectures. `Like different golang types could be specified to amount of bytes, different for systems it runs on 

4. How it goes:
	1. In ==compiler== PL, code is ==written== by the programmer, after that ==compiler checks== ALL code on Errors and bugs, only after compiler runs and ==translates== it into bytecode
	2. In interpreter PL, code is written, and immediately transfers into interpreter, literary one line by line 
	![[Pasted image 20240618181952.png]]