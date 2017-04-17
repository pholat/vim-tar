let s:plugin_path = escape(expand('<sfile>:p:h'), '\')
exe 'pyfile ' . escape(s:plugin_path, ' ') . '/tar.py'

if exists('g:loaded_tar') || &cp
  finish
endif

function tar#lol()
    exe 'python lol()'
endfunction

function tar#Browse(var)
    exe 'python tarbrowse("'a:var'")'
endfunction

function tar#Enter()
    exe 'python tarenter()'
endfunction

let g:loaded_tar = 1
