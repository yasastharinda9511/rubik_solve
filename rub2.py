import copy
import time
start_time = time.time()
rubix=[[["B","Y","G"],["O","W","B"],["O","O","W"]],
       [["W","B","R"],["G","G","B"],["Y","R","Y"]],
       [["B","W","G"],["R","Y","G"],["G","G","W"]],
       [["B","Y","R"],["W","B","W"],["O","Y","R"]],
       [["Y","W","W"],["R","R","G"],["O","O","G"]],
       [["B","O","R"],["B","O","R"],["Y","Y","O"]]]
wFace=0
gFace=1
yFace=2
bFace=3
rFace=4
oFace=5
def graphmove(graph,move):
    if move=="u":
        graph[rFace][0],graph[gFace][0],graph[oFace][0],graph[bFace][0]=graph[bFace][0],graph[rFace][0],graph[gFace][0],graph[oFace][0]
        transposeclock(graph[wFace])
    elif move=="d":
        graph[rFace][2],graph[bFace][2],graph[oFace][2],graph[gFace][2]=graph[gFace][2],graph[rFace][2],graph[bFace][2],graph[oFace][2]
        transposeclock(graph[yFace])
    elif move=="u2":
        graph[rFace][0],graph[oFace][0]=graph[oFace][0],graph[rFace][0]
        graph[bFace][0],graph[gFace][0]=graph[gFace][0],graph[bFace][0]
        transposeclock(graph[wFace])
        transposeclock(graph[wFace])
    elif move=="d2":
        graph[rFace][2],graph[oFace][2]=graph[oFace][2],graph[rFace][2]
        graph[bFace][2],graph[gFace][2]=graph[gFace][2],graph[bFace][2]
        transposeclock(graph[yFace])
        transposeclock(graph[yFace])
    elif move=="r":
        faces=[wFace,gFace,yFace,bFace]
        a,b,c=graph[bFace][0][2],graph[bFace][1][2],graph[bFace][2][2]
        for i in faces:
            if i==wFace:
                d,e,f=graph[i][0][2],graph[i][1][2],graph[i][2][2]
                graph[i][0][2],graph[i][1][2],graph[i][2][2]=a,b,c   
            elif  i==gFace:
                d,e,f=graph[i][0][0],graph[i][1][0],graph[i][2][0]
                graph[i][0][0],graph[i][1][0],graph[i][2][0]=c,b,a
            elif i==yFace:
                d,e,f=graph[i][0][0],graph[i][1][0],graph[i][2][0]
                graph[i][0][0],graph[i][1][0],graph[i][2][0]=a,b,c
            else:
                graph[i][0][2],graph[i][1][2],graph[i][2][2]=c,b,a
            a,b,c=d,e,f
        transposeclock(graph[oFace])
    elif move=="l":
        faces=[bFace,yFace,gFace,wFace]
        a,b,c=graph[wFace][0][0],graph[wFace][1][0],graph[wFace][2][0]
        for i in faces:
            if i==bFace:
                d,e,f=graph[i][0][0],graph[i][1][0],graph[i][2][0]
                graph[i][0][0],graph[i][1][0],graph[i][2][0]=a,b,c   
            elif  i==gFace:
                d,e,f=graph[i][0][2],graph[i][1][2],graph[i][2][2]
                graph[i][0][2],graph[i][1][2],graph[i][2][2]=a,b,c
            elif i==yFace:
                d,e,f=graph[i][0][2],graph[i][1][2],graph[i][2][2]
                graph[i][0][2],graph[i][1][2],graph[i][2][2]=c,b,a
            else:
                graph[i][0][0],graph[i][1][0],graph[i][2][0]=c,b,a
            a,b,c=d,e,f
        transposeclock(graph[rFace])
    elif move=="r2":
        a,b,c=graph[wFace][0][2],graph[wFace][1][2],graph[wFace][2][2]
        d,e,f=graph[yFace][0][0],graph[yFace][1][0],graph[yFace][2][0]
        graph[wFace][0][2],graph[wFace][1][2],graph[wFace][2][2]=f,e,d
        graph[yFace][0][0],graph[yFace][1][0],graph[yFace][2][0]=c,b,a

        a,b,c=graph[gFace][0][0],graph[gFace][1][0],graph[gFace][2][0]
        d,e,f=graph[bFace][0][2],graph[bFace][1][2],graph[bFace][2][2]
        graph[gFace][0][0],graph[gFace][1][0],graph[gFace][2][0]=f,e,d
        graph[bFace][0][2],graph[bFace][1][2],graph[bFace][2][2]=c,b,a
        transposeclock(graph[oFace])
        transposeclock(graph[oFace])
    elif move=="l2":
        a,b,c=graph[yFace][0][2],graph[yFace][1][2],graph[yFace][2][2]
        d,e,f=graph[wFace][0][0],graph[wFace][1][0],graph[wFace][2][0]
        graph[yFace][0][2],graph[yFace][1][2],graph[yFace][2][2]=f,e,d
        graph[wFace][0][0],graph[wFace][1][0],graph[wFace][2][0]=c,b,a

        a,b,c=graph[bFace][0][0],graph[bFace][1][0],graph[bFace][2][0]
        d,e,f=graph[gFace][0][2],graph[gFace][1][2],graph[gFace][2][2]
        graph[bFace][0][0],graph[bFace][1][0],graph[bFace][2][0]=f,e,d
        graph[gFace][0][2],graph[gFace][1][2],graph[gFace][2][2]=c,b,a
        transposeclock(graph[rFace])
        transposeclock(graph[rFace])
    elif move =="f":
        faces=[wFace,oFace,yFace,rFace]
        a,b,c=graph[rFace][0][2],graph[rFace][1][2],graph[rFace][2][2]
        for i in faces:
            if i==wFace:
                d,e,f=graph[i][2][0],graph[i][2][1],graph[i][2][2]
                graph[i][2][0],graph[i][2][1],graph[i][2][2]=c,b,a
            elif i==oFace:
                d,e,f=graph[i][0][0],graph[i][1][0],graph[i][2][0]
                graph[i][0][0],graph[i][1][0],graph[i][2][0]=a,b,c
            elif i==yFace:
                d,e,f=graph[i][2][0],graph[i][2][1],graph[i][2][2]
                graph[i][2][0],graph[i][2][1],graph[i][2][2]=a,b,c
            else:
                graph[i][0][2],graph[i][1][2],graph[i][2][2]=c,b,a
            a,b,c=d,e,f
        transposeclock(graph[bFace])
    elif move =="b":
        faces=[wFace,rFace,yFace,oFace]
        a,b,c=graph[oFace][0][2],graph[oFace][1][2],graph[oFace][2][2]
        for i in faces:
            if i==wFace:
                d,e,f=graph[i][0][0],graph[i][0][1],graph[i][0][2]
                graph[i][0][0],graph[i][0][1],graph[i][0][2]=a,b,c
            elif i==rFace:
                d,e,f=graph[i][0][0],graph[i][1][0],graph[i][2][0]
                graph[i][0][0],graph[i][1][0],graph[i][2][0]=c,b,a
            elif i==yFace:
                d,e,f=graph[i][0][0],graph[i][0][1],graph[i][0][2]
                graph[i][0][0],graph[i][0][1],graph[i][0][2]=c,b,a
            else:
                graph[i][0][2],graph[i][1][2],graph[i][2][2]=a,b,c
            a,b,c=d,e,f
        transposeclock(graph[gFace])
    elif move=="b2":
        graph[wFace][0],graph[yFace][0]=graph[yFace][0],graph[wFace][0]
        
        a,b,c=graph[rFace][0][0],graph[rFace][1][0],graph[rFace][2][0]
        d,e,f=graph[oFace][0][2],graph[oFace][1][2],graph[oFace][2][2]
        graph[rFace][0][0],graph[rFace][1][0],graph[rFace][2][0]=f,e,d
        graph[oFace][0][2],graph[oFace][1][2],graph[oFace][2][2]=c,b,a

        transposeclock(graph[gFace])
        transposeclock(graph[gFace])
    elif move=="f2":
        graph[wFace][2],graph[yFace][2]=graph[yFace][2],graph[wFace][2]

        a,b,c=graph[oFace][0][0],graph[oFace][1][0],graph[oFace][2][0]
        d,e,f=graph[rFace][0][2],graph[rFace][1][2],graph[rFace][2][2]
        graph[oFace][0][0],graph[oFace][1][0],graph[oFace][2][0]=f,e,d
        graph[rFace][0][2],graph[rFace][1][2],graph[rFace][2][2]=c,b,a

        transposeclock(graph[bFace])
        transposeclock(graph[bFace])
    elif move=="r'":
        graphmove(graph,"r2")
        graphmove(graph,"r")
    elif move=="f'":
        graphmove(graph,"f2")
        graphmove(graph,"f")
    elif move=="u'":
        graphmove(graph,"u2")
        graphmove(graph,"u")
    elif move=="d'":
        graphmove(graph,"d2")
        graphmove(graph,"d")
    elif move=="l'":
        graphmove(graph,"l2")
        graphmove(graph,"l")
    elif move=="b'":
        graphmove(graph,"b2")
        graphmove(graph,"b")
        #print "something wrong in the notation, here is the notation",move
