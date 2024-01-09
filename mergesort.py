from manim import *
import math

a=[int(x) for x in input("Enter the list of numbers: ").split()]
n=len(a)

class Mergesort(Scene):
    tab=MathTable([a], include_outer_lines=True).scale(0.7)

    def construct(self):
        tan=Text("LinkedIn: tanishakaur\nGithub: TranquilTanisha", color=GREY_B).scale(0.3).to_corner(DR)
        self.add(tan)

        s=Title(f"Merge Sort", color=TEAL_B).scale(1.2)
        self.play(Write(s), run_time=2)
        self.wait(1)

        self.tab.next_to(s, DOWN*4)
        tab1=MathTable([a], include_outer_lines=True).scale(0.7).next_to(s, DOWN*4)

        self.play(Create(tab1), run_time=2)
        # self.wait(1)

        sq1=Text("m", color=PURPLE_B).scale(0.5)
        sq2=Text("l", color=PURPLE_B).scale(0.5).next_to(tab1.get_rows()[0][0], UP*2)
        sq3=Text("h", color=PURPLE_B).scale(0.5).next_to(tab1.get_rows()[0][n-1], UP*2)
        self.play(FadeIn(sq2), FadeIn(sq3), run_time=1)

        self.mergesort(a, 0, n-1, sq1, sq2, sq3, tab1, s)

        self.wait(3)
        self.clear()
        tan=Text("LinkedIn: tanishakaur\nGithub: TranquilTanisha", color=GREY_B).scale(0.3).to_corner(DR)
        self.add(tan)
        t=Text("Thank you!", color=BLUE).scale(1.2)
        self.play(Write(t), run_time=1)
        self.play(Circumscribe(t), run_time=1)
        self.wait(2) 
    
    def mergesort(self, a, l, h, sq1, sq2, sq3, tab1,s):
        if l<h:
            mid=math.floor((l+h)/2)

            sq1.next_to(tab1.get_rows()[0][mid], DOWN*2)
            self.play(LaggedStart(sq2.animate.next_to(tab1.get_rows()[0][l], UP*2), sq3.animate.next_to(tab1.get_rows()[0][h], UP*2), lag_ratio=0.25), run_time=1)            
            self.play(FadeIn(sq1), Circumscribe(tab1.get_rows()[0][mid], color=PURPLE_B, buff=0.15, fade_out=True), run_time=1.5)
            self.play(FadeOut(sq1), run_time=1)

            self.mergesort(a,l, mid, sq1, sq2, sq3, tab1,s)

            self.play(LaggedStart(sq2.animate.next_to(tab1.get_rows()[0][l], UP*2), sq3.animate.next_to(tab1.get_rows()[0][h], UP*2)), run_time=1)

            self.mergesort(a, mid+1, h, sq1, sq2, sq3, tab1, s)
            self.merge(a, l, mid,h, sq2, sq3, tab1,s)

    def merge(self, a,l, mid,h, sq2, sq3, tab1, s):
        if l!=0 or h!=len(a)-1:
            tab2=MathTable([a[l:h+1]], include_outer_lines=True).scale(0.7).next_to(tab1, DOWN*4)
            self.play(FadeIn(tab2), run_time=1)
        else:
            tab2=tab1
            self.play(LaggedStart(sq2.animate.next_to(tab1.get_rows()[0][l], UP*2), sq3.animate.next_to(tab1.get_rows()[0][h], UP*2)), run_time=1)

        n1=mid-l+1
        n2=h-mid
        L=[]
        R=[]
        for i in range(n1):
            L.append(a[l+i])
        for i in range(n2):
            R.append(a[mid+1+i])

        tab3=MathTable([L], include_outer_lines=True).scale(0.7).next_to(tab2, DOWN*4)
        tab4=MathTable([R], include_outer_lines=True).scale(0.7).next_to(tab3, RIGHT*4)
        gr=VGroup(tab3, tab4).next_to(tab2, DOWN*5)
        # if l!=0 and h!=len(a)-1:
        ar1=Arrow(tab2.get_rows()[0].get_center()+DOWN*0.4, tab3.get_rows()[0].get_center()+UP*0.4, buff=0.1, color=BLUE)
        ar2=Arrow(tab2.get_rows()[0].get_center()+DOWN*0.4, tab4.get_rows()[0].get_center()+UP*0.4, buff=0.1, color=BLUE)
        self.play(Create(ar1), Create(ar2), run_time=1)
        self.play(FadeIn(gr), run_time=1)
        
        t=Text("Sort &\nMerge", color=BLUE).scale(0.7).next_to(gr, LEFT*5)
        self.play(FadeIn(t), FadeOut(ar1), FadeOut(ar2), run_time=1)
        
        #merge the array
        k=l
        i=0
        j=0
        while i<n1 and j<n2:
            if L[i]<=R[j]:
                a[k]=L[i]
                i+=1
            else:
                a[k]=R[j]
                j+=1
            k+=1
        
        while i<n1:
            a[k]=L[i]
            i+=1
            k+=1
        while(j<n2):
            a[k]=R[j]
            j+=1
            k+=1

        tab5=MathTable([a[l:h+1]], include_outer_lines=True).scale(0.7).next_to(tab2, DOWN*4)
        self.play(ReplacementTransform(gr, tab5), run_time=1)
        # self.wait(1)
        self.play(FadeOut(t), run_time=1)
        gr=tab5

        if l!=0 or h!=len(a)-1:
            tab5=MathTable([a[l:h+1]], include_outer_lines=True).scale(0.7).next_to(tab1, DOWN*4)
            self.play(ReplacementTransform(tab2,tab5), gr.animate.next_to(tab1, DOWN*4), run_time=1)
            tab2=tab5
            # self.wait(0.5)

            tab5=MathTable([a], include_outer_lines=True).scale(0.7).next_to(s, DOWN*4)
            self.play(FadeOut(tab2))
            # self.play(gr.animate.move_to(tab1.get_rows()[0][l:h+1], DOWN*4), Transform(gr, tab5), Transform(tab1, tab5), FadeOut(tab2), run_time=1)
            self.play(gr.animate.move_to(tab1.get_rows()[0][l:h+1].get_center()), Transform(tab1, tab5), run_time=1.3)
            self.play(FadeOut(gr))
            tab1=tab5

        else:
            self.play(FadeOut(sq2), FadeOut(sq3), FadeOut(tab1), run_time=1)
            # self.play(ReplacementTransform(tab1,gr), run_time=1)
            self.play(FadeIn(self.tab), runtime=1)