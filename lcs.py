from manim import *

# tab- for c n k
# tab1- for replacement

def check(a,b):
    if a==b:
        return "True"
    else:
        return "False"

class Lcs(Scene):
    def construct(self):
        tan=Text("LinkedIn: tanishakaur\nGithub: TranquilTanisha", color=GREY_B).scale(0.3).to_corner(DR)
        self.add(tan)

        s=Title(f"Longest Common Subsequence (LCS)", color=TEAL_B).scale(1.2)
        self.play(Write(s), run_time=2)
        self.wait(1)

        a=input("Enter the first string: ")
        b=input("Enter the second string: ")
        m=len(a)
        n=len(b)

        t1=Text("String 1: "+a+"\tString 2: "+b, color=BLUE).scale(0.5).next_to(s, DOWN*3)
        self.play(FadeIn(t1), run_time=1)
        # case=Text("Case 1:\nx= "+a+"\ny= "+b, color=BLUE).scale(0.5).next_to(t1, DOWN*1.5).to_edge(LEFT)
        # self.play(FadeIn(case), run_time=1)

        controls=Text("Controls:\n* = move diagonal\n! = move up\n< = move left", color=ORANGE).scale(0.4).next_to(s, DOWN*3).to_edge(RIGHT)
        self.play(Write(controls), run_time=2)
        self.wait(1)

        self.lcs(a,b,m,n,s)
        # self.play(FadeOut(case), run_time=1)

        # a,b=b,a
        # m,n=n,m

        # case=Text("Case 2:\nx= "+a+"\ny= "+b, color=BLUE).scale(0.5).next_to(t1, DOWN*1.5).to_edge(LEFT)
        # self.play(FadeIn(case), run_time=1)

        # self.lcs(a,b,m,n,s)
        # self.play(FadeOut(case), run_time=1)
        self.clear()
        tan=Text("LinkedIn: tanishakaur\nGithub: TranquilTanisha", color=GREY_B).scale(0.3).to_corner(DR)
        self.add(tan)
        t=Text("Thank you!", color=BLUE).scale(1.2)
        self.play(Write(t), run_time=1)
        self.play(Circumscribe(t), run_time=1)
        self.wait(2) 

    def lcs(self, a,b,m,n, s):
        c=[] #To store the value
        k=[] #To store the direction of the path
        for i in range(m+1):
            c.append([0]*(n+1))
            k.append(["."]*(n+1))

        cc=self.create_tab(a,b,m,n,c,k)

        tab=MathTable(cc, include_outer_lines= True).scale(0.5).next_to(s, DOWN*6)
        tab.get_rows()[1].set_color(GREY_C)
        tab.get_columns()[1].set_color(GREY_C)
        self.play(FadeIn(tab),run_time=2)
        # self.wait(1)

        sq=Square(side_length=0.8, color=ORANGE).scale(0.5).move_to(tab.get_rows()[2][2])
        self.play(Create(sq), run_time=1)
        # self.wait(1)

        for i in range(1, m+1):
            for j in range(1,n+1):
                self.play(sq.animate.move_to(tab.get_rows()[i+1][j+1]), run_time=1)

                bool=check(a[i-1], b[j-1])
                t=Text("Is "+a[i-1]+"="+b[j-1]+","+"\n"+bool, color=BLUE, t2c={bool: WHITE}).scale(0.5).next_to(tab, RIGHT*3)

                self.play(Circumscribe(tab.get_rows()[i+1][0], color=PURPLE_A, shape=Rectangle, fade_out=True), Circumscribe(tab.get_rows()[0][j+1], color=PURPLE_A, shape=Rectangle, fade_out=True), run_time=2)
                self.play(Write(t), run_time=2)
                self.wait(1)
                self.play(FadeOut(t), run_time=1)

                if a[i-1]==b[j-1]:
                    c[i][j]=c[i-1][j-1]+1
                    k[i][j]="*" #To move diagonally

                    self.play(Circumscribe(tab.get_rows()[i][j], color=PURPLE_A, shape=Rectangle, fade_out=True), run_time=2)

                else:
                    ma=Text("max{ ", color=BLUE).scale(0.5).next_to(tab, RIGHT*3)
                    n1=Tex(c[i-1][j]).next_to(ma, RIGHT).scale(0.5)
                    n2=Tex(c[i][j-1]).next_to(n1, RIGHT).scale(0.5)

                    self.play(FadeIn(ma), run_time=1)
                    self.play(Circumscribe(tab.get_rows()[i+1][j], color=PURPLE_A, shape=Rectangle, fade_out=True), Circumscribe(tab.get_rows()[i][j+1], color=PURPLE_A, shape=Rectangle, fade_out=True), run_time=2)
                    self.play(FadeIn(n1), FadeIn(n2), run_time=1)

                    if c[i-1][j]>=c[i][j-1]:
                        temp=Text("!").scale(0.5).next_to(n1, DOWN*0.5)

                        self.play(Indicate(n1), run_time=2)
                        self.play(FadeOut(temp), run_time=1)

                        c[i][j]=c[i-1][j]
                        k[i][j]="!" #To move up
                    else:
                        temp=Text("<").scale(0.5).next_to(n2, DOWN*0.5)

                        self.play(Indicate(n2), run_time=2)
                        self.play(FadeIn(temp), run_time=1)
                        self.play(FadeOut(temp), run_time=1)

                        c[i][j]=c[i][j-1]
                        k[i][j]="<" #To move down  

                    self.play(FadeOut(ma), FadeOut(n1), FadeOut(n2), run_time=1)
                
                cc=self.modify(m,n,c,k,cc)
                tab1=MathTable(cc, include_outer_lines=True).scale(0.5).next_to(s, DOWN*6)
                tab1.get_rows()[1].set_color(GREY_C)
                tab1.get_columns()[1].set_color(GREY_C)
                self.play(ReplacementTransform(tab, tab1), run_time=1)
                tab=tab1
                # self.wait(1)
        
        self.play(FadeOut(sq), run_time=1)
        self.print_lcs(a,k, m, n, sq, tab)
        # self.wait(3)

    def create_tab(self, a,b,m,n,c,k):
        cc=[]

        for i in range(m+2):
            cc.append([0]*(n+2))

        for i in range(m+2):
            for j in range(n+2):
                if i==0 and j==0:
                    cc[i][j]="X"

                elif i==0:
                    if j==1:
                        cc[i][j]=0

                    elif j>1:
                        cc[i][j]=b[j-2]

                elif j==0:
                    if i==1:
                        cc[i][j]=0

                    elif i>1:
                        cc[i][j]=a[i-2]

                elif i==1 or j==1:
                    cc[i][j]=0

                else:
                    cc[i][j]=str(c[i-1][j-1])+k[i-1][j-1]

        return cc
    
    def modify(self,m,n,c,k,cc):
        for i in range(2,m+2):
            for j in range(2,n+2):
                cc[i][j]=str(c[i-1][j-1])+k[i-1][j-1]

        return cc

    def print_lcs(self, a, k, m, n, sq, tab):        
        i=m
        j=n
        lcs=""
        t2=Text("LCS: ", color=BLUE).scale(0.5).next_to(tab, RIGHT*3)
        t3=Text(lcs).scale(0.5).next_to(t2, RIGHT*0.5)
        # self.play(FadeIn(t2), run_time=1)

        sq.move_to(tab.get_rows()[i+1][j+1])
        self.play(FadeIn(sq), FadeIn(t2), FadeIn(t3), run_time=1)
        # self.wait(1)

        while i>0 and j>0:

            if k[i][j]=="*":
                lcs=a[i-1]+lcs
                i-=1
                j-=1

                self.play(Circumscribe(tab.get_rows()[i+2][0], color=PURPLE_A, shape=Rectangle, fade_out=True), run_time=2)
                t4=Text(lcs).scale(0.5).next_to(t2, RIGHT*0.5)
                self.play(ReplacementTransform(t3,t4), run_time=1)
                t3=t4
                tab.get_rows()[i+2][0].set_color(YELLOW)
                # self.wait(1)

            elif k[i][j]=="!":
                i-=1
            else:
                j-=1
            self.play(sq.animate.move_to(tab.get_rows()[i+1][j+1]))
        self.wait(2)
        self.play(FadeOut(tab), FadeOut(sq), FadeOut(t2), FadeOut(t3), run_time=1)
