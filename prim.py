from manim import *

def take_input(n):
    print("Enter the cost matrix row-wise: ")
    cost=[]
    for i in range(n):
        c=list(map(int,input().split()))
        cost.append(c)
    return cost

class Prim(Scene):
    def construct(self):
        tan=Text("LinkedIn: tanishakaur\nGithub: TranquilTanisha", color=GREY_B).scale(0.3).to_corner(DR)
        self.add(tan)

        s=Title(f"Prim's Algorithm", color=TEAL_B).scale(1.2)
        self.play(Write(s), run_time=2)
        self.wait(1)

        # n=int(input("Enter the number of vertices: "))
        # v=list(map(int,input().split()))
        # cost=take_input(n)

        n=7
        v=[1,2,3,4,5,6,7]
        cost=[[999, 28, 999,999,999,10,999], 
              [28,999,16,999,999,999,14],
              [999,16,999,12,999,999,999],
              [999,999,12,999,22,999,18],
              [999,999,999,22,999,22,24],
              [10,999,999,999,22,999,999],
              [999,14,999,18,24,999,999]]

        p=self.cr_circle(n, v, LEFT, 4)

        #To generate edges
        line=[] #To store the line co-ordinates for each edge 
        text=[] #To store the center of texts
        line1=[]
        text1=[]
        for i in range(n):
            line.append([0]*n)
            line1.append([0]*n)
            text.append([0]*n)
            text1.append([0]*n)

        line,text=self.cr_edges(cost, n,p,line, text, "q")

        mst=Text("MST: ", color=BLUE).scale(0.6)
        self.play(Write(mst), run_time=1)

        p1=self.cr_circle(n, v, RIGHT, 4)
        line1, text1=self.cr_edges(cost, n,p1, line1,text1, "a")

        t=[]
        e=[]
        near=[]

        for i in range(n):
            for j in range(n):
                if i<j and cost[i][j]!=999:
                    e.append([cost[i][j],[i,j]])

        e.sort()
        min_cost=e[0][0]
        k=e[0][1][0]
        l=e[0][1][1]
        del e[0]
        t.append([k,l])

        ln=Line(line[k][l][0],line[k][l][1]).set_color(YELLOW) #for the line to be considered (applicable for all lines)
        c11=Circle(radius=0.2, color=BLUE_C) #for the text
        l1=Line(line1[k][l][0], line1[k][l][1])#line for the minimum weight
        t1=Tex(min_cost, color=MAROON_A).scale(0.4).move_to(text1[k][l])
        txt=Text("min {").next_to(ORIGIN, DOWN*5).to_edge(DL).scale(0.8)
        min_c=Text("Cost = ").scale(0.65). next_to(txt, RIGHT*32)
        cst=Tex(min_cost, color=BLUE).scale(0.7).next_to(min_c, RIGHT*0.5)

        self.play(Create(ln), run_time=1) 
        self.play(Create(l1), FadeIn(t1), run_time=1)
        self.play(FadeOut(ln), run_time=1)
        self.play(FadeIn(txt), FadeIn(min_c), FadeIn(cst), run_time=1)

        for i in range(n):
            if cost[i][l]<cost[i][k]:
                near.append(l)
            else:
                near.append(k)

        near[k]=near[l]=-1

        for i in range(1, n-1):
            temp=[]
            for j in range(n):
                if near[j]!=-1 and cost[j][near[j]]!=999:
                    temp.append([cost[j][near[j]],[j,near[j]]]) 
                    # print(temp)
                    temp.reverse()
                    k=temp[0][1][0]
                    l=temp[0][1][1]
                    l2=Line(line[l][k][0], line[l][k][1]).set_color(YELLOW)     
                    c11.move_to(text[k][l])
                    self.play(Create(l2), run_time=1)
                    self.play(FadeIn(c11), run_time=1)
                    self.play(FadeOut(l2), FadeOut(c11), run_time=1)

            temp.sort()

            s=""
            for i in range(len(temp)):
                s+=str(temp[i][0])+"  "            

            t.append(temp[0][1])
            k=temp[0][1][0]
            l=temp[0][1][1]
            min_cost+=temp[0][0]
            near[temp[0][1][0]]=-1

            ln=Line(line[l][k][0],line[l][k][1]).set_color(YELLOW)

            l1=Line(line1[l][k][0], line1[l][k][1])#line for the minimum weight
            txt2=Tex(temp[0][0], color=MAROON_A).scale(0.4).move_to(text1[k][l])
            txt1=Text(s, color=BLUE).scale(0.5).next_to(txt, RIGHT*0.5)
            cst1=Tex(min_cost, color=BLUE).scale(0.7).next_to(min_c, RIGHT*0.5)

            self.play(FadeIn(txt1), run_time=1)
            self.play(Create(ln), run_time=1) 
            self.play(Create(l1), FadeIn(txt2), FadeOut(ln), FadeOut(txt1), run_time=1)
            self.play(ReplacementTransform(cst,cst1), run_time=1)
            cst=cst1
            self.wait(1)

            for k in range(n):
                if near[k]!=-1 and cost[k][near[k]]>cost[k][temp[0][1][0]]:
                    near[k]=temp[0][1][0]

        print("The minimum cost is: ",min_cost)
        print(t)

        self.play(FadeOut(txt), run_time=1)

        self.wait(3)
        self.clear()
        tan=Text("LinkedIn: tanishakaur\nGithub: TranquilTanisha", color=GREY_B).scale(0.3).to_corner(DR)
        self.add(tan)
        t=Text("Thank you!", color=BLUE).scale(1.2)
        self.play(Write(t), run_time=1)
        self.play(Circumscribe(t), run_time=1)
        self.wait(2) 

    def cr_circle(self, n, v, dir, m):
        r=2
        circle = Circle(radius=r).shift(dir*m) 
        p=[] #To store the center of the circular vertices
        for i in range(n):
            # p.append(circle.point_from_proportion(i/n))
            c=Circle(radius=0.3, color=RED_C).move_to(circle.point_from_proportion(i/n))
            p.append(c.get_center())
            t=Tex(v[i], color=GREY_A).move_to(p[i]).scale(0.6)
            self.play(GrowFromPoint(c,circle.get_center()), run_time=0.3)
            self.play(FadeIn(t), run_time=0.3)

        return p

    def cr_edges(self, cost, n, p, line, text, tp):
        for i in range(n):
            for j in range(n):
                if cost[i][j]!=999 :
                    if i!=j and i<j:                      
                        l1=Line(p[i], p[j], color=YELLOW)       
                        l=Line(l1.get_start(), p[i]+[0.3,0,0])
                        length=l1.get_length()
                        an=l1.get_angle()
                        an=an*180/PI
                        ang=Angle(l, l1, radius=0.06)
                        l=Line(ang.get_end(), p[j]).set_length(length-0.65)
                        if tp=="q":
                            self.play(Create(l), run_time=0.7)

                        line[i][j]=[l.get_start(), l.get_end()]
                        line[j][i]=[l.get_end(), l.get_start()]

                        if an==0:
                            line[i][j]=[l.get_end(), p[j], length-0.8]

                        if an<0:
                            an=360+an

                        #TO ALIGN TEXTS
                        t=Tex(cost[i][j], color=MAROON_A).scale(0.4)
                        if an==0 or an==360 or an==2*PI or an==-2*PI:
                            t.next_to(l.get_center(), UP*0.5+LEFT*(l.get_length()/4))
                        elif round(an)==90 or an==PI/2:
                            t.next_to(l.get_center(), LEFT*0.5+DOWN*(l.get_length()/4))
                        elif an==180 or an==PI or an==-PI:
                            t.next_to(l.get_center(), DOWN*0.5+RIGHT*(l.get_length()/4))
                        elif an==270 or an==-PI/2:
                            t.next_to(l.get_center(), RIGHT*0.5+UP*(l.get_length()/4))  


                        elif an>0 and an<90:
                            t.next_to(l.get_center(), UP*0.5+LEFT*0.2)
                        elif an>90 and an<180: 
                            t.next_to(l.get_center(), UP*0.5+RIGHT*0.2)
                        elif an>180 and an<250:
                            t.next_to(l.get_center(), UP*0.5+LEFT*0.2)
                        else:
                            t.next_to(l.get_center(), DOWN*0.5+LEFT*0.2)

                        text[i][j]=text[j][i]=t.get_center()                     
                        if tp=="q":
                            self.play(FadeIn(t), run_time=0.3)

        return line, text