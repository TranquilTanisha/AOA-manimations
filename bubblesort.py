from manim import *

def check(l,j):
    if l[j]>l[j+1]:
        b=Tex("True", color=BLUE).scale(0.7)
    else:
        b=Tex("False", color=BLUE).scale(0.7)
    return b

class BubbleSort(Scene):
    def construct(self):
        tan=Text("LinkedIn: tanisha-kaur\nGithub: TranquilTanisha", color=GREY_B).scale(0.3).to_corner(DR)
        self.add(tan)

        s=Title(f"Bubble Sort", color=TEAL_B).scale(1.2)
        self.play(Write(s), run_time=2)
        self.wait(1)

        l=[int(x) for x in input("Enter the list of numbers: ").split()]
        n=len(l)
        # s1=Text("Initial array: ", color=BLUE).scale(0.7)
        # tab1=MathTable([l], include_outer_lines=True).scale(0.7).next_to(s1, RIGHT*2)
        tab1=MathTable([l], include_outer_lines=True).scale(0.7).next_to(s, DOWN*4)
        # gr=VGroup(s1, tab1).next_to(s, DOWN*4)

        # self.play(Create(gr), run_time=3)
        self.play(Create(tab1), run_time=2)
        self.wait(1)

        tab2=MathTable([l], include_outer_lines=True).scale(0.7).next_to(tab1, DOWN*4)
        s2=Text("Iteration", color=BLUE).scale(0.7).next_to(tab2, LEFT*4)
        sign=Text(">", color=BLUE).scale(0.7).next_to(tab2, DOWN*6.7)

        self.play(FadeIn(s2), run_time=1)   
        self.play(Create(tab2), run_time=2)
        self.play(FadeIn(sign), run_time=1)

        for i in range(n-1):
            it=Text(str(i+1), color=BLUE).scale(0.7).next_to(s2, RIGHT)
            self.play(FadeIn(it), run_time=1)

            for j in range(n-i-1):
                b1=Tex(l[j]).scale(0.7).next_to(sign, LEFT)
                b2=Tex(l[j+1]).scale(0.7).next_to(sign, RIGHT)
                b=check(l, j)
                b.next_to(sign, DOWN)

                self.play(Circumscribe(tab2.get_rows()[0][j], color=PURPLE_B, buff=0.15, fade_out=True, run_time=2), Circumscribe(tab2.get_rows()[0][j+1], color=PURPLE_B, buff=0.15, fade_out=True, run_time=2))
                self.play(FadeIn(b1), FadeIn(b2), run_time=1)
                self.play(Write(b), run_time=1)
                self.play(FadeOut(b), FadeOut(b1), FadeOut(b2), run_time=1)

                if l[j]>l[j+1]:
                    arr=CurvedDoubleArrow(tab2.get_rows()[0][j].get_center(), tab2.get_rows()[0][j+1].get_center(), color=PURPLE_B).shift(DOWN*0.7).scale(0.7)
                    swap=Text("Swap", color=PURPLE_B).scale(0.5).next_to(arr, DOWN*0.5)

                    l[j],l[j+1]=l[j+1],l[j]
                    tab3=MathTable([l], include_outer_lines=True).scale(0.7).next_to(tab1, DOWN*4)

                    self.play(Create(arr), run_time=1)
                    self.play(FadeIn(swap), run_time=1)
                    self.play(FadeOut(arr), FadeOut(swap),ReplacementTransform(tab2, tab3), run_time=1)
                    tab2=tab3

            self.play(FadeOut(it), run_time=1)
            tab3=tab2
            for k in range(n-1, n-i-2, -1):
                tab3.get_rows()[0][k].set_color(GOLD_B)
            self.play(ReplacementTransform(tab2, tab3), run_time=1)
            tab2=tab3
        
        tab2.get_rows()[0][0].set_color(GOLD_B)

        self.play(FadeOut(sign), FadeOut(s2), run_time=1)
        # s2=Text("After Sorting:", color=BLUE).scale(0.7).next_to(s1, DOWN*5)
        # self.play(Write(s2), run_time=1)
        self.wait(3)
        self.clear()
        tan=Text("LinkedIn: tanisha-kaur\nGithub: TranquilTanisha", color=GREY_B).scale(0.3).to_corner(DR)
        self.add(tan)
        t=Text("Thank you!", color=BLUE).scale(1.2)
        self.play(Write(t), run_time=1)
        self.play(Circumscribe(t), run_time=1)
        self.wait(2) 
