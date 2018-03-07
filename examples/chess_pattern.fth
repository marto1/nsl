" Print a chess pattern.  " .
invrow : n3 1 - : rot n3 n3 ; swap loop rot 2 * print ; def
V -1 def
invert-V : \" V \" \" V \" get-word invert def ; def
chess : : " □ " " ■ " \" V \" get-word : swap ; if invrow invert-V ; swap 0 swap rot .insert swap loop ; def
8 8 chess
