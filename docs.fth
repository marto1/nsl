'.item " access a with index b (a b -- c) " .doc
'.slice " get slice from a from b to c (a b c -- d) " .doc
'.doc " set documentation for word ('word doc -- ) " .doc
'.s " print stack ( -- ) " .doc
'words " print all defined words ( -- ) " .doc
'depth " put stack size on top ( -- +n ) " .doc
'.m " call a method from object ( n1 a b  -- c ) " .doc
'.split " create a list of strings ( adbdc d -- [a, b, c] ) " .doc
'.split, " .split with , shorthand  ( a,b,c -- [a, b, c] ) " .doc
'.split. " .split with . shorthand  ( a,b,c -- [a, b, c] ) " .doc
'.split; " .split with ; shorthand  ( a,b,c -- [a, b, c] ) " .doc
'+ " add two numeric values ( n1 n2 -- n1+n2 ) " .doc
'- " substract two numeric values ( n1 n2 -- n1-n2 ) " .doc
'and " logical and ( a b -- -1/0 ) " .doc
'or " logical or ( a b -- -1/0 ) " .doc
'xor " logical xor ( a b -- -1/0 ) " .doc
'* " multiplication of 2 objects ( a b -- a*b ) " .doc
'drop " delete top of stack element ( a -- ) " .doc
'dup " duplicate top ( a -- a a ) " .doc
'2dup " duplicate top 2 elements ( a b -- a b a b ) " .doc
'rot " rotate 3rd element ( a b c -- b c a ) " .doc
'rrot " reverse rotate ( a b c -- c a b ) " .doc
'swap " swap 2 topmost elements ( a b -- b a ) " .doc
'loop " take word and number, execute word n times  ( a n -- ) " .doc
'over " copy 2nd element to top ( a b -- a b a ) " .doc
'= " equality test ( a b -- -1/0 ) " .doc
'> " bigger than test ( a b -- -1/0 ) " .doc
'< " smaller than test ( a b -- -1/0 ) " .doc
'<= " smaller or equal than test ( a b -- -1/0 ) " .doc
'>= " bigger or equal than test ( a b -- -1/0 ) " .doc
'invert " invert numerical value ( 0 -- -1 ; def -1 -- 0 ) " .doc
'negate " negate numeric value ( n -- -n ) " .doc
'.help " get documention for word ('word -- doc) " .doc
'. " pop top and print it ( a -- ) " .doc
'true " True value added to stack ( -- -1 ) " .doc
'false " False value added to stack ( -- 0 ) " .doc
'0> " bigger than 0 ( a -- -1/0 ) " .doc
'0< " smaller than 0 ( a -- -1/0 ) " .doc
'empty " empty out and print stack ( -- ) " .doc
'clearstack " empty out stack ( -- ) " .doc
'bye " exit interpreter ( -- ) " .doc
'if " conditional function ( -1/0 block -- ) " .doc
'.slice " get slice of sequence  ( n1 n2 -- s ) " .doc
'nip " delete element before top of stack ( a b -- b ) " .doc
'tuck " copy top of stack to 3rd place  ( a b -- b a b ) " .doc
'get-word " get a definition from global words ( a -- b ) " .doc
