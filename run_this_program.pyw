import subprocess as subp

subp.run("Python -m janken", shell=True) # shell=Trueでコマンドを文字列として実行。脆弱性となりうるので注意

