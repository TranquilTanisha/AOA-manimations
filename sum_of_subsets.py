from manim import *

# n=int(input("Enter the number of items "))
# m=int(input("Enter the capacity of the bag "))
# w=[int(x) for x in input("Enter the weights of the items: ").split()]

n=6
m=30
w=[5,10,12,13,15,18]

x=[-1]*n #Solution vector
rem_sum=sum(w) #Remaining sum
sum=0 #Sum of the weights added

class Sum_of_Subsets(Scene):
    def construct(self):
        tan=Text("LinkedIn: tanisha-kaur\nGithub: TranquilTanisha", color=GREY_B).scale(0.3).to_corner(DR)
        self.add(tan)

        s=Title(f"Sum of Subsets", color=TEAL_B).scale(1.2)
        self.play(Write(s), run_time=2)
        self.wait(1)

        t1=Text("Capacity of the bag: "+str(m), t2c={"Capacity of the bag: ": BLUE}).scale(0.5).next_to(s,DOWN*2).to_edge(LEFT)
        t2=Text("Weights: ", t2c={"Weights: ": BLUE}).scale(0.5).next_to(t1,DOWN*3)
        weight= MathTable([w], include_outer_lines=1).scale(0.5).next_to(s, DOWN*5.5)
        t3=Text("Solution: ", color=BLUE).scale(0.5).next_to(t2,DOWN*3)

        self.play(Write(t1), run_time=1)
        self.play(Write(t2), run_time=1)
        self.play(FadeIn(weight), run_time=1)
        self.play(Write(t3), run_time=1)

        self.sum_of_subsets(0, sum, w, rem_sum)
        self.wait(2)
        self.clear()
        tan=Text("LinkedIn: tanisha-kaur\nGithub: TranquilTanisha", color=GREY_B).scale(0.3).to_corner(DR)
        self.add(tan)
        t=Text("Thank you!", color=BLUE).scale(1.2)
        self.play(Write(t), run_time=1)
        self.play(Circumscribe(t), run_time=1)
        self.wait(2)
        self.clear()
        tan=Text("LinkedIn: tanisha-kaur\nGithub: TranquilTanisha", color=GREY_B).scale(0.3).to_corner(DR)
        self.add(tan)
        t=Text("Thank you!", color=BLUE).scale(1.2)
        self.play(Write(t), run_time=1)
        self.play(Circumscribe(t), run_time=1)
        self.wait(2)  

    def sum_of_subsets(self, i, sum, w, rem_sum):
        if self.feasible(i):
            if sum==m:
                print("Feasible solution: ", x[:i])
                tab=MathTable([x[:i]], include_outer_lines=True).scale(0.5)

                t4=Text("Sum = ", color=BLUE).scale(0.5).move_to(DOWN+LEFT)
                t5=""
                for i in range(len(x)):
                    if x[i]==1:
                        t5+=str(w[i])+" +"
                t6=Text(t5[:len(t5)-1]).scale(0.5).next_to(t4, RIGHT)

                self.play(FadeIn(tab), run_time=1)
                self.play(Write(t4), Write(t6), run_time=1)
                t7=Tex(m).scale(0.6).next_to(t4, RIGHT)
                self.wait(2)
                self.play(ReplacementTransform(t6,t7), run_time=1)
                self.wait(2)
                self.play(FadeOut(tab), FadeOut(t4), FadeOut(t7), run_time=1)
        else:
            x[i]=1
            self.sum_of_subsets(i+1, sum+w[i], w, rem_sum-w[i])
            x[i]=0
            self.sum_of_subsets(i+1, sum, w, rem_sum-w[i])

    def feasible(self, i):
        if (sum+rem_sum>=m) and i<n and (sum==m or sum+w[i]<m):
            return False
        return True