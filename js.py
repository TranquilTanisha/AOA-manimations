from manim import *

class JobScheduling(Scene):
    def construct(self):
        tan=Text("LinkedIn: tanisha-kaur\nGithub: TranquilTanisha", color=GREY_B).scale(0.3).to_corner(DR)
        self.add(tan)

        s=Title(f"Job Scheduling with Deadline", color=TEAL_B).scale(1.2)
        self.play(Write(s), run_time=2)
        self.wait(1)

        n=int(input("Enter the no of jobs: "))
        print("Enter profit and deadline")
        pd=[]
        dead=[]
        for i in range(n):
            pd.append([int(x) for x in input().split()])
            dead.append(pd[i][1])
            pd[i].append(i+1)

        t=self.arrange(pd, n)
        tab=MathTable(t, include_outer_lines=True).scale(0.5).move_to(UP*0.5)
        p=Text("Total Profit=", color=BLUE).scale(0.5).next_to(tab, RIGHT*3)
        tp=Text("0").scale(0.5).next_to(p, RIGHT*0.5)
        gr=VGroup(tab, p, tp).next_to(s, DOWN*3)
        self.play(Create(gr), run_time=4)
        self.wait(1)   

        pd.sort(reverse=True)
        t=self.arrange(pd, n)
        text=Text("Sorting in descending order of Profit", t2c={"Profit": BLUE}).scale(0.5).move_to(DOWN*2.5)
        tab1=MathTable(t, include_outer_lines=True).scale(0.5).move_to(tab.get_center())
        self.play(FadeIn(text), run_time=0.7)
        self.play(ReplacementTransform(tab, tab1), run_time=1)
        tab=tab1
        self.play(FadeOut(text), run_time=0.7)
        self.wait(0.8) 

        m=max(dead)
        ni=min(dead)
        order=[-1]*m

        tab2=MathTable([order], include_outer_lines=True).scale(0.5).next_to(tab, DOWN*4)
        minimum=Tex(ni-1, color=BLUE).scale(0.5).next_to(tab2.get_rows()[0][0], DOWN*2+LEFT*1.25)
        maximim=Tex(m, color=BLUE).scale(0.5).next_to(tab2.get_rows()[0][m-1], DOWN*2+RIGHT*1.75)
        o=Text("Order:", color=BLUE).scale(0.5).next_to(tab2, LEFT*1.25)

        self.play(GrowFromCenter(tab2), FadeIn(o), run_time=1)
        self.play(FadeIn(minimum), FadeIn(maximim), run_time=1)
        self.wait(1)

        slot=[False]*m
        total_p=0

        for i in range(n):
            self.play(Circumscribe(tab.get_rows()[i+1], shape=Rectangle, color=YELLOW, buff=0.16, fade_in=True, fade_out=True), run_time=2)
            self.wait(0.5)
            for j in range(min(m,pd[i][1])-1,-1,-1):
                if -1 in order[:min(m,pd[i][1])]:
                    if slot[j]==False:
                        slot[j]=True
                        order[j]="J"+str(pd[i][2])

                        tab3=MathTable([order], include_outer_lines=True).scale(0.5).next_to(tab, DOWN*4)
                        tab3.get_rows()[0][j].set_color(YELLOW)
                        self.play(ReplacementTransform(tab2, tab3), run_time=1)
                        tab2=tab3

                        total_p+=pd[i][0]
                        self.play(Circumscribe(tab.get_rows()[i+1][1], shape=Rectangle, color=PURPLE_B, buff=0.15, fade_out=True), run_time=2)
                        tp1=Text(str(total_p)).scale(0.5).next_to(p, RIGHT*0.5)
                        self.play(ReplacementTransform(tp, tp1), run_time=1)
                        tp=tp1
                        break

                else:
                    # self.play(Circumscribe(tab.get_rows()[i+1], shape=Rectangle, color=YELLOW, buff=0.165, fade_in=True, fade_out=True), run_time=2)
                    tab.get_rows()[i+1].set_color(GREY)
                    break

        self.wait(3)
        self.clear()
        tan=Text("LinkedIn: tanisha-kaur\nGithub: TranquilTanisha", color=GREY_B).scale(0.3).to_corner(DR)
        self.add(tan)
        t=Text("Thank you!", color=BLUE).scale(1.2)
        self.play(Write(t), run_time=1)
        self.play(Circumscribe(t), run_time=1)
        self.wait(2) 

    def arrange(self, pd, n):
        t=[-1]*(n+1)
        k=1
        t[0]=["Job", "Profit", "Deadline"]
        for i in range(n):
            t[k]=["J"+str(pd[i][2]), pd[i][0], pd[i][1]]
            k+=1

        return t


