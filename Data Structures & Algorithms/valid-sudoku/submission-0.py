class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def validmatric(mat):
            count = {}
            for i in range(len(mat)):
                for j in range(len(mat[i])):
                    if mat[i][j] == ".":
                        continue
                    if mat[i][j] in count:
                        count[mat[i][j]]+=1
                    else:
                        count[mat[i][j]]=1
            for i in count.keys():
                if count[i]>1:
                    return False
            return True
        for i in board:
            if validmatric(i) == False:
                return False

            
        res=[]
        for i in range(9):
            arr=[]
            for j in range(9):
                arr.append(board[j][i])
                res.append(arr)
        for i in res:
            if validmatric(i) == False:
                return False

        res_new=[]
        for i in range(0,len(board),3):
            for j in range(0,len(board[i]),3):
                arr=[]
                for k in range(i,i+3):
                    for l in range(j,j+3):
                        arr.append(board[k][l])
                res_new.append(arr)

        for i in res_new:
            if validmatric(i) == False:
                return False
        
            
            
        return True
        