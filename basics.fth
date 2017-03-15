over : -2 stack " __getitem__ " 2 getattr 1 call ; def
swap : over -3 stack " __delitem__ " 2 getattr 1 call ; def
negate : op " __neg__ " 2 getattr 1 call ; def
.item : swap __getitem__ 2 getattr 1 call ; def
.slice : 2 slice .item ; def
get-word : global_words swap .item ; def
.doc : swap 1 none .slice get-word swap func_doc swap 3 setattr ; def
'.item " access a with index b (a b -- c) " .doc
'.slice " get slice from a from b to c (a b c -- d) " .doc
'.doc " set documentation for word ('word doc -- ) " .doc
included : 1 read_file_and_execute ; def
.s : stack 1 print ; def
'.s " print stack ( -- ) " .doc
words : global_words " keys " 2 getattr 0 call 1 print ; def
'words " print all defined words ( -- ) " .doc
depth : stack 1 len ; def
'depth " put stack size on top ( -- +n ) " .doc
+ : op " __add__ " 2 getattr 2 call ; def
'+ " add two numeric values ( n1 n2 -- n1+n2 ) " .doc
- : negate + ; def
and : op " __and__ " 2 getattr 2 call 1 bool 1 int negate ; def
'and " logical and ( a b -- -1/0 ) " .doc
or : op " __or__ " 2 getattr 2 call 1 bool 1 int negate ; def
'or " logical or ( a b -- -1/0 ) " .doc
* : op " mul " 2 getattr 2 call ; def
'over " copy 2nd element to top ( a b -- a b a ) " .doc
drop : -1 stack " __delitem__ " 2 getattr 1 call ; def
nip : -2 stack " __delitem__ " 2 getattr 1 call ; def
dup : -1 stack " __getitem__ " 2 getattr 1 call ; def
tuck : dup -2 swap stack " insert " 2 getattr 2 call ; def
2dup : over over ; def
rot : -3 stack " pop " 2 getattr 1 call ; def
rrot : -2 swap stack " insert " 2 getattr 2 call ; def
= : op " eq " 2 getattr 2 call 1 int negate ; def
'= " equality test ( a b -- -1/0 ) " .doc
> : op " gt " 2 getattr 2 call 1 int negate ; def
'> " bigger than test ( a b -- -1/0 ) " .doc
< : op " lt " 2 getattr 2 call 1 int negate ; def
'< " smaller than test ( a b -- -1/0 ) " .doc
>= : 2dup > rrot = or ; def
<= : 2dup < rrot = or ; def
xor : op " __xor__ " 2 getattr 2 call 1 int negate ; def
invert : op " __invert__ " 2 getattr 1 call ; def
'invert " invert numerical value ( 0 -- -1 ; def -1 -- 0 ) " .doc
true : -1 ; def
false : 0 ; def
0> : 0 > ; def
empty : '. depth 1 - loop ; def
clearstack : none none 2 slice stack " __delitem__ " 2 getattr 1 call ; def
.help : 1 none .slice get-word func_doc 2 getattr 1 print ; def
'.help " get documention for word ('word -- doc) " .doc
bye : 0 exit ; def
. : 1 print ; def
'. " pop top and print it ( a -- ) " .doc
'negate " negate numeric value ( n -- -n ) " .doc
loop : swap * stack global_words 3 execute ; def
