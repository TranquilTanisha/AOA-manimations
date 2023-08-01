from manim import *

#tab-for profit and weight
#tab1- replacement of tab
#tab2- for ratio (p/w)
# tab3- replacement of tab2
#tab4- for order (x)
#tab5- replacement of tab3
#tab6- for u
#tab7- replacement of tab6

# def check(a,b):
#     if a<=b:
#         return "True"
#     else:
#         return "False"

class Fractional_Knapsack(Scene):
    def construct(self):
        tan=Text("LinkedIn: tanisha-kaur\nGithub: TranquilTanisha", color=GREY_B).scale(0.3).to_corner(DR)
        self.add(tan)

        s=Title(f"Fractional Knapsack Problem", color=TEAL_B).scale(1.2)
        self.play(Write(s), run_time=2)
        self.wait(1)

        m=int(input("Enter the weight of the bag: "))
        n=int(input("Enter the no of items: "))
        print("Enter profit and weight")
        k=[]
        for i in range(n):
            p,w=map(int,input().split())
            k.append([round(p/w,2),p,w])
 
        t1=Text("Knapsack Capacity (m): "+str(m), t2c={"Knapsack Capacity (m): ": BLUE}).scale(0.5).next_to(s, DOWN*2).to_edge(LEFT)
        # t2=Text("Items: ", color=BLUE).scale(0.5).next_to(t1, DOWN)
        self.play(FadeIn(t1), run_time=1)

        t=self.arrange(k, n)
        tab=MathTable(t, include_outer_lines=True).scale(0.5).move_to(LEFT*4)

        pw=self.weight_sort(k, n)
        tab2=MathTable(pw, include_outer_lines=True).scale(0.5).move_to(LEFT)

        self.play(Create(tab), run_time=4)
        self.play(Create(tab2), run_time=2)
        self.wait(2)   

        k.sort(reverse=True)
        t=self.arrange(k, n)
        tab1=MathTable(t, include_outer_lines=True).scale(0.5).move_to(tab.get_center())
        pw1=self.weight_sort(k, n)
        tab3=MathTable(pw1, include_outer_lines=True).scale(0.5).move_to(tab2.get_center())
        text=Text("Sorting in descending order of Ratio", t2c={"Ratio": BLUE}).scale(0.5).move_to(DOWN*3)

        self.play(FadeIn(text), run_time=0.7)
        self.play(ReplacementTransform(tab, tab1), ReplacementTransform(tab2,tab3), run_time=1)
        tab=tab1
        tab2=tab3
        pw=pw1
        self.play(FadeOut(text), run_time=0.7)
        self.wait(1) 

        #FRACTIONAL KNAPSACK STARTS HERE

        total_p=0
        u=m
        x=[0]*n
        o=self.modify(x, n)
        # tab4=MathTable(o, include_outer_lines=True).scale(0.5).next_to(tab2, RIGHT*3)
        tab4=MathTable(o, include_outer_lines=True).scale(0.5).move_to(RIGHT)
        self.play(FadeIn(tab4), run_time=1)
        self.wait(1)

        uu=[[0]]*(n+1)
        uu[0]=["Remaining(m-w)"]
        tab6=MathTable(uu, include_outer_lines=True).scale(0.5).move_to(RIGHT*4)
        self.play(FadeIn(tab6), run_time=1)
        self.wait(1)

        for i in range(n):
            print(i)
            self.play(Circumscribe(tab.get_rows()[i+1][1], shape=Rectangle, color=YELLOW, fade_out=True), run_time=2)
            if k[i][2]<=u:
                b="True"
            else:
                b="False"
            t3=Text(str(k[i][2])+" <= "+str(u), t2c={" <=":BLUE}).scale(0.5).move_to(DOWN*2)
            t4=Text(b, color=GOLD).scale(0.5).next_to(t3, DOWN*0.5)
            self.play(FadeIn(t3), run_time=1)
            self.play(FadeIn(t4), run_time=1)

            if k[i][2]<=u:
                x[i]=1

                o1=self.modify(x, n)
                tab5=MathTable(o1, include_outer_lines=True).scale(0.5).move_to(tab4.get_center())
                self.play(ReplacementTransform(tab4, tab5), run_time=1)
                tab4=tab5
                self.play(Indicate(tab4.get_rows()[i+1][0]), run_time=2)

                uu=self.remaining(u, k[i][2], uu, i)
                tab7=MathTable(uu, include_outer_lines=True).scale(0.5).move_to(tab6.get_center())
                self.play(ReplacementTransform(tab6, tab7), run_time=1)
                tab6=tab7
                self.wait(1)

                u-=k[i][2]

                uu[i+1]=[u]
                tab7=MathTable(uu, include_outer_lines=True).scale(0.5).move_to(tab6.get_center())
                tab7.get_rows().set_color(GREY_D)
                tab7.get_rows()[i+1][0].set_color(YELLOW_A)
                tab7.get_rows()[0][0].set_color(WHITE)
                self.play(ReplacementTransform(tab6, tab7), run_time=1)
                tab6=tab7

            else:
                t=1
                x[i]=str(u)+"/"+str(k[i][2])

                o1=self.modify(x, n)
                tab5=MathTable(o1, include_outer_lines=True).scale(0.5).move_to(tab4.get_center())
                self.play(ReplacementTransform(tab4, tab5), run_time=1)
                tab4=tab5
                self.wait(1)

                x[i]=round(u/k[i][2],2)

                o1=self.modify(x, n)
                tab5=MathTable(o1, include_outer_lines=True).scale(0.5).move_to(tab4.get_center())
                self.play(ReplacementTransform(tab4, tab5), run_time=1)
                tab4=tab5
                self.play(Indicate(tab4.get_rows()[i+1][0]), run_time=2)

                uu[i+1]=[0]
                tab7=MathTable(uu, include_outer_lines=True).scale(0.5).move_to(tab6.get_center())
                tab7.get_rows().set_color(GREY_D)
                tab7.get_rows()[i+1][0].set_color(YELLOW_A)
                tab7.get_rows()[0][0].set_color(WHITE)
                self.play(ReplacementTransform(tab6, tab7), run_time=1)
                tab6=tab7

                break

            self.play(FadeOut(t3), FadeOut(t4), run_time=1)

        if t==1:
            self.play(FadeOut(t3), FadeOut(t4), run_time=1)

        self.play(FadeOut(tab2), FadeOut(tab6), tab.animate.move_to(LEFT*2), tab4.animate.move_to(RIGHT*2), run_time=1)
        p=Text("Total Profit = ", color=BLUE).scale(0.5).move_to(DOWN*2+LEFT*0.5)
        self.play(FadeIn(p), run_time=1)
        tab.get_columns()[1].set_color(GREY_B)

        t=""
        for i in range(n):
            if x[i]!=0:
                t+=str(k[i][1])+"*"+str(x[i])+" + "
                total_p+=k[i][1]*x[i]

        t3=Text(t[:len(t)-2]).scale(0.5).next_to(p, RIGHT*0.5)
        self.play(FadeIn(t3), run_time=1)
        self.wait(3)
        t4=Tex(total_p).scale(0.6).next_to(p, RIGHT*0.5)
        self.play(ReplacementTransform(t3,t4), run_time=1)

        self.wait(3)
        self.clear()
        tan=Text("LinkedIn: tanisha-kaur\nGithub: TranquilTanisha", color=GREY_B).scale(0.3).to_corner(DR)
        self.add(tan)
        t=Text("Thank you!", color=BLUE).scale(1.2)
        self.play(Write(t), run_time=1)
        self.play(Circumscribe(t), run_time=1)
        self.wait(2) 

    def arrange(self, k, n):
        t=[-1]*(n+1)
        l=1
        t[0]=["Profit", "Weight"]
        for i in range(n):
            t[l]=[k[i][1], k[i][2]]
            l+=1

        return t
    
    def weight_sort(self, k, n):
        a=[]
        l=1
        a.append(["Ratio"])
        for i in range(n):
            a.append([k[i][0]])
            l+=1

        return a
    
    def modify(self, x, n):
        a=[0]*(n+1)
        # l=1
        a[0]=["x"]
        for i in range(n):
            a[i+1]=[x[i]]
            # l+=1
        return a
    
    def remaining(self, u, z, uu, i):
        uu[i+1]=[str(u)+"-"+str(z)+"="+str(u-z)]
        return uu
        
    


