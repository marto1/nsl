" Very simple tic tac toe game. Select 0-8 to fill. " .
F : 0 0 0 0 0 0 0 0 0 ; def
V 1 def
invert-V : \" V \" invert-var ; def
get-V : \" V \" get-word ; def
empty-field : : "  | | " . ; 3 loop ; def
tr : dup 0 = : _ swap ; if dup 1 = : X swap ; if -2 = : O ; if ; def
tr-3 : tr rrot tr swap tr ; def
field : F : tr-3 3 print ; 3 loop ; def
clear-screen : clear os true imported " system " .. 1 call drop ; def
user-input : " (0-8)> " 1 input ; def
init : clear-screen field ; def
get-F : 'F get-word-q ; def
sitem : __setitem__ ; def
set-field : get-V 2 get-F sitem .m invert-V ; def
rules : dup get-F swap .item 0 = : set-field ; if ; def
game-loop : : init user-input rules ; 100 loop ; def
game-loop