def solve(rubix):
    count=0
    moves=["l2","r2","u2","d2","f2","b2","l","r","u","d","f","b"]
    graphs=[rubix]
    movespermute=[[]]
    maximum=0
    while(count<=9):
        newgraphs=[]
        newmovespermute=[]
        p=0
        for r in graphs:
            #print r
            getpermute=False
            move1=moves[:]
            if r[yFace][0][1]=="W":
                move1.remove("b")
                move1.remove("b2")
            if r[yFace][2][1]=="W":
                move1.remove("f")
                move1.remove("f2")
            if r[yFace][1][2]=="W":
                move1.remove("l")
                move1.remove("l2")
            if r[yFace][1][0]=="W":
                move1.remove("r")
                move1.remove("r2")
                #move1.remove("r'")
            for i in move1:
                #print(i)
                permute= copy.deepcopy(r)
                graphmove(permute,i)
                if permute not in newgraphs and getcount(permute)>=maximum :
                    newgraphs.append(permute)
                    movespermute[p].append(i)
                    s=movespermute[p][:]
                    newmovespermute.append(s)
                    #print s
                    #printrubix(permute)
                    #print(s)
                    #raw_input()
                    movespermute[p].pop()
                    maximum=getcount(permute)
                    #print(getcount(permute))
                    if permute[yFace][0][1]=="W" and  permute[yFace][1][0]=="W" and permute[yFace][1][2]=="W" and permute[yFace][2][1]=="W":
                        #printrubix(permute)
                        return permute,s,"Yesssssssssssssssssssssssssssssssssssssssssss"
            p+=1
        movespermute=newmovespermute
        graphs=newgraphs
        count=count+1
        #print graphs
       #print movespermute
        #print count
    return movespermute,(graphs),None
