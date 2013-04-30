" PostPrompt Markdown Language
" Author : Quinten Palmer

highlight link fieldtype   Type
highlight link declaration Function
highlight link name        String
highlight link pptodo      String

if exists("b:current_syntax")
	finish
endif

syn keyword fieldtype field method
syn keyword pptodo TODO
syn match declaration '^\w\+'
syn match name "\%(:\s*\)\@<=\h\w*"
