#!/usr/bin/env python3
# pip3 install sh
import sh

sh.pwd()
#* current directory

sh.mkdir('new-folder')

sh.touch('new-file.txt')

sh.whoami()
#* username

sh.echo('Hi!')
#* Hi!