from manim import *
import math

def take_input(n,v,cost):
    v=input("Enter the vertices separated by space: ").split()
    print("Enter the adjacency matrix row-wise: ")
    for i in range(n):
        cost.append([int(x) for x in input().split()])
    return v

class GenerateGraph(Scene):
    def construct(self):
        tan=Text("LinkedIn: tanishakaur \nGithub: TranquilTanisha", color=GREY_B).scale(0.3).to_corner(DR)
        self.add(tan)

        s=Title(f"Construct Graph", color=TEAL_B).scale(1.2)
        self.play(Write(s), run_time=2)
        self.wait(1)

        n=int(input("Enter the number of vertices: "))
        cost=[]
        v=[]
        v=take_input(n,v,cost)

        mat=IntegerMatrix(cost).scale(0.7).shift(LEFT*4)
        # z=Text("A = ", color=BLUE).scale(0.6).next_to(mat, LEFT)
        sq=Square(side_length=0.7, color=TEAL_B).scale(0.6).move_to(mat.get_rows()[0][0])

        # self.play(FadeIn(z), run_time=0.5)
        self.play(FadeIn(mat), run_time=1)
        self.wait(1)
        
        r=1.8
        circle = Circle(radius=r).shift(RIGHT*3)  # create a circle
        p=[]
        for i in range(n):
            # p.append(circle.point_from_proportion(i/n))
            c=Circle(radius=0.3, color=RED_E).move_to(circle.point_from_proportion(i/n))
            p.append(c.get_center())
            t=Tex(v[i], color=GREY_A).move_to(p[i]).scale(0.6)
            self.play(GrowFromPoint(c,circle.get_center()), run_time=0.3)
            self.play(FadeIn(t), run_time=0.3)

        #To generate arrows
        # theeta=(n-2)*PI/n #interior angle
        self.play(FadeIn(sq), run_time=0.5)
        for i in range(n):
            for j in range(n):
                self.play(sq.animate.move_to(mat.get_rows()[i][j]), run_time=1)
                if cost[i][j]!=0 and cost[i][j]!=999:
                    if i!=j:                      
                        l1=Line(p[i], p[j], color=YELLOW)       
                        l=Line(l1.get_start(), p[i]+[0.3,0,0])
                        len=l1.get_length()
                        an=l1.get_angle()
                        an=an*180/PI
                        ang=Angle(l, l1, radius=0.1)
                        arrow=Arrow(ang.get_end(),p[j], color=RED_C).set_length(len-0.8)
                    
                        if an<0:#Convert to degrees
                            an=360+an
                        # print(an)

                        t=Tex(cost[i][j]).scale(0.6)
                        if an==0 or an==360 or an==2*PI or an==-2*PI: #To align text
                            t.next_to(arrow.get_center(), UP*0.5+LEFT*(arrow.get_length()/4))
                        elif round(an)==90 or an==PI/2:
                            t.next_to(arrow.get_center(), LEFT*0.5+DOWN*(arrow.get_length()/4))
                        elif an==180 or an==PI or an==-PI:
                            t.next_to(arrow.get_center(), DOWN*0.5+RIGHT*(arrow.get_length()/4))                        
                        elif an==270 or an==-PI/2:
                            t.next_to(arrow.get_center(), RIGHT*0.5+UP*(arrow.get_length()/4))
                        
                        elif i<j:
                            t.next_to(l1.get_center(), DOWN)
                        elif i>j:
                            t.next_to(l1.get_center(), UP)
                        # self.play(GrowArrow(arrow), run_time=0.3)
                        # elif an>0 and an<90:
                        #     t.next_to(arrow.get_center(), DOWN*0.5+LEFT*0.2)
                        # elif an>90 and an<180: 
                        #     t.next_to(arrow.get_center(), UP*0.5+RIGHT*0.2)
                        # elif an>180 and an<270:
                        #     t.next_to(arrow.get_center(), UP*0.5+LEFT*0.2)
                        # else:
                        #     t.next_to(arrow.get_center(), DOWN*0.5+LEFT*0.2)

                        self.play(GrowArrow(arrow), run_time=0.7)                      

                    else:
                        l1=Line(p[i], p[i]+[0.3,0,0]).set_angle((-1+i)*PI/2)
                        l2=Line(p[i], p[i]+[0.3,0,0]).set_angle((-1+i)*PI/2+PI/2)
                        an=Angle(l1, l2, radius=0.3)
                        arc=Arc(radius=0.7, start_angle=(-1+i)*PI/2, angle=PI/2, color=RED, arc_center=an.get_center())
                        circle=Circle.from_three_points(an.get_start(), arc.get_center(), an.get_end(), color=RED)
                        c=Circle(radius=0.3).move_to(p[i])
                        diff=Difference(circle, c, color=RED_C)
                        t=Tex(str(cost[i][j]), color=MAROON_A).move_to(diff.get_center())
                        t.scale(0.5)
                        self.play(Create(diff), run_time=0.3)
                      
                    self.play(FadeIn(t), run_time=0.3)
        
        self.play(FadeOut(sq))
        self.wait(3)
        self.clear()
        tan=Text("LinkedIn: tanishakaur \nGithub: TranquilTanisha", color=GREY_B).scale(0.3).to_corner(DR)
        self.add(tan)
        t=Text("Than you!", color=BLUE)
        self.play(Write(t), run_time=1)
        self.play(Circumscribe(t), run_time=0.7)
        self.wait(2)        