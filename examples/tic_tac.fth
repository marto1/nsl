" Very simple tic tac toe game. Select 0-9 to fill. " .
empty-field : : "  | | " . ; 3 loop ; def
clear-screen : " clear " " os " true imported " system " .. 1 call ; def
" os " : system ; imported
clear-screen
empty-field

