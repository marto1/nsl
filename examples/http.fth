" Example HTTP GET request " .
R http://raw.githubusercontent.com/marto1/picoforth/master/README.md def
get-R : \" R \" get-word ; def
http urllib2 true imported " urlopen " .. def
get-http : \" http \" get-word 1 call ; def
" Result code from example.com: " . 
0 http://example.com get-http getcode .m .
" README file content: " .
0 get-R get-http read .m .
