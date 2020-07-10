set term=color_xterm
"set autoindent
set encoding=utf-8
set shiftwidth=4
set softtabstop=4
set laststatus=2
syntax on
set guifont=Consolas:h12:cANSI"英文字体
set tabstop=4
set expandtab"tab转空格
set autoread"当文件在外部被修改时自动重读
set history=400
set nocompatible"使用vim键盘模式
set confirm"处理未保存或者只读文件提示
set smartindent"智能对齐
set shiftwidth=4
set backup "自动备份
set backupext=.bak "自动备份文件后缀
set patchmode=.orig "自动保存原始文件
autocmd BufNewFile *.py,*.sh exec ":call SetTitle()"
""定义函数SetTitle，自动插入文件头
func SetTitle()
        "如果文件类型为.sh文件
        if &filetype == 'sh'
                call setline(1,"\#################################################")
                call append(line("."), "\#!/bin/bash")
                call append(line(".")+1, "\# File Name: ".expand("%"))
                call append(line(".")+2, "\# Author: lixuebin")
                call append(line(".")+3, "\# mail: li.xuebin@hotmail.com")
                call append(line(".")+4, "\# Created Time: ".strftime("%c"))
                call append(line(".")+5, "\#################################################")
                call append(line(".")+6, "")
        elseif &filetype == 'python'
                call setline(1, "\###############################################")
                call append(line("."), "\#!/usr/bin/env python")
                call append(line(".")+1, "\# -*- coding:utf-8 -*-")
                call append(line(".")+2, '"""')
                call append(line(".")+3, " > File Name: ".expand("%"))
                call append(line(".")+4, " > Author: lixuebin")
                call append(line(".")+5, " > Mail: li.xuebin@hotmail.com ")
                call append(line(".")+6, " > Created Time: ".strftime("%c"))
                call append(line(".")+7, '"""')
                call append(line(".")+8, "\################################################")
                
    else
                call setline(1, "\*************************************************************************")
                call append(line("."), "        > File Name: ".expand("%"))
                call append(line(".")+1, "      > Author: lixuebin")
                call append(line(".")+2, "      > Mail: li.xuebin@hotmail.com ")
                call append(line(".")+3, "      > Created Time: ".strftime("%c"))
                call append(line(".")+4, " **********************************************************************")
                call append(line(".")+5, "")
        endif
        "新建文件后，自动定位到文件末尾
        autocmd BufNewFile * normal G
endfunc
