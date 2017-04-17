if exists('g:loaded_tar') || &cp
  finish
endif

" done acording to gundo
command! -nargs=0 TarLol call tar#lol()
command! -nargs=1 TarBrowse call tar#Browse(<q-args>)
command! -nargs=0 TarEnter call tar#Enter()
"nmap <cr> tar#Enter()
