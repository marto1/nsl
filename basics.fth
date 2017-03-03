: .item swap __getitem__ 2 getattr 1 call ;
: .slice 2 slice .item ;
: get-word global_words swap .item ;
: .doc swap 1 None .slice get-word swap func_doc swap 3 setattr ;
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
: - negate + ;
: ++ over + ;
: * op " mul " 2 getattr 2 call ;
: 2dup over over ;
: = op " eq " 2 getattr 2 call 1 int negate ;
'= " equality test ( a b -- -1/0 ) " .doc
: > op " gt " 2 getattr 2 call 1 int negate ;
'> " bigger than test ( a b -- -1/0 ) " .doc
: < op " lt " 2 getattr 2 call 1 int negate ;
'< " smaller than test ( a b -- -1/0 ) " .doc
: >= 2dup > rrot = or ;
: <= 2dup < rrot = or ;
: xor op " __xor__ " 2 getattr 2 call 1 int negate ;
: true -1 ;
: false 0 ;
: 0> 0 > ;
: empty '. depth 1 - loop ;
: clearstack None None 2 slice stack " __delitem__ " 2 getattr 1 call ;
: .help 1 None .slice get-word func_doc 2 getattr 1 print ;
'.help " get documention for word ('word -- doc) " .doc
: bye 0 exit ;
: drop -1 stack " __delitem__ " 2 getattr 1 call ;
: nip -2 stack " __delitem__ " 2 getattr 1 call ;