def getcount(permute):
    count=0
    if permute[yFace][0][1]=="W":
        count=count+1
    if permute[yFace][1][0]=="W":
        count=count+1
    if permute[yFace][1][2]=="W":
        count=count+1
    if permute[yFace][2][1]=="W":
        count=count+1
    return count
def transposeclock(face):
    face[1][0],face[0][1],face[1][2],face[2][1]=face[2][1],face[1][0],face[0][1],face[1][2]
    face[2][0],face[0][0],face[0][2],face[2][2]=face[2][2],face[2][0],face[0][0],face[0][2]
def printrubix(graph):
    side=[0,1,2,3]
    for i in side:
        for r in range(3):
            if i==2:
                print (" ".join(graph[4][r])),
                print ("*"),
                print (" ".join(graph[2][r])),
                print ("*"),
                print (" ".join(graph[5][r]))
            else:
                print ("       "),
                print (" ".join(graph[i][r]))
        print("********************************")
    print ("###############")
def solvewhitecross(permute,s):
    faces=[bFace,oFace,gFace,rFace]
    move2=["f2","r2","b2","l2"]
    y_face_num=[(2,1),(1,0),(0,1),(1,2)]
    while permute[wFace][0][1]!="W" or permute[wFace][1][0]!="W" or permute[wFace][1][2]!="W" or permute[wFace][2][1]!="W":
        moves=["without move","d","d2","d'"]
        for r in moves:
            current=100
            phase=0 #1---left 2---right
            phaseshift=False
            b1 = copy.deepcopy(permute)
            if r!="without move":
                graphmove(b1,r)
            for i in range(len(faces)):
                a,b=y_face_num[i]
                if b1[faces[i]][2][1]==b1[faces[i]][1][1] and b1[yFace][a][b]=="W":
                    #print "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
                    permute=b1
                    phaseshift=True
                    printrubix(permute)
                    #print b1[faces[i]][2][1]
                    #print move2[i]
                    current=move2[i]
                    #print faces
                    #print move2
                    #raw_input()
                    break
            if phaseshift:
                if r!="without move":
                    s.append(r)
                graphmove(permute,current)
                s.append(current)
                #print "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXSDASDADASD"
                break
        printrubix(permute)
        #raw_input()
    return permute,s
