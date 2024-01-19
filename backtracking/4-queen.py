from manim import *

# n=int(input("Enter the number of queens: "))
n=4
x=[-1]*n #To store the final solution
y=[] #To store in string
q=[["X",1,2,3,4]] #2 D table
solution=[["Q1", "Q2", "Q3", "Q4"]]

for i in range(n):
    q.append(["."]*(n+1))
    y.append("Q_"+str(i+1))

for i in range(n):
    q[i+1][0]=i+1

class Four_queens(Scene):
    tab=MathTable(q, include_outer_lines=True).scale(0.6)
    tab.get_rows()[0].set_color(YELLOW)
    tab.get_columns()[0].set_color(YELLOW)

    def construct(self):
        tan=Text("LinkedIn: tanishakaur\nGithub: TranquilTanisha", color=GREY_B).scale(0.3).to_corner(DR)
        self.add(tan)

        s=Title(f"4-Queens Problem", color=TEAL_B).scale(1.2)
        self.play(Write(s), run_time=2)
        self.wait(1)

        txt=Text("Queens must not be placed:", color=BLUE).scale(0.6).move_to(UP*1.5)
        t1=BulletedList("In the same column", "In the same Row", "In diagonal cells", buff=0.7).scale(0.6).next_to(txt, DOWN)
        self.play(Write(txt), run_time=2)
        self.play(Write(t1), run_time=2)
        self.wait(1)
        self.play(FadeOut(txt), FadeOut(t1), run_time=0.7)

        self.play(Create(self.tab), run_time=2)

        self.nqueen(0)

        self.play(FadeOut(self.tab), run_time=1)

        for i in range(1,len(solution)):
            for j in range(n):
                solution[i][j]+=1

        t=Text("Solution: ", slant=ITALIC).scale(0.6).next_to(s, DOWN*3)
        table=MathTable(solution, include_outer_lines=True).scale(0.6).next_to(t, DOWN*1.5)
        table.get_rows()[0].set_color(YELLOW)

        self.play(Write(t), run_time=1)
        self.play(Create(table), run_time=2)
        self.wait(3)
        self.clear()
        tan=Text("LinkedIn: tanishakaur\nGithub: TranquilTanisha", color=GREY_B).scale(0.3).to_corner(DR)
        self.add(tan)
        t=Text("Thank you!", color=BLUE).scale(1.2)
        self.play(Write(t), run_time=1)
        self.play(Circumscribe(t), run_time=1)
        self.wait(2) 

    def nqueen(self, k):
        for i in range(n):
            q[k+1][i+1]=y[k]
            tab1=MathTable(q, include_outer_lines=True).scale(0.6)
            tab1.get_rows()[0].set_color(YELLOW)
            tab1.get_columns()[0].set_color(YELLOW)
            self.play(ReplacementTransform(self.tab,tab1), run_time=1)
            self.tab=tab1

            if self.place(k,i):
                x[k]=i
                if k==n-1:
                    solution.append(x.copy())
                    text=Text("Possible Solution: ", color=BLUE).scale(0.5).next_to(self.tab, LEFT*2)
                    self.play(Circumscribe(self.tab, color=YELLOW, shape=Rectangle, fade_out=True))
                    self.play(FadeIn(text), run_time=1)
                    self.wait(1)
                    self.play(FadeOut(text), run_time=1)

                else:
                    self.nqueen(k+1)
                    q[k+1][i+1]="."
                    tab1=MathTable(q, include_outer_lines=True).scale(0.6)
                    tab1.get_rows()[0].set_color(YELLOW)
                    tab1.get_columns()[0].set_color(YELLOW)
                    self.play(ReplacementTransform(self.tab,tab1), run_time=1)
                    self.tab=tab1
            
            else:
                cross=Cross().scale(0.2).move_to(self.tab.get_rows()[k+1][i+1])
                self.play(FadeIn(cross), run_time=0.7)
                self.play(FadeOut(cross))

            q[k+1][i+1]="."
            tab1=MathTable(q, include_outer_lines=True).scale(0.6)
            tab1.get_rows()[0].set_color(YELLOW)
            tab1.get_columns()[0].set_color(YELLOW)
            self.play(ReplacementTransform(self.tab,tab1), run_time=1)
            self.tab=tab1

    
    def place(self,k,i):
        for j in range(k):
            if x[j]==i or abs(x[j]-i)==abs(j-k): #Same column or diagonal
                return False            
        return True