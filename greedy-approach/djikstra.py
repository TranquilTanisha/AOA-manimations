from manim import *

def take_input(n):
    print("Enter the cost matrix row-wise: ")
    cost=[]
    for i in range(n):
        c=list(map(int,input().split()))
        cost.append(c)
    return cost

class Dijkstra(Scene):
    def construct(self):
        tan=Text("LinkedIn: tanishakaur\nGithub: TranquilTanisha", color=GREY_B).scale(0.3).to_corner(DR)
        self.add(tan)

        s=Title(f"Dijkstra's Algorithm", color=TEAL_B).scale(1.2)
        self.play(Write(s), run_time=2)
        self.wait(1)

        # n=int(input("Enter the number of vertices: "))
        # v=list(map(int,input().split()))

        n=6
        v=[1,2,3,4,5,6]
        cost=[[999,2,4,999,999,999],
            [999,999,1,7,999,999],
            [999,999,999,999,3,999],
            [999,999,999,999,999,1],
            [999,999,999,2,999,5],
            [999,999,999,999,999,999]]

        # cost=take_input(n)
        p=self.cr_circle(n, v)

        #To generate edges
        line=[] #To store the line co-ordinates for each edge 
        text=[]
        for i in range(n):
            line.append([0]*n)
            text.append([0]*n)
        line,text=self.cr_edges(cost, n,p,line, text)

        c1=Circle(radius=0.3, color=PINK).move_to(p[0]) #THE VERTEX TAKEN IN CONSIDERATION
        c2=Circle(radius=0.15, color=BLUE) #for the text
        c3=Circle(radius=0.3, color=TEAL).move_to(p[0]) #THE VERTEX TAKEN IN CONSIDERATION

