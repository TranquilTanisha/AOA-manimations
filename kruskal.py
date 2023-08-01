from manim import *

p=[]
t=[]
cost=[]
edges=[]
n=0

def union(j, k):
    p[k]=j

def find(i):
    while p[i]>=0:
        i=p[i]
    return i

def take_input(n):
    print("Enter the cost matrix row-wise: ")
    cost=[]
    for i in range(n):
        c=list(map(int,input().split()))
        cost.append(c)
    return cost

class Kruskal(Scene):
    def construct(self):
        # tan=Text("LinkedIn: tanisha-kaur\nGithub: TranquilTanisha", color=GREY_B).scale(0.3).to_corner(DR)
        # self.add(tan)

        s=Title(f"Kruskal's Algorithm", color=TEAL_B).scale(1.2)
        self.play(Write(s), run_time=2)
        self.wait(1)

        # n=int(input("Enter the number of vertices: "))
        # v=list(map(int,input().split()))
        # cost=take_input(n)

        n=7
        v=[1,2,3,4,5,6,7]
        edges=[]
        cost=[[999, 28, 999,999,999,10,999], 
              [28,999,16,999,999,999,14],
              [999,16,999,12,999,999,999],
              [999,999,12,999,22,999,18],
              [999,999,999,22,999,22,24],
              [10,999,999,999,22,999,999],
              [999,14,999,18,24,999,999]]

        for i in range(n):
            for j in range(n):
                if cost[i][j]!=999 and i<j:
                    edges.append([cost[i][j], [i,j]])

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

        min_c=Text("Cost = ", color=BLUE).scale(0.6). next_to(ORIGIN, RIGHT*10+DOWN*11)
        cst=Tex("0", color=BLUE).scale(0.7).next_to(min_c, RIGHT*0.5)
        self.play(FadeIn(min_c), FadeIn(cst), run_time=1)

        self.kruskal(edges,n, min_c, cst, line,text,line1,text1)
        self.wait(3)
        self.clear()
        tan=Text("LinkedIn: tanisha-kaur\nGithub: TranquilTanisha", color=GREY_B).scale(0.3).to_corner(DR)
        self.add(tan)
        t=Text("Thank you!", color=BLUE).scale(1.2)
        self.play(Write(t), run_time=1)
        self.play(Circumscribe(t), run_time=1)
        self.wait(2) 

    def kruskal(self, edges,n, min_c, cst, line,text,line1,text1):
        for i in range(n-1):
            t.append([0, 0])

        edges.sort()
        for i in range(n):
            p.append(-1)
        
        i=0
        l=0 #iterator
        mc=0 #for the min cost
        while l<(n-1) and edges!=None:
            u=edges[0][1][0]
            v=edges[0][1][1]
            w=edges[0][0]
            del edges[0]
            j=find(u)
            k=find(v)

            ln=Line(line[u][v][0],line[u][v][1]).set_color(YELLOW) #for the line to be considered (applicable for all lines)
            c11=Circle(radius=0.2, color=BLUE_C).move_to(text[u][v])

            self.play(Create(ln), run_time=0.7)
            self.play(FadeIn(c11), run_time=0.7)
            self.play(FadeOut(c11), FadeOut(ln), run_time=0.7)

            if j!=k:
                l1=Line(line1[u][v][0], line1[u][v][1])
                t1=Tex(w).scale(0.4).move_to(text1[u][v])

                self.play(FadeIn(t1), Create(l1), run_time=0.7)

                t[i][0]=u
                t[i][1]=v
                mc+=w
                union(j,k)
                i+=1
                l+=1

                cst1=Tex(str(mc)).scale(0.7).next_to(min_c, RIGHT*0.5)
                self.play(ReplacementTransform(cst,cst1), run_time=1)
                cst=cst1
                # self.wait(1)
            
            else:
                ln.set_color(GREY)
                self.play(Create(ln), run_time=0.7)

        print("The minimum spanning tree is: ",t)
        print("Mincost is: ",mc)

    
    def cr_circle(self, n, v, dir, m):
        r=2
        circle = Circle(radius=r).shift(dir*m) 
        a=[] #To store the center of the circular vertices
        for i in range(n):
            # p.append(circle.point_from_proportion(i/n))
            c=Circle(radius=0.3, color=RED_C).move_to(circle.point_from_proportion(i/n))
            a.append(c.get_center())
            t=Tex(v[i], color=GREY_A).move_to(a[i]).scale(0.6)
            self.play(GrowFromPoint(c,circle.get_center()), run_time=0.3)
            self.play(FadeIn(t), run_time=0.3)

        return a

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
                            self.play(Create(l), run_time=0.5)

                        line[i][j]=[l.get_start(), l.get_end()]
                        line[j][i]=[l.get_end(), l.get_start()]

                        if an==0:
                            line[i][j]=[l.get_end(), p[j], length-0.8]

                        if an<0:
                            an=360+an

                        #TO ALIGN TEXTS
                        t=Tex(cost[i][j]).scale(0.4)
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