def solvewhitelayer(permute,move_list):
    faces=[(bFace,oFace),(oFace,gFace),(gFace,rFace),(rFace,bFace)]
    p="p"
    q="q"
    v="v"
    s="s"
    p_q_r_s=[["r'","r","f","f'"],["b'","b","r","r'"],["l'","l","b","b'"],["f'","f","l","l'"]]
    moves=[["p","d'","q"],["v","d","s"],["p","d2","q","d","p","d'","q"]]
    while permute[wFace][0][0] !="W" or permute[wFace][0][2] !="W" or permute[wFace][2][0] !="W" or permute[wFace][2][2] !="W":
        raw_input()
        move=["without move","d","d2","d'"]
        printrubix(permute)
        for r in move:
            phase=100
            phaseshift=False
            #print r
            #print "YYYYYYYYYYYYYYYYYYYY"
            for i in range(4):
                move=r
                #print r
                #print"zzxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxzxzzxzx"
                current=i
                b1= copy.deepcopy(permute)
                if r!="without move":
                    graphmove(b1,r)
                x,y=faces[i]
                a,b,c=b1[x][1][1],b1[y][1][1],"W"
                d,e =b1[x][2][2],b1[y][2][0]
                if x==bFace:
                    f=b1[yFace][2][0]
                elif x==oFace:
                    f=b1[yFace][0][0]
                elif x==gFace:
                    f=b1[yFace][0][2]
                else:
                    f=b1[yFace][2][2]
                if a==d and c==e and b==f:
                    phase=True
                    phaseshift=True
                    phase=0
                    permute=b1
                    #print "xxxxxxxxxxxxxxxxxxxx"
                    #printrubix(permute)
                    #print"phase1",x,y,r
                    #raw_input()
                    break
                elif c==d and b==e and a==f:
                    phaseshift=True
                    permute=b1
                    phase=1
                    #print "xxxxxxxxxxxxxxxxxxxx"
                    #printrubix(permute)
                    #print"phase2",x,y,r
                    phaseshift=True
                    #raw_input()
                    break
                elif a==e and c==f and b==d:
                    phaseshift=True
                    permute=b1
                    #print "xxxxxxxxxxxxxxxxxxxx"
                    #printrubix(permute)
                    phase=2
                    #print"phase3",x,y,r
                    #raw_input()
                    break
            if phaseshift:
                newlist=[]
                #print move,
                #print ("#############################################33")
                if move!="without move":
                    move_list.append(r)
                    newlist.append(r)
                #print moves[phase]
                for z in moves[phase]:
                    #print z
                    if z=="p":
                        graphmove(permute,p_q_r_s[current][0])
                        move_list.append(p_q_r_s[current][0])
                        newlist.append(p_q_r_s[current][0])
                        #print p_q_r_s[current][0],
                    elif z=="q":
                        graphmove(permute,p_q_r_s[current][1])
                        move_list.append(p_q_r_s[current][1])
                        newlist.append(p_q_r_s[current][1])
                        #print p_q_r_s[current][1],
                    elif z=="v":
                        graphmove(permute,p_q_r_s[current][2])
                        move_list.append(p_q_r_s[current][2])
                        newlist.append(p_q_r_s[current][2])
                        #print p_q_r_s[current][2],
                    elif z=="s":
                        graphmove(permute,p_q_r_s[current][3])
                        move_list.append(p_q_r_s[current][3])
                        newlist.append(p_q_r_s[current][3])
                        #print p_q_r_s[current][3],
                    else:
                        graphmove(permute,z)
                        move_list.append(z)
                        newlist.append(z)
                        #print z
                printrubix(permute)
                print (newlist)
                raw_input()
                #print "WWWWWWWWWWWWWWWWWWww"
                break
        if (phaseshift)==False:
            white_in_first_layer(permute,move_list)
    return permute,move_list
