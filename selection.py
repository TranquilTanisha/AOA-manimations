from manim import *

def check(l,i,j):
    if l[j]<l[i]:
        b=Tex("True", color=BLUE).scale(0.8)
    else:
        b=Tex("False", color=BLUE).scale(0.8)
    return b

class SelectionSort(Scene):
    def construct(self):
        tan=Text("LinkedIn: tanishakaur\nGithub: TranquilTanisha", color=GREY_B).scale(0.3).to_corner(DR)
        self.add(tan)

        s=Title(f"Selection Sort", color=TEAL_B).scale(1.2)
        self.play(Write(s), run_time=2)
        self.wait(1)

        l=[int(x) for x in input("Enter the list of numbers: ").split()]
        # s1=Text("Initial array: ", color=BLUE).scale(0.7)
        tab1=MathTable([l], include_outer_lines=True).scale(0.7).next_to(s, DOWN*3)
        self.play(Create(tab1), run_time=2)

        tab2=MathTable([l], include_outer_lines=True).scale(0.7).next_to(tab1, DOWN*4)
        s2=Text("Iteration", color=BLUE).scale(0.7).next_to(tab2, LEFT*4)
        sign=Text(">", color=BLUE).scale(0.7).next_to(tab2, DOWN*4)
        # sign=Text(">", color=BLUE).scale(0.7).next_to(tab2, RIGHT*3)

        self.play(Create(tab2), run_time=2)
        self.play(FadeIn(s2), run_time=1)   
        self.play(FadeIn(sign), run_time=1)

        sq1=Text("i", color=GREEN).scale(0.5).next_to(tab2.get_rows()[0][0], UP*2)
        sq2=Text("j", color=ORANGE).scale(0.5).next_to(tab2.get_rows()[0][1], UP*2)
        self.play(FadeIn(sq1), run_time=1)

        for i in range(len(l)-1):
            if i>0:
                tab2.get_rows()[0][:i].set_color(GREY_B)
            it=Text(str(i+1)).scale(0.7).next_to(s2, RIGHT)
            j=i+1

            sq2.next_to(tab2.get_rows()[0][j], UP*2)
            self.play(FadeIn(it), sq1.animate.next_to(tab2.get_rows()[0][i], UP*2), FadeIn(sq2), run_time=1)

            while j<len(l):
                b1=Tex(l[i]).scale(0.8).next_to(sign, LEFT)
                b2=Tex(l[j]).scale(0.8).next_to(sign, RIGHT)
                b=check(l, i, j)
                b.next_to(sign, DOWN*1.5)

                self.play(FadeIn(b1), FadeIn(b2), run_time=1)
                self.play(Write(b), run_time=1)
                self.play(FadeOut(b), FadeOut(b1), FadeOut(b2), run_time=1)

                if l[j]<l[i]:
                    arr=CurvedDoubleArrow(tab2.get_rows()[0][i].get_center(), tab2.get_rows()[0][j].get_center(), color=PURPLE_B).shift(DOWN*0.7).scale(0.7)
                    swap=Text("Swap", color=PURPLE_B).scale(0.5).next_to(arr, DOWN*0.5)

                    l[j], l[i]=l[i], l[j]
                    tab3=MathTable([l], include_outer_lines=True).scale(0.7).next_to(tab1, DOWN*4)
                    tab3.get_rows()[0][:i].set_color(GREY_B)

                    self.play(FadeOut(sign), run_time=1)
                    self.play(Create(arr), FadeIn(swap), run_time=1)
                    self.play(FadeOut(arr), FadeOut(swap),ReplacementTransform(tab2, tab3), FadeIn(sign), run_time=1.5)
                    tab2=tab3

                j+=1
                if j<len(l):
                    self.play(sq2.animate.next_to(tab2.get_rows()[0][j], UP*2), run_time=1)
                else:
                    self.play(FadeOut(sq2), run_time=1)

            self.play(FadeOut(it), run_time=1)

        tab2.get_rows()[0].set_color(GOLD_B)

        self.play(FadeOut(sign), FadeOut(s2), FadeOut(sq1), run_time=1)
        self.wait(3)
        self.clear()
        tan=Text("LinkedIn: tanishakaur\nGithub: TranquilTanisha", color=GREY_B).scale(0.3).to_corner(DR)
        self.add(tan)
        t=Text("Thank you!", color=BLUE).scale(1.2)
        self.play(Write(t), run_time=1)
        self.play(Circumscribe(t), run_time=1)
        self.wait(2) 

