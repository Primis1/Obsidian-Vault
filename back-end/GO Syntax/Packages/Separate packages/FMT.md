Special values:
1. fmt - formatting #package
2. ln - if func has a such suffix, it will end a \n to each line automatically
3. f - allows to use *==verbs==*

To know:
1. there are a bunch of verb that we can use:
	   - `%v`: The value in a default format.
	- `%+v`: When printing structs, the plus flag adds field names.
	- `%#v`: A Go-syntax representation of the value.
	- `%T`: A Go-syntax representation of the type of the value.
	- `%%`: A literal percent sign; consumes no value.
	
	For **integers**:
	
	- `%b`: Base 2.
	- `%c`: The character represented by the corresponding Unicode code point.
	- `%d`: Base 10.
	- `%o`: Base 8.
	- `%x`: Base 16, with lower-case letters for a-f.
	- `%X`: Base 16, with upper-case letters for A-F.
	
	For **floating-point numbers**:
	
	- `%f`: Decimal point but no exponent.
	- `%e`: Scientific notation, with a lower-case ‘e’.
	- `%E`: Scientific notation, with an upper-case ‘E’.
	- `%g`: Uses `%e` for large exponents, `%f` otherwise.
	
	For **strings**:
	
	- `%s`: The uninterpreted bytes of the string or slice.
	- `%q`: A double-quoted string safely escaped with Go syntax.
	
	For **pointers**:
	
	- `%p`: Base 16 notation, with leading 0x.