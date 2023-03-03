def guillermo_diamante ():
    ast = []
    cnt=0
    i = 10
    while cnt < i:
        ast.append("/")
        ast.append(" ")
        print ((ast[1]) * (i-cnt)+ (ast[0]) + (ast[1]) * len(ast) + "\\")
        cnt = cnt + 1
    if cnt == i:
        while cnt > 1:
            ast.pop(0)
            j = i+cnt
            k = i-cnt
            print ((" ") * (i-cnt+1)+("\\") + (" ") * (len(range(j,k,-1))) + "/")