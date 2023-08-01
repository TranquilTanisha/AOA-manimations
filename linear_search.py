from manim import *

# n=int(input("Enter the no of elements: "))
l=[int(x) for x in input("Enter the elements: ").split()]
key=int(input("Enter the element to search for: "))
n=len(l)
t=False

class Linear_search(Scene):
    def construct(self):
        tan=Text("LinkedIn: tanisha-kaur\nGithub: TranquilTanisha", color=GREY_B).scale(0.3).to_corner(DR)
        self.add(tan)

        s=Title(f"Linear Search", color=TEAL_B).scale(1.2)
        self.play(Write(s), run_time=2)
        self.wait(1)

        tab=MathTable([l], include_outer_lines=True).scale(0.8).move_to(UP*0.5)
        t1=Text("Key = "+str(key), t2c={"Key = ": BLUE}).scale(0.7).next_to(tab,UP*2+LEFT)
        t2=Text(str(key)+" = ", t2c={str(key): BLUE}).scale(0.6).next_to(tab, DOWN*3)
        pos=-1

        self.play(FadeIn(tab), run_time=1)
        self.play(Write(t1), run_time=1)
        self.wait(1)
        self.play(Write(t2), run_time=1)

        for i in range(n):
            cell=tab.get_rows()[0][i].get_center()
            self.play(tab.get_rows()[0][i].animate.next_to(t2, RIGHT*0.5), run_time=1)

            if l[i]==key:
                pos=i+1
                t3=Text("True", color=BLUE).scale(0.6).move_to(DOWN*1.5+RIGHT*0.2)
                self.play(Write(t3), run_time=1)
                self.play(FadeOut(t3), FadeOut(t2), tab.get_rows()[0][i].animate.move_to(cell), run_time=1)
                break

            else:
                t3=Text("False", color=BLUE).scale(0.6).move_to(DOWN*1.5+RIGHT*0.2)
                self.play(FadeIn(t3), run_time=1)
                self.play(FadeOut(t3), tab.get_rows()[0][i].animate.move_to(cell), run_time=1)

        if pos==-1:
            t3=Text("Key not found", color=BLUE).scale(0.6).move_to(t2.get_center())
        else:
            for i in range(n):
                t5=Tex(i, color=GREY_B).next_to(tab.get_rows()[0][i], DOWN*2).scale(0.6)
                self.play(FadeIn(t5))
            sq=Square(side_length=0.5, color=YELLOW).move_to(tab.get_rows()[0][pos-1])

            t6=Text("Element found at index "+str(pos-1), t2c={str(pos-1): BLUE}).scale(0.6).move_to(t2.get_center()+DOWN*0.5)
            self.play(Write(t6), FadeIn(sq), run_time=2)

        self.wait(3)
        self.clear()
        tan=Text("LinkedIn: tanisha-kaur \nGithub: TranquilTanisha", color=GREY_B).scale(0.3).to_corner(DR)
        self.add(tan)
        t=Text("Than you!", color=BLUE).scale(1.2)
        self.play(Write(t), run_time=1)
        self.play(Circumscribe(t), run_time=1)
        self.wait(2)   