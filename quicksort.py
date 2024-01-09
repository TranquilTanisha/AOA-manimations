from manim import *

pivot=[]
a=[int(x) for x in input("Enter the list of numbers: ").split()]
n=len(a)

def check(l,p):
    if l<=p:
        b=Tex("True", color=BLUE).scale(0.7)
    else:
        b=Tex("False", color=BLUE).scale(0.7)
    return b

class QuickSort(Scene):
    s=Title(f"Quick Sort", color=TEAL_B).scale(1.2)
    tab1=MathTable([a], include_outer_lines=True).scale(0.7).next_to(s, DOWN*3)
    tab2=MathTable([a], include_outer_lines=True).scale(0.7).next_to(tab1, DOWN*4)
    def construct(self):
        tan=Text("LinkedIn: tanishakaur\nGithub: TranquilTanisha", color=GREY_B).scale(0.3).to_corner(DR)
        self.add(tan)

        self.play(Write(self.s), run_time=2)
        self.wait(1)

        # s1=Text("Initial array: ", color=BLUE).scale(0.7)
        # gr=VGroup(s1, tab1).next_to(s, DOWN*4)
        t="Partition at\nindex: "

        # self.play(Create(gr), run_time=3)
        self.play(Create(self.tab1), run_time=2)
        self.wait(1)

        # sign=Text("<", color=BLUE).scale(0.7).next_to(ORIGIN, DOWN*10+RIGHT*3)
        sign=Text("<", color=BLUE).scale(0.7).next_to(self.tab2, DOWN*6.5)

        sq1=Text("p", color=PURPLE_B).scale(0.5)
        sq2=Text("i", color=GREEN).scale(0.5)
        sq3=Text("j", color=ORANGE).scale(0.5)
        sq4=Text("l", color=GREY_B).scale(0.5).next_to(self.tab2.get_rows()[0][0], UP*2)
        sq5=Text("h", color=GREY_B).scale(0.5).next_to(self.tab2.get_rows()[0][n-1], UP*2)

        self.play(Create(self.tab2), run_time=2)
        self.play(FadeIn(sign), FadeIn(sq4), FadeIn(sq5), run_time=1)

        self.quicksort(a, 0, n-1, sq1, sq2, sq3, sq4, sq5, sign, t)

        self.play(FadeOut(sign), FadeOut(sq4), FadeOut(sq5), run_time=1)
        # self.wait(1)
        # s2=Text("After Sorting:", color=BLUE).scale(0.7).next_to(s1, DOWN*5)
        # self.play(Write(s2), run_time=1)
        self.tab2.get_rows()[0].set_color(GOLD_B)
        self.wait(3)
        self.clear()
        tan=Text("LinkedIn: tanishakaur\nGithub: TranquilTanisha", color=GREY_B).scale(0.3).to_corner(DR)
        self.add(tan)
        t=Text("Thank you!", color=BLUE).scale(1.2)
        self.play(Write(t), run_time=1)
        self.play(Circumscribe(t), run_time=1)
        self.wait(2) 

    def quicksort(self, a,l,h, sq1, sq2, sq3, sq4, sq5, sign, t):
        if l<h:
            self.play(sq4.animate.next_to(self.tab2.get_rows()[0][l], UP*2), sq5.animate.next_to(self.tab2.get_rows()[0][h], UP*2), run_time=1)
            p=self.partition(a,l,h, sq1, sq2, sq3, sign, t)  
            self.quicksort(a,l,p-1, sq1, sq2, sq3, sq4, sq5, sign, t)            
            self.quicksort(a,p+1,h, sq1, sq2, sq3, sq4, sq5, sign, t)   

    def partition(self, a,l,h, sq1, sq2, sq3, sign, t):
        p=a[h]
        t1=Tex(a[h]).scale(0.7).next_to(sign, RIGHT)
        i=l-1

        sq1.next_to(self.tab2.get_rows()[0][h], DOWN*2)
        if i==-1:
            sq2.next_to(self.tab2.get_rows()[0][0], DOWN*4+LEFT*4)
        else:
            sq2.next_to(self.tab2.get_rows()[0][i], DOWN*4)

        sq3.next_to(self.tab2.get_rows()[0][l], DOWN*2)

        self.play(FadeIn(sq1), FadeIn(sq2), FadeIn(sq3), run_time=1)
        # cell1=tab2.get_rows()[0][h].get_center() #to store the center of h
        self.play(Circumscribe(self.tab2.get_rows()[0][h], color=PURPLE_B, buff=0.15, fade_out=True, time_width=2, run_time=2))
        self.play(FadeIn(t1), run_time=0.7)
        # self.play(tab2.get_rows()[0][h].animate.next_to(sign,RIGHT), run_time=1)

        for j in range(l,h):
            if j!=l:
                self.play(sq3.animate.next_to(self.tab2.get_rows()[0][j], DOWN*2), run_time=1)

            cell2=self.tab2.get_rows()[0][j].get_center()
            b=check(a[j], p)
            b.next_to(sign, DOWN)

            self.play(self.tab2.get_rows()[0][j].animate.next_to(sign,LEFT), run_time=1)
            self.play(Write(b), run_time=1)
            self.play(FadeOut(b), run_time=1)
            self.play(self.tab2.get_rows()[0][j].animate.move_to(cell2), run_time=1)

            if a[j]<=p:
                i+=1
                self.play(sq2.animate.next_to(self.tab2.get_rows()[0][i], DOWN*4), run_time=1)

                if i!=j:
                    arr=CurvedDoubleArrow(self.tab2.get_rows()[0][i].get_center()+LEFT*0.5, self.tab2.get_rows()[0][j].get_center()+RIGHT*0.5, color=PURPLE_B).shift(DOWN*0.6).scale(0.7)
                    swap=Text("Swap", color=PURPLE_B).scale(0.5).next_to(arr, DOWN*0.5)

                    self.play(FadeOut(sq2), FadeOut(sq3), FadeOut(sq1), run_time=1)
                    self.play(Create(arr), FadeIn(swap), run_time=1)

                    a[i], a[j]=a[j], a[i]
                    tab3=MathTable([a], include_outer_lines=True).scale(0.7).next_to(self.tab1, DOWN*4)
                    # if len(pivot)!=0:
                    #     for a in pivot:
                    #         tab3.get_rows()[0][a].set_color(GOLD_B)
                    self.play(ReplacementTransform(self.tab2, tab3), run_time=1)
                    self.tab2=tab3
                    self.play(FadeOut(arr), FadeOut(swap), FadeIn(sq1), FadeIn(sq2), FadeIn(sq3), run_time=2)
                    # self.play(FadeOut(tab3))  
        
        # self.play(tab2.get_rows()[0][h].animate.move_to(cell1), run_time=1)
        self.play(FadeOut(t1), run_time=1)

        if i+1!=h:
            self.play(sq2.animate.next_to(self.tab2.get_rows()[0][i+1], DOWN*4), run_time=1)
            arr=CurvedDoubleArrow(self.tab2.get_rows()[0][i+1].get_center()+LEFT*0.5, self.tab2.get_rows()[0][h].get_center()+RIGHT*0.5, color=PURPLE_B).shift(DOWN*0.7).scale(0.7)
            swap=Text("Swap", color=PURPLE_B).scale(0.5).next_to(arr, DOWN*0.5)

            self.play(FadeOut(sq1), FadeOut(sq2), FadeOut(sq3), FadeOut(sign), run_time=1)
            self.play(Create(arr), FadeIn(swap), run_time=1)
            self.play(FadeOut(arr), FadeOut(swap), FadeIn(sign), run_time=2)

        i+=1
        a[i], a[h]=a[h], a[i]
        tab4=MathTable([a], include_outer_lines=True).scale(0.7).next_to(self.tab1, DOWN*4)
        # if len(pivot)!=0:
        #     for a in pivot:
        #         tab4.get_rows()[0][a].set_color(GOLD_B)
        self.play(ReplacementTransform(self.tab2, tab4), run_time=1)
        self.tab2=tab4
        # self.play(FadeOut(tab3))
        
        s3=Text(t+str(i), t2c={t: BLUE}).scale(0.5).next_to(self.tab1, DOWN*5).next_to(self.tab2, LEFT*4)

        # if i!=h:
        #     self.play(FadeOut(sq1))
        # else:
        #     self.play(FadeOut(sq1), FadeOut(sq2), FadeOut(sq3), run_time=1)

        self.play(FadeIn(s3), Circumscribe(self.tab2.get_rows()[0][i], color=GOLD, buff=0.15, fade_out=True, run_time=2))
        self.play(FadeOut(s3), run_time=1)
        self.tab2.get_rows()[0][i].set_color(GOLD_B)           

        return i