def white_in_first_layer(permute,s):
    faces=[(bFace,oFace),(oFace,gFace),(gFace,rFace),(rFace,bFace)]
    moves=[["r'","d","r"],["b'","d","b"],["l'","d","l"],["f'","d","f"]]
    for i in range (len(faces)):
        x,y=faces[i]
        z=[permute[x][0][2],permute[y][0][0]]
        newmove=[]
        if "W" in z:
            for r in moves[i]:
                graphmove(permute,r)
                s.append(r)
                newmove.append(r)
            print (newmove)
            printrubix(permute)
            raw_input()
            return 
def thirdcorners(permute):
    faces=[bFace,oFace,gFace,rFace]
    for i in faces:
        if permute[i][1][0]!=permute[i][1][1] or permute[i][1][2]!=permute[i][1][1]:
            return True
    return False
def solvingsecondlayer(permute,move_list):
    print ("Second layer")
    faces=[bFace,oFace,gFace,rFace]
    sideFaces=[(rFace,oFace),(bFace,gFace),(oFace,rFace),(gFace,bFace)]#(Left,Right)
    y_face_num=[(2,1),(1,0),(0,1),(1,2)]
    moves=[["d'","p'","d","p","d","v","d'","v'"],["d","w","d'","w'","d'","v'","d","v"]]
    p_v_w=[["r","r'","f","f'","l","l'"],["b","b'","r","r'","f","f'"],["l","l'","b","b'","r","r'"],["f","f'","l","l'","b","b'"]]
    while thirdcorners(permute):
        move=["without move","d","d2","d'"]
        for i in move:
            face=100
            phase=0 #1---left 2---right
            phaseshift=False
            b1 = copy.deepcopy(permute)
            if i!="without move":
                graphmove(b1,i)
            for r in range(4):
                #print faces[r]
                if b1[faces[r]][2][1]==b1[faces[r]][1][1]:
                    x,y=y_face_num[r]
                    p,q=sideFaces[r]
                    #print"coming herereeeeeeeeeeee",b1[p][1][1],b1[q][1][1]
                    #print"co",b1[yFace][x][y]
                    #print"co",b1[yFace][1][1]
                    if b1[yFace][x][y]==b1[p][1][1]:
                        phase=1
                        face=r
                        phaseshift=True
                        print ("phase1")
                        permute=b1
                        printrubix(b1)
                        printrubix(permute)
                        break
                    elif b1[yFace][x][y]==b1[q][1][1]:
                        phase=0
                        face=r
                        phaseshift=True
                        print ("phase2")
                        permute=b1
                        printrubix(b1)
                        printrubix(permute)
                        break
            if phaseshift:
                newlist=[]
                if i!="without move":
                    move_list.append(i)
                    newlist.append(i)
                for i in moves[phase]:
                    if i=="p":
                        graphmove(permute,p_v_w[face][0])
                        move_list.append(p_v_w[face][0])
                        newlist.append(p_v_w[face][0])
                    elif i=="p'":
                        graphmove(permute,p_v_w[face][1])
                        move_list.append(p_v_w[face][1])
                        newlist.append(p_v_w[face][1])
                    elif i=="v":
                        graphmove(permute,p_v_w[face][2])
                        move_list.append(p_v_w[face][2])
                        newlist.append(p_v_w[face][2])
                    elif i=="v'":
                        graphmove(permute,p_v_w[face][3])
                        move_list.append(p_v_w[face][3])
                        newlist.append(p_v_w[face][3])
                    elif i=="w":
                        graphmove(permute,p_v_w[face][4])
                        move_list.append(p_v_w[face][4])
                        newlist.append(p_v_w[face][4])
                    elif i=="w'":
                        graphmove(permute,p_v_w[face][5])
                        move_list.append(p_v_w[face][5])
                        newlist.append(p_v_w[face][5])
                    else:
                        graphmove(permute,i)
                        move_list.append(i)
                        newlist.append(i)
                    #cornersFine(permute)
                printrubix(permute)
                print(newlist)
                raw_input()
                break
            #printrubix(permute)
            #raw_input()
    return permute,move_list
