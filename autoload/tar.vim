let s:plugin_path = escape(expand('<sfile>:p:h'), '\')
exe 'pyfile ' . escape(s:plugin_path, ' ') . '/tar.py'

if exists('g:loaded_tar') || &cp
  finish
endif

function tar#tarlol()
    python lol()
endfunction

function tar#tarlist(var)
    exe 'python tarlist("'a:var'")'
endfunction

function tar#Browse(var)
    exe 'python tarlist("'a:var'")'
endfunction

function tar#Enter()
    exe 'python tarenter()'
endfunction

let g:loaded_tar = 1
