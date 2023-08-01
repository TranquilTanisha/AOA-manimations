from manim import *

def take_input(n,v,a):
    v=input("Enter the vertices separated by space: ").split()
    print("Enter the adjacency matrix row-wise: ")
    for i in range(n):
        a.append([int(x) for x in input().split()])

    for i in range(n):
        for j in range(n):
            if i==j:
                a[i][j]=0
    return v
 
class Apsp(Scene):
    def construct(self):
        tan=Text("LinkedIn: tanisha-kaur\nGithub: TranquilTanisha", color=GREY_B).scale(0.3).to_corner(DR)
        self.add(tan)

        s=Title(f"Floyd Warshall Algorithm", color=TEAL_B).scale(1.2)
        self.play(Write(s), run_time=2)
        self.wait(1)

        n=int(input("Enter the number of vertices: "))
        cost=[]
        a=[]
        v=[]
        v=take_input(n,v,a)
        cost=a.copy()

        #To plot the points
        p=self.cr_circle(n, v)

        #To generate edges
        line=[] #To store the line co-ordinates for each edge 
        text=[]
        for i in range(n):
            line.append([0]*n)
            text.append([0]*n)
        line,text=self.cr_edges(cost, n,p,line, text)

        c1=Circle(radius=0.3, color=YELLOW) #via which vertex
        c2=Circle(radius=0.3, color=PURE_BLUE) #from which vertex
        c3=Circle(radius=0.3, color=PURE_GREEN) #to which vertex

        c2.scale(0.7)
        c1.scale(0.7).next_to(c1, UP*0.5)
        c3.scale(0.7).next_to(c2, DOWN*0.5)
        t=Text("Controls", color=BLUE).scale(0.6).next_to(c1, UP)
        t1=Text("Via vertex").scale(0.5).next_to(c1, RIGHT)
        g1=VGroup(c1,t1)
        b=Text("From vertex").scale(0.5).next_to(c2, RIGHT)
        g2=VGroup(c2,b)
        c=Text("To vertex").scale(0.5).next_to(c3, RIGHT)
        g3=VGroup(c3,c)

        self.play(Write(t), run_time=1)
        self.play(FadeIn(g1), run_time=1)
        self.play(FadeIn(g2), run_time=1)
        self.play(FadeIn(g3), run_time=1)
        self.wait(3)
        self.play(FadeOut(t), FadeOut(g1), FadeOut(g2), FadeOut(g3), run_time=1)

        # show matrix
        mat=IntegerMatrix(a, left_bracket="[", right_bracket="]", v_buff=0.8, h_buff=1.5, color=GREY_A).shift(RIGHT*3).scale(0.6)
        eq=Tex("=", color=GREY_A).next_to(mat, LEFT).scale(0.7)
        t=Text("A0", color=GREY_A).next_to(eq, LEFT).scale(0.65)

        c1=Circle(radius=0.3, color=YELLOW) #via which vertex
        c11=Circle(radius=0.2, color=BLUE) #direct text
        c2=Circle(radius=0.3, color=PURE_BLUE) #from which vertex
        c22=Circle(radius=0.2, color=BLUE)
        c3=Circle(radius=0.3, color=PURE_GREEN) #to which vertex
        c33=Circle(radius=0.2, color=BLUE)
        sq=Square(side_length=0.5, color=GREEN).move_to(mat.get_rows()[0][0])

        self.play(FadeIn(t), FadeIn(eq), run_time=1)
        self.play(Create(mat), run_time=1)
        self.wait(2)
        self.play(Create(sq), FadeOut(t))

        mat1=IntegerMatrix(a, left_bracket="[", right_bracket="]", v_buff=0.8, h_buff=1.5, color=GREY_A).shift(RIGHT*3).scale(0.6)
        # mat1.get_rows()[0].set_color(GREY_B)
        # mat1.get_columns()[0].set_color(GREY_B)
        self.play(ReplacementTransform(mat, mat1), run_time=1)
        mat=mat1

        #Start APSP
        for k in range(n):
            t=Text("A"+str(k+1), color=GREY_A).next_to(eq, LEFT).scale(0.65)
            c1.move_to(p[k])
            self.play(FadeIn(t), FadeIn(c1), run_time=0.5) 

            t1=Text("min { ", color=BLUE).scale(0.8).next_to(mat, DOWN*4+LEFT*2)
            self.play(FadeIn(t1), run_time=1)

            for i in range(n):
                c2.move_to(p[i])
                if i!=k:
                    self.play(FadeIn(c2), run_time=0.5)

                for j in range(n):
                    mat1=IntegerMatrix(a, left_bracket="[", right_bracket="]", v_buff=0.8, h_buff=1.5, color=GREY_A).shift(RIGHT*3).scale(0.6)
                    mat1.get_rows()[k].set_color(GREY_B)
                    mat1.get_columns()[k].set_color(GREY_B)
                    self.play(ReplacementTransform(mat, mat1), run_time=1)
                    mat=mat1

                    # a[i][j]=min(a[i][j], a[i][k]+a[k][j])   
                    self.play(sq.animate.move_to(mat.get_rows()[i][j]), run_time=1) 
                    
                    if i==k or j==k or i==j:
                        pass

                    else:                 
                        c3.move_to(p[j])  
  
                        if j!=k:
                            self.play(FadeIn(c3), run_time=1)   
                            if i!=k:
                                if a[i][j]==999:          
                                    t2=Tex("$\\infty$").scale(0.7).next_to(t1, RIGHT)     
                                else:
                                    t2=Tex(a[i][j]).scale(0.7).next_to(t1, RIGHT) 
                                if a[i][k]==999 or a[k][j]==999:
                                    t3=Tex("$\\infty$").scale(0.7).next_to(t2, RIGHT*2)
                                else:
                                    t3=Tex(a[i][k]+a[k][j]).scale(0.7).next_to(t2, RIGHT*2)
                                self.play(FadeIn(t2), FadeIn(t3), run_time=1)

                        if (a[i][j]!=0 and a[i][j]!=999) or (a[i][k]!=0 and a[i][k]!=999 and a[k][j]!=0 and a[k][j]!=999):

                            if a[i][j]<=a[i][k]+a[k][j]:
                                if line[i][j]!=0:
                                    ll=Line(line[i][j][0], line[i][j][1], color=BLUE)
                                    length=ll.get_length()
                                    ar=Arrow(line[i][j][0], line[i][j][1], color=BLUE).set_length(length-0.7)
                                    # ar=Arrow(line[i][j][0], line[i][j][1], color=BLUE).set_length(line[i][j][2])
                                    c11.move_to(text[i][j])

                                    self.play(Create(ar),Create(c11), run_time=1)
                                    # self.wait(1)
                                    self.play(FadeOut(ar), FadeOut(c11), run_time=1)

                            elif a[i][k]+a[k][j]<a[i][j]:
                                if line[i][k]!=0 and line[k][j]!=0:
                                    ll=Line(line[i][k][0], line[i][k][1], color=BLUE_C)
                                    len=ll.get_length()
                                    ar1=Arrow(line[i][k][0], line[i][k][1], color=BLUE_C).set_length(len-0.7)
                                    # ar1=Arrow(line[i][k][0], line[i][k][1], color=BLUE_C).set_length(line[i][j][2])

                                    ll=Line(line[k][j][0], line[k][j][1], color=BLUE_C)
                                    len=ll.get_length()
                                    ar2=Arrow(line[k][j][0], line[k][j][1], color=BLUE_C).set_length(len-0.7)
                                    # ar2=Arrow(line[k][j][0], line[k][j][1], color=BLUE_C).set_length(line[i][j][2])
                                    c22.move_to(text[i][k])
                                    c33.move_to(text[k][j])

                                    self.play(Create(ar1), run_time=1)
                                    self.play(Create(ar2), Create(c22), Create(c33), run_time=1)
                                    self.play(FadeOut(ar1), FadeOut(ar2),FadeOut(c22), FadeOut(c33), run_time=1)

                                else:
                                    c22.move_to(mat.get_rows()[i][k])
                                    c33.move_to(mat.get_rows()[k][j])
                                    self.play(Create(c22), Create(c33), run_time=1)
                                    self.play(FadeOut(c22), FadeOut(c33), run_time=1)

                        if (a[i][j]!=999 or a[i][j]!=0) and a[i][j]<a[i][k]+a[k][j]:
                            self.play(Circumscribe(t2, shape=Rectangle, color=PURPLE_B, fade_out=True), run_time=1)
                        elif ((a[i][k]+a[k][j])!=0 or (a[i][k]+a[k][j]!=999)) and a[i][k]+a[k][j]<999:
                            self.play(Circumscribe(t3, shape=Rectangle, color=PURPLE_B, fade_out=True), run_time=1)

                        if a[i][j]>a[i][k]+a[k][j]:
                            a[i][j]=a[i][k]+a[k][j]
                            # mat.get_rows()[i][j].set_value(a[i][j])
                        mat1=IntegerMatrix(a, left_bracket="[", right_bracket="]", v_buff=0.8, h_buff=1.5, color=GREY_A).shift(RIGHT*3).scale(0.6)
                        mat1.get_rows()[k].set_color(GREY_B)
                        mat1.get_columns()[k].set_color(GREY_B)
                        self.play(ReplacementTransform(mat, mat1), run_time=1)
                        mat=mat1

                        if j!=k:
                            if i!=k:
                                self.play(FadeOut(t2), FadeOut(t3), run_time=1)
                            self.play(FadeOut(c3), run_time=1)                 
            if i!=k:
                self.play(FadeOut(c2), run_time=0.5)
            self.play(FadeOut(t), FadeOut(c1), FadeOut(t1), run_time=1)

        self.play(FadeOut(eq), FadeOut(sq))
        self.wait(2)  
        self.clear()
        tan=Text("LinkedIn: tanisha-kaur\nGithub: TranquilTanisha", color=GREY_B).scale(0.3).to_corner(DR)
        self.add(tan)
        t=Text("Thank you!", color=BLUE).scale(1.2)
        self.play(Write(t), run_time=1)
        self.play(Circumscribe(t), run_time=1)
        self.wait(2)  

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

    def cr_edges(self,a,n,p,line,text):
        for i in range(n):
            for j in range(n):
                if a[i][j]!=0 and a[i][j]!=999:
                    if i!=j:                      
                        l1=Line(p[i], p[j], color=YELLOW)       
                        l=Line(l1.get_start(), p[i]+[0.3,0,0])
                        length=l1.get_length()
                        an=l1.get_angle()
                        an=an*180/PI
                        ang=Angle(l, l1, radius=0.1)
                        arr=Arrow(ang.get_end(),p[j]).set_length(length-0.8)
                        line[i][j]=[ang.get_end(), p[j]]

                        if an==0:
                            line[i][j]=[l.get_end(), p[j]]

                        if an<0:
                            an=360+an

                        t=Tex(a[i][j]).scale(0.4)
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