def yellowcross(permute,s):
    while permute[yFace][0][1]!="Y" or permute[yFace][1][0]!="Y" or permute[yFace][1][2]!="Y" or permute[yFace][2][1]!="Y":
        moves=["nothing to move","d","d2","d'"]
        for i in moves:
            print (i)
            phaseshift=False
            b1= copy.deepcopy(permute)
            if i!= "nothing to move":
                graphmove(b1,i)
            if b1[bFace][2][1]=="Y" and b1[rFace][2][1]=="Y" and b1[gFace][2][1]=="Y" and b1[oFace][2][1]=="Y":
                permute=b1
                move_list=["f","l","d","l'","d'","f'"]
                phaseshift=True
                break
            elif b1[yFace][0][1]=="Y" and b1[yFace][1][0]=="Y":
                permute=b1
                move_list=["f","d","l","d'","l'","f'"]
                phaseshift=True
                break
            elif  b1[yFace][1][0]=="Y" and b1[yFace][1][2]=="Y":
                permute=b1
                move_list=["f","l","d","l'","d'","f'"]
                phaseshift=True
                break
        if phaseshift:
            new_list=[]
            if i!="nothing to move":
                s.append(i)
                new_list.append(i)
            for r in move_list:
                graphmove(permute,r)
                s.append(r)
                new_list.append(r)
            printrubix(permute)
            print (new_list)
            raw_input()
    return permute,s
def swapcornerBoolean(permute):
    faces=[bFace,oFace,gFace,rFace]
    for i in faces:
        if permute[i][2][1]!=permute[i][1][1]:
            return True
    return False
def swapcorners(permute,s):
    print ("             swapcorners                  ")
    while swapcornerBoolean(permute):
        pair_of_faces=[(bFace,rFace),(oFace,bFace),(gFace,oFace),(gFace,rFace)]
        moves=[["b","d","b'","d","b","d2","b'","d"],["l","d","l'","d","l","d2","l'","d"],["f","d","f'","d","f","d2","f'","d"],["r","d","r'","d","r","d2","r'","d"]]
        basicmoves=["without move","d","d2","d'"]
        current=""
        for r in basicmoves:
            #print r
            b1= copy.deepcopy(permute)
            if r!="without move":
                graphmove(b1,r)
                #printrubix(b1)
            for i in range(len(pair_of_faces)):
                phaseShift=False
                x,y= pair_of_faces[i]
                if b1[x][1][1]==b1[y][2][1] and b1[y][1][1]==b1[x][2][1]:
                    permute=b1
                    move_list=moves[i]
                    phaseShift=True
                    current=r
                    break
            if phaseShift:
                break
            if b1[gFace][2][1]==b1[bFace][1][1] and b1[gFace][1][1]==b1[bFace][2][1]:
                permute=b1
                move_list=["d","b","d","b'","d","b","d2","b'","d"]
                phaseShift=True
                current=r
                break
            elif b1[rFace][2][1]==b1[oFace][1][1] and b1[rFace][1][1]==b1[oFace][2][1]:
                    permute=b1
                    move_list=["d","r","d","r'","d","r","d2","r'","d"]
                    phaseShift=True
                    current=r
                    break
        if phaseShift:
            new_list=[]
            if current != "without move":
                s.append(current)
                new_list.append(current)
            for r in move_list:
                graphmove(permute,r)
                s.append(r)
                new_list.append(r)
            printrubix(permute)
            print (new_list)
        raw_input()
    return permute,s
def orientedcorners(permute):
    faces=[(bFace,rFace),(rFace,gFace),(gFace,oFace),(oFace,bFace)]
    yellowFaces=[(2,2),(0,2),(0,0),(2,0)]
    for r in range(4):
        x,y=faces[r]
        p,q=yellowFaces[r]
        z=[permute[x][2][0],permute[y][2][2],permute[yFace][p][q]]
        print (z)
        print ([permute[x][1][1],permute[y][1][1],permute[yFace][1][1]])
        phaseShift=False
        if permute[x][1][1] not in z or permute[y][1][1] not in z or permute[yFace][1][1] not in z:
            return True
    return False
