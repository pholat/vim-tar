if exists('g:loaded_tar') || &cp
  finish
endif

" done acording to gundo
command! -nargs=0 TarLol call tar#tarlol()
command! -nargs=1 TarList call tar#tarlist(<q-args>)
nmap <cr> tar#Enter
