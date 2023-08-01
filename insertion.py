from manim import *

def check(key, l ,j):
    if l[j]>key:
        b=Text("True", color=BLUE).scale(0.7)
    else:
        b=Text("False", color=BLUE).scale(0.7)
    return b

class InsertionSort(Scene):
    def construct(self):
        tan=Text("LinkedIn: tanisha-kaur\nGithub: TranquilTanisha", color=GREY_B).scale(0.3).to_corner(DR)
        self.add(tan)

        s=Title(f"Insertion Sort", color=TEAL_B).scale(1.2)
        self.play(Write(s), run_time=2)
        self.wait(1)

        l=[int(x) for x in input("Enter the list of numbers: ").split()]
        tab1=MathTable([l], include_outer_lines=True).scale(0.7).next_to(s, DOWN*4)
        self.play(Create(tab1), run_time=2)

        tab2=MathTable([l], include_outer_lines=True).scale(0.7).next_to(tab1, DOWN*4)
        s2=Text("Iteration", color=BLUE).scale(0.7).next_to(tab2, LEFT*4)
        sign=Text("<", color=BLUE).scale(0.7).next_to(tab2, DOWN*6.7)
        kk=Text("Key=", color=BLUE).scale(0.7).next_to(sign, LEFT*7)

        self.play(FadeIn(s2), run_time=1)   
        self.play(Create(tab2), run_time=2)
        self.play(FadeIn(sign), run_time=1)
        self.play(Write(kk), run_time=1)

        sq1=Text("i", color=GREEN).scale(0.5)
        sq2=Text("j", color=ORANGE).scale(0.5)

        for i in range(1, len(l)):
            j=i-1
            key=l[i]

            it=Text(str(i)).scale(0.7).next_to(s2, RIGHT)
            k=Tex(key).scale(0.8).next_to(kk, RIGHT*0.5)

            sq1.next_to(tab2.get_rows()[0][i], UP*2)
            sq2.next_to(tab2.get_rows()[0][j], UP*2)

            self.play(FadeIn(it), run_time=1)
            self.play(FadeIn(sq1), run_time=1)
            self.play(FadeIn(sq2), run_time=1)
            self.play(Circumscribe(tab2.get_rows()[0][i], color=PURPLE_B, buff=0.15, fade_out=True, time_width=1))
            self.play(FadeIn(k), run_time=1)

            b1=Tex(key).scale(0.8).next_to(sign, LEFT)
            b2=Tex(l[j]).scale(0.8).next_to(sign, RIGHT)
            b=check(key, l, j)
            b.next_to(sign, DOWN*1.5).scale(0.7)

            self.play(FadeIn(b1), FadeIn(b2), run_time=1)
            self.play(Write(b), run_time=1)
            self.play(FadeOut(b), FadeOut(b2), run_time=1)

            while j>=0 and l[j]>key:
                l[j+1]=l[j]

                arr=CurvedArrow(start_point=tab2.get_rows()[0][j].get_center(), end_point=tab2.get_rows()[0][j+1].get_center(), color=PURPLE_B,).shift(DOWN*0.7)
                shift=Text("Shift", color=PURPLE_B).scale(0.7).next_to(arr, DOWN*0.5).scale(0.65)

                self.play(Create(arr), FadeIn(shift), run_time=1)

                tab3=MathTable([l], include_outer_lines=True).scale(0.7).next_to(tab1, DOWN*4)
                self.play(FadeOut(arr), FadeOut(shift), ReplacementTransform(tab2, tab3), run_time=1)
                tab2=tab3
                j-=1
                if j!=-1 and j!=len(l)-1:
                    self.play(sq2.animate.next_to(tab3.get_rows()[0][j], UP*2), run_time=1)

                    b2=Tex(l[j]).scale(0.7).next_to(sign, RIGHT)
                    b=check(key, l, j)
                    b.next_to(sign, DOWN).scale(0.7)

                    self.play(FadeIn(b2), run_time=1)
                    self.play(Write(b), run_time=1)

                    self.play(FadeOut(b), FadeOut(b2), run_time=1)

                else:
                    self.play(FadeOut(sq2), run_time=1)
                self.wait(1)

            l[j+1]=key
            tab3=MathTable([l], include_outer_lines=True).scale(0.7).next_to(tab1, DOWN*4)
            self.play(FadeOut(b1), k.animate.move_to(tab3.get_rows()[0][j+1].get_center()), ReplacementTransform(tab2, tab3), run_time=1)
            tab2=tab3
            if j!=-1 and j!=len(l)-1:
                self.play(FadeOut(sq2), run_time=1)
            self.play(FadeOut(it), FadeOut(sq1), FadeOut(k), run_time=1)   
        
        tab2.get_rows()[0].set_color(GOLD_B)
        self.play(FadeOut(sign), FadeOut(s2), FadeOut(kk), run_time=1)     
        self.wait(3)
        self.clear()
        tan=Text("LinkedIn: tanisha-kaur\nGithub: TranquilTanisha", color=GREY_B).scale(0.3).to_corner(DR)
        self.add(tan)
        t=Text("Thank you!", color=BLUE).scale(1.2)
        self.play(Write(t), run_time=1)
        self.play(Circumscribe(t), run_time=1)
        self.wait(2) 
