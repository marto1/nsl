'.item " access a with index b (a b -- c) " .doc
'.slice " get slice from a from b to c (a b c -- d) " .doc
'.doc " set documentation for word ('word doc -- ) " .doc
'.s " print stack ( -- ) " .doc
'words " print all defined words ( -- ) " .doc
'depth " put stack size on top ( -- +n ) " .doc
'+ " add two numeric values ( n1 n2 -- n1+n2 ) " .doc
'and " logical and ( a b -- -1/0 ) " .doc
'or " logical or ( a b -- -1/0 ) " .doc
'over " copy 2nd element to top ( a b -- a b a ) " .doc
'= " equality test ( a b -- -1/0 ) " .doc
'> " bigger than test ( a b -- -1/0 ) " .doc
'< " smaller than test ( a b -- -1/0 ) " .doc
'invert " invert numerical value ( 0 -- -1 ; def -1 -- 0 ) " .doc
'negate " negate numeric value ( n -- -n ) " .doc
'.help " get documention for word ('word -- doc) " .doc
'. " pop top and print it ( a -- ) " .doc
