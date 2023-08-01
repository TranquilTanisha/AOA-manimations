from manim import *

# n=int(input("Enter the number of vertices "))
# m=int(input("Enter the number of colors: "))
# cost=[]

n=4
m=4
v=[1,2,3,4]
cost=[[0,1,0,1], [1,0,1,0], [0,1,0,1], [1,0,1,0]]
x=[0]*n
l=[]# To store the minimum number o colors required
colors=[GOLD_D, PURPLE_D,  PINK, BLUE_D, ORANGE, MAROON]

class Graph_coloring(Scene):
    def construct(self):
        tan=Text("LinkedIn: tanisha-kaur\nGithub: TranquilTanisha", color=GREY_B).scale(0.3).to_corner(DR)
        self.add(tan)

        s=Title(f"Graph Coloring", color=TEAL_B).scale(1.2)
        self.play(Write(s), run_time=2)
        self.wait(1)

        matrix = IntegerMatrix(cost).scale(0.6).move_to(LEFT*3)
        t=Text("Given Matrix:", color=BLUE).scale(0.5).next_to(matrix, UP)
        self.play(FadeIn(t), run_time=1)
        self.play(Create(matrix))
        self.wait(1)

        p=self.cr_circle(n, v)

        #To generate edges
        line=[] #To store the line co-ordinates for each edge 
        text=[]
        for i in range(n):
            line.append([0]*n)
            text.append([0]*n)
        line,text=self.cr_edges(cost, n,p,line, text)

        self.play(FadeOut(t), FadeOut(matrix), run_time=1)

        self.coloring(0)

        t1=Text("Minimum number of\ncolors required = "+str(len(l)), t2c={str(len(l)): BLUE}).scale(0.6).move_to(t)
        t2=Text("Possible Solution: ", color=BLUE).scale(0.6).next_to(t1, DOWN*2)
        self.play(FadeIn(t1), run_time=1)
        self.play(FadeIn(t2), run_time=1)

        for i in range(n):
            c=Circle(radius=0.3, color=colors[x[i]-1], fill_opacity=0.7).move_to(p[i])
            t=Tex(v[i]).move_to(p[i]).scale(0.6)
            self.play(FadeIn(c), FadeIn(t), run_time=2)

        self.wait(3)
        self.clear()
        tan=Text("LinkedIn: tanisha-kaur\nGithub: TranquilTanisha", color=GREY_B).scale(0.3).to_corner(DR)
        self.add(tan)
        t=Text("Thank you!", color=BLUE).scale(1.2)
        self.play(Write(t), run_time=1)
        self.play(Circumscribe(t), run_time=1)
        self.wait(2) 

    def coloring(self, k):
        self.nextvalue(k)
        if x[k]==0:
            print("No color is possible")

        elif k==n-1:
            print("Possibility: ")
            print(x)
            # l=[]
            for i in range(n):
                if x[i] not in l:
                    l.append(x[i])
            # print("Minimum number of colors required: ", len(l))
            # return len(l)
            
        else:
            self.coloring(k+1)

    def nextvalue(self, k):
        while True:
            x[k]=(x[k]+1)%(m+1)
            j=0
            while j<n:
                if cost[k][j]!=0 and x[k]==x[j]:
                    break
                j+=1
            if j==n:
                break

    def cr_circle(self, n, v):
        r=2
        circle = Circle(radius=r).shift(RIGHT*3) 
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
                    if i!=j and i<j:                      
                        l1=Line(p[i], p[j], color=YELLOW)       
                        l=Line(l1.get_start(), p[i]+[0.3,0,0])
                        length=l1.get_length()
                        an=l1.get_angle()
                        an=an*180/PI
                        ang=Arc(start_angle=0, angle=an, radius=0.06).move_to(p[i])
                        arr=Line(ang.get_end(),p[j]).set_length(length-0.8)
                        line[i][j]=[ang.get_end(), p[j], length-0.8]

                        if an==0:
                            line[i][j]=[l.get_end(), p[j], length-0.8]

                        self.play(Create(arr), run_time=0.3)                      

        return line, text