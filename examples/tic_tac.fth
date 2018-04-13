" Very simple tic tac toe game. Select 0-9 to fill. " .
F : 0 0 0 0 0 0 0 0 0 ; def
V 1 def
invert-V : \" V \" invert-var ; def
get-V : \" V \" get-word ; def
empty-field : : "  | | " . ; 3 loop ; def
translate : dup 0 = : _ . ; if dup 1 = : X . ; if -2 = : O . ; if ; def
field : F : translate ; 9 loop ; def
clear-screen : clear os true imported " system " .. 1 call drop ; def
user-input : " (0-9)> " 1 input ; def
init : clear-screen field ; def
get-F : 'F get-word-q ; def
sitem : __setitem__ ; def
set-field : get-V 2 get-F sitem .m invert-V ; def
rules : dup get-F swap .item 0 = : set-field ; if ; def
game-loop : : init user-input rules ; 5 loop ; def
game-loop
