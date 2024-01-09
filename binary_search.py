from manim import *
import math

l=[int(x) for x in input("Enter the elements: ").split()]
key=int(input("Enter the key: "))
pos=-1

class Binary_search(Scene):
    tab=MathTable([l], include_outer_lines=True).scale(0.7).move_to(UP*1)
    sq1=Text("l", color=PURPLE_B).scale(0.5).next_to(tab.get_rows()[0][0], UP*2)
    sq2=Text("h", color=PURPLE_B).scale(0.5).next_to(tab.get_rows()[0][len(l)-1], UP*2)
    sq3=Text("m", color=PURPLE_B).scale(0.5).next_to(tab.get_rows()[0][math.ceil((len(l)-1)/2)], DOWN*2)

    def construct(self):
        tan=Text("LinkedIn: tanishakaur\nGithub: TranquilTanisha", color=GREY_B).scale(0.3).to_corner(DR)
        self.add(tan)

        s=Title(f"Binary Search", color=TEAL_B).scale(1.2)
        self.play(Write(s), run_time=2)
        self.wait(1)

        t1=Text("Key = "+str(key), t2c={"Key = ": BLUE}).scale(0.65).next_to(self.tab,UP*2+LEFT)

        self.play(FadeIn(self.tab), run_time=1)
        self.play(Write(t1), run_time=1)
        self.wait(1)

        t=Text("Sorting in ascending order").scale(0.65).move_to(DOWN)
        l.sort()
        tab1=MathTable([l], include_outer_lines=True).scale(0.7).move_to(UP*1)
        self.play(Write(t), run_time=1)
        self.wait(1)
        self.play(FadeOut(t), run_time=0.7)
        self.wait(0.5)
        self.play(ReplacementTransform(self.tab, tab1), run_time=2)
        self.tab=tab1
        self.play(FadeIn(self.sq1), FadeIn(self.sq2), FadeIn(self.sq3), run_time=1)

        pos=self.binary_search(0, len(l)-1)

        if pos==-1:
            self.play(FadeOut(self.sq1), FadeOut(self.sq2), FadeOut(self.sq3), run_time=0.7)
            t2=Text("Element not found", color=BLUE).scale(0.5).move_to(DOWN)
            self.play(Write(t2), run_time=1)

        self.wait(3)
        self.clear()
        tan=Text("LinkedIn: tanishakaur\nGithub: TranquilTanisha", color=GREY_B).scale(0.3).to_corner(DR)
        self.add(tan)
        t=Text("Thank you!", color=BLUE).scale(1.2)
        self.play(Write(t), run_time=1)
        self.play(Circumscribe(t), run_time=1)
        self.wait(2) 

    def binary_search(self, beg, end):
        if(beg<=end):
            mid=math.ceil((beg+end)/2)
            if mid!=math.ceil((len(l)-1)/2):
                self.play(FadeOut(self.sq3), run_time=0.8)

            if beg!=end:
                self.play(LaggedStart(self.sq1.animate.next_to(self.tab.get_rows()[0][beg], UP*2), self.sq2.animate.next_to(self.tab.get_rows()[0][end], UP*2), lag_ratio=0.4), run_time=1.5)
            else:
                self.play(LaggedStart(self.sq1.animate.next_to(self.tab.get_rows()[0][beg], UP*2+LEFT*0.5), self.sq2.animate.next_to(self.tab.get_rows()[0][end], UP*2+RIGHT*0.5), lag_ratio=0.4), run_time=1.5)

            if mid!=math.ceil((len(l)-1)/2):
                self.sq3.next_to(self.tab.get_rows()[0][mid], DOWN*2)
                self.play(FadeIn(self.sq3), run_time=0.7)
           
            self.play(Circumscribe(self.tab.get_rows()[0][mid], fade_out=True, time_width=1.7), run_time=1)

            t3=Text(str(key)+" = "+str(l[mid]), t2c={str(key):BLUE, " = ": YELLOW}).scale(0.6).move_to(DOWN)
            if key==l[mid]:
                t4=Text("True", color=BLUE).scale(0.6).next_to(t3, DOWN)
            else:
                t4=Text("False", color=BLUE).scale(0.6).next_to(t3, DOWN)

            self.play(Write(t3), run_time=1)
            self.play(Write(t4), run_time=1)
            self.wait(1)
            self.play(FadeOut(t3), FadeOut(t4), run_time=1)

            if key==l[mid]:
                self.play(FadeOut(self.sq1), FadeOut(self.sq2), FadeOut(self.sq3), run_time=0.7)
                sq=Square(side_length=0.5, color=YELLOW).move_to(self.tab.get_rows()[0][mid])
                t5=Text("Element found at index "+str(mid), t2c={str(mid): BLUE}).scale(0.6).move_to(DOWN)
                self.play(FadeIn(sq), run_time=1)
                self.play(Write(t5), run_time=1)
                return mid
                    
            elif key<l[mid]:
                t3=Text(str(key)+" < "+str(l[mid]), t2c={str(key):BLUE, " < ":YELLOW}).scale(0.6).move_to(DOWN)
                t4=Text("True", color=BLUE).scale(0.6).next_to(t3, DOWN)
                self.play(Write(t3), run_time=1)
                self.play(Write(t4), run_time=1)
                self.wait(1)
                self.tab.get_rows()[0][mid:].set_color(GREY_B)
                self.play(FadeOut(t3), FadeOut(t4), run_time=1)
                end=mid-1      

            elif key>l[mid]:
                t3=Text(str(key)+" > "+str(l[mid]), t2c={str(key):BLUE," > ":YELLOW}).scale(0.6).move_to(DOWN)
                t4=Text("True", color=BLUE).scale(0.6).next_to(t3, DOWN)
                self.play(Write(t3), run_time=1)
                self.play(Write(t4), run_time=1)
                self.wait(1)
                self.tab.get_rows()[0][:mid+1].set_color(GREY_B)
                self.play(FadeOut(t3), FadeOut(t4), run_time=1)
                beg=mid+1

            else:
                return -1

            self.binary_search(beg,end)