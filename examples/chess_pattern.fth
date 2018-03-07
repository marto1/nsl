" Print a chess pattern.  " .
invrow : n3 1 - : rot n3 n3 ; swap loop rot 2 * 2 + print ; def
invertpattern :  dup invrow  ; def
chess : " _ " " X " rot invrow ; def
5 " _ " " X " invrow
