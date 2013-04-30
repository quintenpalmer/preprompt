" PostPrompt Markdown Language
" Author : Quinten Palmer

highlight link ppAttributeType Type
highlight link ppDeclaration   Function
highlight link ppFieldName     String
highlight link ppMethodName    String
highlight link ppTodo          String

if exists("b:current_syntax")
	finish
endif

syn keyword ppAttributeType field method
syn keyword ppTodo TODO
syn match ppDeclaration '^\w\+'
syn match ppFieldName "\(field :\s*\)\@<=\h\w*"
syn match ppMethodName "\(method :\s*\)\@<=\h\w*"
syn match ppTodo "\(TODO :\s*\)\@<=\h.*"