# DIJKSTRA START
        s=[False]*(n)
        minim=[]
        visited=[0]
        # cost[0][0]=0
        dist=cost[0].copy()
        s[0]=True
        k=1

        cc=self.modify(n,v)
        
        tab=MathTable(cc, include_outer_lines=True).scale(0.4).move_to(RIGHT*3)
        # sign=Text(">").scale(0.6).next_to(tab, DOWN*2)
        sign=Text(">").scale(0.6).move_to(DOWN*2.5)
        plus=Text("+").scale(0.6)

        self.play(FadeIn(tab), run_time=1)
        self.wait(1)
        self.play(FadeIn(c1))
        cc,tab=self.change(cost,cost[0],cc,n,line,text,tab,0, c2,0)
        self.play(FadeOut(c1))

        for i in range(n-1):
            tab.get_columns()[1].set_color(GREY)
            nxt=dist.index(min(dist)) #TO CHOSE THE NEXT VERTEX

            if s[nxt]==True:
                tp=dist.copy()
                for j in minim:
                    del tp[tp.index(j)]
                nxt=dist.index(min(tp))

            s[nxt]=True
            visited.append(nxt)
            minim.append(dist[nxt])

            c1.move_to(p[nxt])

            cc[k+1][0]=v[nxt]
            tab1=MathTable(cc, include_outer_lines=True).scale(0.4).move_to(RIGHT*3)
            self.play(Circumscribe(tab.get_rows()[k][nxt+1], shape=Rectangle, fade_out=True), run_time=2)
            for j in visited:
                tab1.get_columns()[j+1].set_color(GREY)
            self.play(ReplacementTransform(tab,tab1), FadeIn(c1), run_time=1)
            tab=tab1

            # cc,tab=self.change(cost,cost[nxt],cc,n,line,text,tab,nxt, c2,k)

            for j in range(n):
                if s[j]==False :
                    # dist[j]
                    self.play(Circumscribe(tab.get_rows()[k][j+1], shape=Circle, color=PURPLE_B, fade_out=True), run_time=1)
                    if cc[k][j+1]!=999:
                        a1=Tex(cc[k][j+1], color=BLUE).scale(0.6).next_to(sign, LEFT)
                    else:
                        a1=Tex("$\\infty$").scale(0.6).next_to(sign, LEFT)
                    self.play(Write(a1), FadeIn(sign), run_time=1)
                    self.wait(1)

                    #dist[nxt]
                    self.play(Circumscribe(tab.get_rows()[k][nxt+1], shape=Circle, color=PURPLE_B, fade_out=True), run_time=1)
                    if cc[k][nxt]!=999:
                        a2=Tex(cc[k][nxt+1], color=BLUE).scale(0.6).next_to(sign, RIGHT)
                    else:
                        a2=Tex("$\\infty$").scale(0.6).next_to(sign, RIGHT)
                    plus.next_to(a2,RIGHT)
                    self.play(Write(a2), FadeIn(plus), un_time=1)

                    if cost[nxt][j]!=999:
                        arr=Arrow(line[nxt][j][0], line[nxt][j][1], color=YELLOW).set_length(line[nxt][j][2])
                        c2.move_to(text[nxt][j])
                        self.play(Create(arr), FadeIn(c2), run_time=1)
                        self.play(FadeOut(arr), FadeOut(c2), run_time=1)
                        a3=Tex(str(cost[nxt][j]), color=BLUE).scale(0.6).next_to(plus, RIGHT)
                    else:
                        a3=Tex("$\\infty$").scale(0.6).next_to(plus, RIGHT*0.5)
                    self.play(Write(a3), run_time=1)
                    self.wait(1)

                    if dist[j]>(dist[nxt]+cost[nxt][j]):
                        dist[j]=dist[nxt]+cost[nxt][j]
                        b=Text("True").scale(0.5).next_to(sign, DOWN)
                        self.play(Write(b), run_time=1)

                    else:
                        if dist[j]==999 and (dist[nxt]==999 or cost[nxt][j]==999):
                            b=Text("No Change").scale(0.5).next_to(sign, DOWN)
                        else:
                            b=Text("False").scale(0.5).next_to(sign, DOWN)

                        self.play(Write(b), run_time=1)

                    self.play(FadeOut(a1), FadeOut(a2), FadeOut(a3), FadeOut(b), FadeOut(plus), run_time=1)

                # else:
                cc[k+1][j+1]=dist[j]
                cc[k+1][1]=0
                tab1=MathTable(cc, include_outer_lines=True).scale(0.4).move_to(RIGHT*3)
                for j in visited:
                    tab1.get_columns()[j+1].set_color(GREY)
                self.play(ReplacementTransform(tab,tab1), run_time=1)
                tab=tab1

            k+=1

        self.play(FadeOut(c1), FadeOut(sign), run_time=1)
        for j in visited:
            tab.get_columns()[j+1].set_color(WHITE)
        self.wait(3)
        # self.play(FadeOut(tab))

        dist[0]=0
        d=[["Vertex", "Distance"]]
        for i in range(n):
            d.append([v[i], dist[i]])

        tab1=MathTable(d, include_outer_lines=True).scale(0.4).move_to(RIGHT*3)
        self.play(ReplacementTransform(tab,tab1), run_time=1)
        self.wait(3)
        self.clear()
        tan=Text("LinkedIn: tanishakaur\nGithub: TranquilTanisha", color=GREY_B).scale(0.3).to_corner(DR)
        self.add(tan)
        t=Text("Thank you!", color=BLUE).scale(1.2)
        self.play(Write(t), run_time=1)
        self.play(Circumscribe(t), run_time=1)
        self.wait(2) 

    # CALLED ONCE
    def modify(self, n, v):
        cc=[]
        for i in range(n+1):
            cc.append([-1]*(n+1))
        cc[0][0]="X"

        for i in range(len(v)):
            cc[0][i+1]=v[i]
        cc[1][0]=v[0]
        cc[1][1]=0
        return cc

    def change(self,cost,d,cc,n,line,text,tab,nxt, c2, k):
        for j in range(n):
            if cost[nxt][j]!=999 and cost[nxt][j]!=0:
                arr=Arrow(line[nxt][j][0], line[nxt][j][1], color=YELLOW).set_length(line[nxt][j][2])
                c2.move_to(text[nxt][j])
                self.play(Create(arr), FadeIn(c2), run_time=1)
                self.play(FadeOut(arr), FadeOut(c2), run_time=1)

            cc[k+1][j+1]=d[j]
            cc[1][1]=0
            tab1=MathTable(cc, include_outer_lines=True).scale(0.4).move_to(RIGHT*3)
            self.play(ReplacementTransform(tab,tab1), run_time=1)
            tab=tab1
        return cc,tab

    def cr_circle(self, n, v):
        r=2
        circle = Circle(radius=r).shift(LEFT*4) 
        p=[] #To store the center of the circular vertices
        for i in range(n):
            # p.append(circle.point_from_proportion(i/n))
            c=Circle(radius=0.3, color=RED_C).move_to(circle.point_from_proportion(i/n))
            p.append(c.get_center())
            t=Tex(v[i], color=GREY_A).move_to(p[i]).scale(0.6)
            self.play(GrowFromPoint(c,circle.get_center()), run_time=0.3)
            self.play(FadeIn(t), run_time=0.3)

        return p

    def cr_edges(self, cost, n, p, line, text):
        for i in range(n):
            for j in range(n):
                if cost[i][j]!=999 :
                    if i!=j:                      
                        l1=Line(p[i], p[j], color=YELLOW)       
                        l=Line(l1.get_start(), p[i]+[0.3,0,0])
                        length=l1.get_length()
                        an=l1.get_angle()
                        an=an*180/PI
                        ang=Arc(start_angle=0, angle=an, radius=0.06).move_to(p[i])
                        arr=Arrow(ang.get_end(),p[j]).set_length(length-0.8)
                        line[i][j]=[ang.get_end(), p[j], length-0.8]

                        if an==0:
                            line[i][j]=[l.get_end(), p[j], length-0.8]

                        if an<0:
                            an=360+an

                        #TO ALIGN TEXTS
                        t=Tex(cost[i][j]).scale(0.4)
                        if an==0 or an==360 or an==2*PI or an==-2*PI:
                            t.next_to(arr.get_center(), UP*0.5+LEFT*(arr.get_length()/4))
                        elif round(an)==90 or an==PI/2:
                            t.next_to(arr.get_center(), LEFT*0.5+DOWN*(arr.get_length()/4))
                        elif an==180 or an==PI or an==-PI:
                            t.next_to(arr.get_center(), DOWN*0.5+RIGHT*(arr.get_length()/4))
                        elif an==270 or an==-PI/2:
                            t.next_to(arr.get_center(), RIGHT*0.5+UP*(arr.get_length()/4))  


                        elif an>0 and an<90:
                            t.next_to(arr.get_center(), UP*0.5+LEFT*0.2)
                        elif an>90 and an<180: 
                            t.next_to(arr.get_center(), UP*0.5+RIGHT*0.2)
                        elif an>180 and an<270:
                            t.next_to(arr.get_center(), UP*0.5+LEFT*0.2)
                        else:
                            t.next_to(arr.get_center(), DOWN*0.5+LEFT*0.2)

                        text[i][j]=t.get_center()
                        self.play(GrowArrow(arr), run_time=0.3)                      
                        self.play(FadeIn(t), run_time=0.3)

        return line, text