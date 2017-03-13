: .item swap __getitem__ 2 getattr 1 call ;
: .slice 2 slice .item ;
: get-word global_words swap .item ;
: .doc swap 1 none .slice get-word swap func_doc swap 3 setattr ;
'.item " access a with index b (a b -- c) " .doc
'.slice " get slice from a from b to c (a b c -- d) " .doc
'.doc " set documentation for word ('word doc -- ) " .doc
: included 1 read_file_and_execute ;
: .s stack 1 print ;
'.s " print stack ( -- ) " .doc
: words global_words " keys " 2 getattr 0 call 1 print ;
'words " print all defined words ( -- ) " .doc
: depth stack 1 len ;
'depth " put stack size on top ( -- +n ) " .doc
: + op " __add__ " 2 getattr 2 call ;
'+ " add two numeric values ( n1 n2 -- n1+n2 ) " .doc
: - negate + ;
: and op " __and__ " 2 getattr 2 call 1 bool 1 int negate ;
'and " logical and ( a b -- -1/0 ) " .doc
: or op " __or__ " 2 getattr 2 call 1 bool 1 int negate ;
'or " logical or ( a b -- -1/0 ) " .doc
: * op " mul " 2 getattr 2 call ;
: drop -1 stack " __delitem__ " 2 getattr 1 call ;
: nip -2 stack " __delitem__ " 2 getattr 1 call ;
: dup -1 stack " __getitem__ " 2 getattr 1 call ;
: 2dup over over ;
: rot -3 stack " pop " 2 getattr 1 call ;
: rrot -2 swap stack " insert " 2 getattr 2 call ;
: = op " eq " 2 getattr 2 call 1 int negate ;
'= " equality test ( a b -- -1/0 ) " .doc
: > op " gt " 2 getattr 2 call 1 int negate ;
'> " bigger than test ( a b -- -1/0 ) " .doc
: < op " lt " 2 getattr 2 call 1 int negate ;
'< " smaller than test ( a b -- -1/0 ) " .doc
: >= 2dup > rrot = or ;
: <= 2dup < rrot = or ;
: xor op " __xor__ " 2 getattr 2 call 1 int negate ;
: invert op " __invert__ " 2 getattr 2 call ;
'invert " invert numerical value ( 0 -- -1 ; -1 -- 0 ) " .doc
: true -1 ;
: false 0 ;
: 0> 0 > ;
: empty '. depth 1 - loop ;
: clearstack none none 2 slice stack " __delitem__ " 2 getattr 1 call ;
: .help 1 none .slice get-word func_doc 2 getattr 1 print ;
'.help " get documention for word ('word -- doc) " .doc
: bye 0 exit ;
