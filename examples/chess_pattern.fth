" Print a chess pattern.  " .
crow : n3 1 - : rot n3 n3 ; swap loop rot 2 * print ; def
V -1 def
invert-V : \" V \" invert-var ; def
get-V : \" V \" get-word ; def
swap-if : : swap ; if ; def
loop-row : : " □ " " ■ " get-V swap-if crow invert-V ; ; def
chess : 0 swap loop-row .insert swap loop ; def
8 8 chess
