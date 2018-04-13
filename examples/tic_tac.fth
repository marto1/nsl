" Very simple tic tac toe game. Select 0-9 to fill. " .
F : 0 0 0 0 0 0 0 0 0 ; def
V 1 def
invert-V : \" V \" invert-var ; def
get-V : \" V \" get-word ; def
empty-field : : "  | | " . ; 3 loop ; def
field : F : . ; 9 loop ; def
clear-screen : clear os true imported " system " .. 1 call drop ; def
user-input : " (0-9)> " 1 input ; def
init : clear-screen field ; def
rules : get-V 2 'F get-word-q __setitem__ .m invert-V ; def
game-loop : : init user-input rules ; 5 loop ; def
game-loop
