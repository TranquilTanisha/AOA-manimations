from manim import *

n=8
x=[-1]*n #To store the final solution
y=[] #To store in string
q=[["X",1,2,3,4,5,6,7,8]] #2 D table
# solution=[["Q1", "Q2", "Q3", "Q4", "Q5", "Q6", "Q7", "Q8"]]

for i in range(n):
    q.append(["."]*(n+1))
    y.append("Q"+str(i+1))

for i in range(n):
    q[i+1][0]=i+1

class Eight_queens(Scene):
    tab=MathTable(q, include_outer_lines=True).scale(0.4).move_to(DOWN*0.65)
    tab.get_rows()[0].set_color(YELLOW)
    tab.get_columns()[0].set_color(YELLOW)

    def construct(self):
        tan=Text("LinkedIn: tanisha-kaur\nGithub: TranquilTanisha", color=GREY_B).scale(0.3).to_corner(DR)
        self.add(tan)

        s=Title(f"8-Queens Problem", color=TEAL_B).scale(1.2)
        self.play(Write(s), run_time=2)
        self.wait(1)

        txt=Text("Queens must not be placed:", color=BLUE).scale(0.6).move_to(UP*1.5)
        t1=BulletedList("In the same column", "In the same Row", "In diagonal cells", buff=0.7).scale(0.6).next_to(txt, DOWN)
        self.play(Write(txt), run_time=2)
        self.play(Write(t1), run_time=1.5)
        self.wait(2)
        self.play(FadeOut(txt), FadeOut(t1), run_time=1)

        self.play(Create(self.tab), run_time=2)
        text=Text("Solution: ", color=BLUE).scale(0.5).move_to(LEFT*5.5)
        self.play(FadeIn(text), run_time=1)

        self.nqueen(0)

        self.wait(3)
        self.clear()
        tan=Text("LinkedIn: tanisha-kaur\nGithub: TranquilTanisha", color=GREY_B).scale(0.3).to_corner(DR)
        self.add(tan)
        t=Text("Thank you!", color=BLUE).scale(1.2)
        self.play(Write(t), run_time=1)
        self.play(Circumscribe(t), run_time=1)
        self.wait(2) 

    def nqueen(self, k):
        for i in range(n):
            if self.place(k,i):
                x[k]=i
                if k==n-1:
                    l=0
                    m=0
                    for l in range(n):
                        q[l+1][x[m]+1]=y[m]
                        m+=1

                    tab1=MathTable(q, include_outer_lines=True).scale(0.4).move_to(DOWN*0.65)
                    tab1.get_rows()[0].set_color(YELLOW)
                    tab1.get_columns()[0].set_color(YELLOW)
                    self.play(ReplacementTransform(self.tab,tab1), run_time=2)
                    self.tab=tab1

                    self.play(Circumscribe(self.tab, color=YELLOW, shape=Rectangle, fade_out=True))
                    self.wait(1)

                    l=0
                    m=0
                    for l in range(n):
                        q[l+1][x[m]+1]="."
                        m+=1
                        
                else:
                    self.nqueen(k+1)
    
    def place(self,k,i):
        for j in range(k):
            if x[j]==i or abs(x[j]-i)==abs(j-k): #Same column or diagonal
                return False            
        return True