def positionYellowCorners(permute,s):
    print ("positionYellowCorners")
    faces=[(bFace,rFace),(rFace,gFace),(gFace,oFace),(oFace,bFace)]
    yellowFaces=[(2,2),(0,2),(0,0),(2,0)]
    while orientedcorners(permute):
        moves=[["d","l","d'","r'","d","l'","d'","r"],["d","b","d'","f'","d","b'","d'","f"],["d","r","d'","l'","d","r'","d'","l"],["d","f","d'","b'","d","f'","d'","b"]]
        for r in range(4):
            x,y=faces[r]
            p,q=yellowFaces[r]
            z=[permute[x][2][0],permute[y][2][2],permute[yFace][p][q]]
            phaseShift=False
            if permute[x][1][1] in z and permute[y][1][1] in z and permute[yFace][1][1] in z:
                move_list=moves[r]
                phaseShift=True
                break
        if phaseShift:
            new_list=[]
            for i in move_list:
                graphmove(permute,i)
                s.append(i)
                new_list.append(i)
        else:
            new_list=[]
            for i in ["d","l","d'","r'","d","l'","d'","r"]:
                graphmove(permute,i)
                s.append(i)
                new_list.append(i)
        printrubix(permute)
        print (new_list)
        raw_input()
def corners(permute):
    yellowFaces=[(2,2),(0,2),(0,0),(2,0)]
    for i in yellowFaces:
        x,y=i
        if permute[yFace][x][y]!="Y":
            return True
    return False
def orientedLastLayer(permute,s):
    move=False
    while corners(permute):
        move=True
        moves=["l'","u'","l","u"]
        while permute[yFace][2][2]!="Y":
            for r in moves:
                graphmove(permute,r)
                s.append(r)
            print (moves)
        printrubix(permute)
        graphmove(permute,"d")
        s.append("d")
        raw_input()
    if move:
        graphmove(permute,"d2")
        s.append("d2")
        printrubix(permute)
def countColor(permute):
    countR=0
    countG=0
    countB=0
    countY=0
    countW=0
    countO=0
    for i in permute:
        for r in i:
            for z in r:
                if z=="W":
                    countW+=1
                elif z=="Y":
                    countY+=1
                elif z=="O":
                    countO+=1
                elif z=="R":
                    countR+=1
                elif z=="G":
                    countG+=1
                elif z=="B":
                    countB+=1
    if countW!=9 or countY!=9 or countO!=9 or countR!=9 or countG!=9 or countB!=9 :
        print ("Wrong",countW,countY,countO,countR,countG,countB)
def evaluvate(s):
    post=len(s)
    pre=0
    while pre!=post:
        c=[]
        post=len(s)
        for i in range(0,len(s)-1,2):
            x=s[i]
            y=s[i+1]
            if x==y:
                c.append(x+"2")
            elif x+"2"==y:
                c.append(x+"'")
            elif y+"2"==x:
                c.append(y+"'")
            elif y+"'"==x:
                continue
            elif x+"'"==y:
                continue  
            else:
                c.append(x)
                c.append(y)
        s=c
        pre=len(c)
    return s
b3= copy.deepcopy(rubix)
countColor(rubix)
b3,c,a=solve(b3)
printrubix(b3)
print (c)
raw_input()
b3,c=solvewhitecross(b3,c)
print (c)
raw_input()
b3,c=solvewhitelayer(b3,c)
printrubix(b3)
print (c)
print (len(c))
b3,c=solvingsecondlayer(b3,c)
printrubix(b3)
print (c)
print (len(c))
b3,c=yellowcross(b3,c)
s5=c[:]
print (c)
print (len(c))
b3,c=swapcorners(b3,c)
printrubix(b3)
print (c)
print (len(c))
positionYellowCorners(b3,c)
printrubix(b3)
print (c)
print (len(c))
orientedLastLayer(b3,c)
printrubix(b3)
print (c)
print (len(c))
q=evaluvate(c)
print (q)
print (len(q))
for r in q:
    graphmove(rubix,r)
printrubix(rubix)

