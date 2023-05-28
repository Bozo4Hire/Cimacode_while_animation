from manim import *
import numpy as np

# Nord Theme Palettes
polarNight0 = '#2e3440' 
polarNight1 = '#3b4252'
polarNight2 = '#434c5e'
polarNight3 = '#4c566a'
snowStorm0 = '#d8dee9'
snowStorm1 = '#e5e9f0'
snowStorm2 = '#eceff4'
frost0 = '#5e81ac'
frost1 = '#81a1c1'
frost2 = '#88c0d0'
frost3 = '#8fbcbb'
auroraRed = '#bf616a'
auroraOrange = '#d08770'
auroraYellow = '#ebcb8b'
auroraGreen = '#a3be8c'
auroraMagenta = '#b48ead'

class AWhile(Scene):
    def construct(self):
        # Support grid allocation
        """ for x in range(-7, 8):
            for y in range(-4, 5):
                self.add(Dot(np.array([x, y, 0]), color=DARK_GREY)) """

        self.camera.background_color = polarNight0

        t1 = Tex(r"\textbf{Ciclo \textit{While}}", color = snowStorm2, font_size=100) 
        
        w1 = Text(
            "While <Condición> :",
            t2c={'[:6]': auroraMagenta, '[6:17]': frost0, '[17:18]': snowStorm2},
            font_size = 60
        ).to_edge(LEFT, buff = 2)
        w2 = Text("<Bloque>", font_size = 60, color = frost3).to_edge(LEFT, buff = 3)

        i1 = Text(
            "If <Condición> :",
            t2c={'[:3]': auroraMagenta, '[3:14]': frost0, '[14:15]': snowStorm2},
            font_size = 60
        ).to_edge(LEFT, buff = 2).shift(DOWN * 1)
        i2 = Text("<Bloque>", font_size = 60, color = frost3).to_edge(LEFT, buff = 3).shift(DOWN * 2.1)

        # Init arrows for spinning wheel
        spin_x = 5
        spin_y = 0.5
        d = 0.75
        spin_rt = 3
        arrow1 = CurvedArrow(
            start_point=np.array([spin_x-d,spin_y-d,0]), 
            end_point=np.array([spin_x-d,spin_y+d,0]), 
            color = snowStorm1).flip(UP)
        arrow2 = CurvedArrow(
            start_point=np.array([spin_x+d,spin_y+d,0]), 
            end_point=np.array([spin_x+d,spin_y-d,0]), 
            color = snowStorm1).flip(UP)
        
        hlighter1 = Rectangle(
             fill_color = YELLOW, 
             width = 2.2, height = 1.1, 
             fill_opacity = 0.25, 
             stroke_opacity = 0).next_to(w1, RIGHT).shift(LEFT * 8).shift(UP * 1.1)
        
        hlighter2 = Rectangle(
             fill_color = YELLOW, 
             width = 5, height = 1.1, 
             fill_opacity = 0.25, 
             stroke_opacity = 0).next_to(w1, RIGHT).shift(LEFT * 5.6).shift(UP * 1.1)

        hlighter3 = Rectangle(
             fill_color = YELLOW, 
             width = 3.6, height = 1.1, 
             fill_opacity = 0.25, 
             stroke_opacity = 0).next_to(w2, RIGHT).shift(LEFT * 3.75)
        
        # Intro
        self.play(Write(t1), run_time=2)
        self.wait(7)
        self.play(t1.animate.scale(0.8).to_edge(UL, buff = 0.2), run_time = 1) # 9s

        # Write While statement
        self.play(AddTextLetterByLetter(w1))
        self.play(w1.animate.shift(UP * 1.1))
        self.play(AddTextLetterByLetter(w2)) # 14s
        self.wait(0.5)
        self.play(Create(VGroup(arrow1, arrow2)), run_time = 1)
        self.wait(0.5)
        self.play(
            Rotate(arrow1, angle=-6*PI, about_point = np.array([spin_x,spin_y,0]), rate_func = linear), 
            Rotate(arrow2, angle=-6*PI, about_point = np.array([spin_x,spin_y,0]), rate_func = linear), run_time = 3)
        self.wait()
        self.play(FadeOut(VGroup(arrow1, arrow2)))
        self.wait() # 22s

        self.play(FadeIn(hlighter1)) 
        self.wait(3)
        self.play(FadeOut(hlighter1))
        
        self.play(FadeIn(hlighter2))
        self.wait(2.5)
        self.play(FadeOut(hlighter2))
 
        self.play(FadeIn(hlighter3))
        self.wait(4.5)
        self.play(FadeOut(hlighter3))
        self.wait() # 38.5s


        # Write If statement 
        self.play(VGroup(w1, w2).animate.shift(UP * 1.1))
        self.play(AddTextLetterByLetter(i1))
        self.play(AddTextLetterByLetter(i2)) # 42s
        self.wait(8.3) 

        txt = Text("Verdadero ✓", font_size = 50, color = GREEN, weight=BOLD).next_to(i1, RIGHT).shift(RIGHT * 1)
        self.play(FadeIn(txt))
        self.wait(2.5)

        a1 = always_redraw( lambda: Arrow(start=np.array([-4.8,-1.5,0]), end=np.array([-4.2,-2,0]), color = GREEN, stroke_width = 10, buff = 0))
        self.play(Create(a1))
        self.wait() # 55.5 s
        self.play(FadeOut(a1, txt))
        self.wait(1)

        txt = Text("Falso ✕", font_size = 50, color = auroraRed, weight=BOLD).next_to(i1, RIGHT).shift(RIGHT * 1.5)
        self.play(FadeIn(txt))
        self.wait(1.5)

        a2 = always_redraw( lambda: Arrow(start=np.array([-4.8,-1.5,0]), end=np.array([-4.8,-3,0]), color = auroraRed, stroke_width = 5, buff = 0, ))
        self.play(Create(a2))
        self.wait()
        self.play(FadeOut(a2, txt)) # 1 min 3s 
        self.wait(3.5) 
          
        # Counting reps for If statement
        txt1 = Text("0, 1 veces", font_size = 50, color = snowStorm1).next_to(i1, RIGHT).shift(RIGHT * 1.5 )
        self.play(AddTextLetterByLetter(txt1), Create(VGroup(a1,a2))) # 1 min 7.5 s
        self.wait(10.5)

        # Describing While statement
        a3 = always_redraw( lambda: Arrow(start=np.array([-4.8,1.7,0]), end=np.array([-4.2,1.15,0]), color = GREEN, stroke_width = 10, buff = 0) )
        a4 = always_redraw( lambda: CurvedArrow(start_point=np.array([-5.5,1.1,0]), end_point=np.array([-5.5,2.3,0]), color = GREEN, stroke_width = 5).flip(UP) )
        tr = Text("Verdadero ✓", font_size = 45, color = GREEN, weight=BOLD).next_to(w1, RIGHT).shift(RIGHT * 0.1)
        self.play(FadeIn(tr))
        self.wait()
        self.play(Create(a3))
        self.wait(8)
        self.play(Create(a4), FadeOut(tr))
        self.wait(9)
   
        
        # Counting reps for While statement
        k = ValueTracker(0)
        num = always_redraw( lambda: Integer(font_size = 50, color = snowStorm1).set_value(k.get_value()).next_to(w1, RIGHT).shift(RIGHT * 0.3) )
        txt2 = Text("veces", font_size = 50, color = snowStorm1).next_to(w1, RIGHT).shift(RIGHT * 1.025)
        n = Text("n", font_size = 50, color = snowStorm1).next_to(w1, RIGHT).shift(RIGHT * 0.4)
        self.play(AddTextLetterByLetter(num))
        self.wait(0.05)
        self.play(AddTextLetterByLetter(txt2))
        self.wait() 
        self.play(k.animate.set_value(99), run_time = 2, rate_func = rush_into)
        self.remove(num)
        self.play(AddTextWordByWord(n))
        self.wait() 

        # While break
        self.play(FadeOut(VGroup(a3, a4)), VGroup(n, txt2).animate.shift(DOWN * 1.1))
        a5 = Arrow (start=np.array([-4.8,1.8,0]), end=np.array([-4.8,0.3,0]), color = auroraRed, stroke_width = 5, buff = 0)
        fa = Text("Falso ✕", font_size = 45, color = auroraRed, weight=BOLD).next_to(w1, RIGHT).shift(RIGHT * 0.3)
        self.play(FadeIn(fa))
        self.wait()
        self.play(Create(a5))
        self.wait()
        
        # Fade Out Intro
        self.play(*[FadeOut(mob)for mob in self.mobjects])
        self.wait()

            
class Example1(Scene):
    def construct(self):
        # Support grid allocation
        """ for x in range(-7, 8):
            for y in range(-4, 5):
                self.add(Dot(np.array([x, y, 0]), color=DARK_GREY)) """
    
        self.camera.background_color = polarNight0

        t1 = Tex("Algunos ", "Ejemplos", color = snowStorm2, font_size=100) 
        self.play(FadeIn(t1))
        self.wait()
        self.play(Uncreate(t1[0]), t1[1].animate.to_edge(UP).shift(LEFT* 1.9).scale(0.75))
        self.wait()

        code1 = Code(
            "./e1.py",
            tab_width=6,
            font_size=35,
            background_stroke_width=5,
            background_stroke_color= polarNight2 ,
            insert_line_no=True,
            style=Code.styles_list[14],
            language="py",
        ).to_edge(LEFT, buff = 1)

        term1 = consTerminal().to_edge(RIGHT, buff = 1)
        hlighter = Rectangle(
             fill_color = YELLOW, 
             width = 4.8, height = 0.5, 
             fill_opacity = 0.25, 
             stroke_opacity = 0).next_to(code1, UP).shift(DOWN * 0.95)
        # code1 linespace = 0.5

        
        itxt = Tex("i = ", font_size = 50, color = snowStorm2).next_to(code1, DOWN).shift(DOWN * 0.5)
        k = ValueTracker(0)
        num = always_redraw(lambda: Integer(color = snowStorm2).set_value(k.get_value()).next_to(itxt, RIGHT))
        checkM = always_redraw( 
             lambda : Text("✓", font_size = 40, color = GREEN, weight=BOLD).shift(LEFT * 0.5).shift(UP * 0.3) 
        )
        redL = Line(np.array([-2.95, -2.35, 0]), np.array([-2.65, -2.35, 0]), color = auroraRed, stroke_width = 5)

        self.play(DrawBorderThenFill(code1), run_time = 0.5)
        self.play(DrawBorderThenFill(term1), run_time = 0.5)
        self.wait()
        self.play(FadeIn(hlighter))
        
        # Explanation
        self.play(FadeIn(VGroup(num, itxt)))
        self.wait()
        self.play(hlighter.animate.shift(DOWN * 0.5))
        self.wait(13)
        self.play(Create(checkM))
        self.wait(1)
        self.play(Uncreate(checkM), hlighter.animate.shift(DOWN * 0.5 ))
        self.wait(3)
        self.play(Write(redL))
        self.wait(1)
        self.add(Text("0", font = "Courier new", font_size = 25, color = WHITE).shift(RIGHT * 1.75).shift(UP * 2.1))
        self.play(FadeOut(redL))
        self.wait()
        self.play(hlighter.animate.shift(DOWN * 0.5))
        self.wait()
        self.play(k.animate.set_value(1), run_time = 1, rate_func = smooth)
        self.wait()
        self.play(hlighter.animate.shift(UP * 1))

        # Rep until we reach i = 10
        i  = 1
        y = 2.1
        for i in range (1, 10):
            y -= 0.45
            self.play(FadeIn(checkM), run_time = 0.5)
            self.play(FadeOut(checkM), hlighter.animate.shift(DOWN * 0.5 ), run_time = 0.5)
            self.add(Text(str(i), font = "Courier new", font_size = 25, color = WHITE).shift(RIGHT * 1.75).shift(UP * y))
            self.wait(0.5)
            self.play(hlighter.animate.shift(DOWN * 0.5 ), run_time = 0.5)
            self.play(k.animate.set_value(i+1), run_time = 0.5)
            self.play(hlighter.animate.shift(UP * 1), run_time = 0.5)
        self.wait()

        # Condition no longer satisfied 
        self.play(Write(Line(np.array([-2.95, -2.35, 0]), np.array([-2.50, -2.35, 0]), color = auroraRed, stroke_width = 5)))
        self.wait(5)
        self.play(Create(Text("✕", font_size = 40, color = auroraRed, weight=BOLD).shift(LEFT * 0.5).shift(UP * 0.3)))
        self.wait(2)
        self.play(hlighter.animate.shift(DOWN * 1.5), run_time = 0.5)
        self.play(FadeOut(hlighter))
        self.wait()

        # Fade into next Example
        self.play(*[FadeOut(mob)for mob in self.mobjects])
        self.wait()

class Example2(Scene):
    def construct(self):
        # Support grid allocation
        """ for x in range(-7, 8):
            for y in range(-4, 5):
                self.add(Dot(np.array([x, y, 0]), color=DARK_GREY)) """
        self.camera.background_color = polarNight0

        code2 = Code(
            "./e2.py",
            tab_width=6,
            font_size=24,
            background_stroke_width=5,
            background_stroke_color= polarNight2 ,
            insert_line_no=True,
            style=Code.styles_list[14],
            language="py",
        ).to_edge(LEFT, buff = 1)

        term2 = consTerminal().to_edge(RIGHT, buff = 1)

        hlighter = Rectangle(
             fill_color = YELLOW, 
             width = 5.2, height = 0.3, 
             fill_opacity = 0.25, 
             stroke_opacity = 0).next_to(code2, UP).shift(DOWN * (2.425))
        hlighter_big = Rectangle(
             fill_color = YELLOW, 
             width = 5.2, height = 0.315*5, 
             fill_opacity = 0.25, 
             stroke_opacity = 0).next_to(code2, UP).shift(DOWN * (1.26+0.85))
        
        itxt = Tex("i = ", font_size = 50, color = snowStorm2).next_to(code2, DOWN).shift(DOWN * 0.3)
        k = ValueTracker(0)
        num = always_redraw(lambda: Integer(color = snowStorm2).set_value(k.get_value()).next_to(itxt, RIGHT))
        
        linePace = 0.315
        self.play(DrawBorderThenFill(code2), run_time = 0.5)
        self.play(DrawBorderThenFill(term2), run_time = 0.5)
        self.wait(8)
        self.play(FadeIn(hlighter_big))
        self.wait()
        self.play(FadeOut(hlighter_big))
        self.wait()
        self.play(FadeIn(hlighter), FadeIn(VGroup(num, itxt)))
        self.wait(6)
        self.play(hlighter.animate.shift(DOWN * linePace), run_time = 0.5)

        i = 0; y = 3
        arreglo = ["perro", "gato","gallina"]

        for i in range (0, 3):
            y -= 1
            self.wait(0.5)
            self.play(hlighter.animate.shift(DOWN * linePace), run_time = 0.5)
            self.add(Text(arreglo[i], font = "Courier new", font_size = 25, color = WHITE).shift(RIGHT * 2.5).shift(UP * y))
            self.wait(0.5)
            self.play(hlighter.animate.shift(DOWN * linePace ), run_time = 0.5)
            self.play(k.animate.set_value(i+1), run_time = 0.5)
            self.wait(0.5)
            self.play(hlighter.animate.shift(UP * (linePace*2)), run_time = 0.5)
        self.wait(3)
        self.play(hlighter.animate.shift(DOWN * (linePace*3)), run_time = 0.5)
        self.play(FadeOut(hlighter))
        self.wait()

        self.wait(8)

        self.play(*[FadeOut(mob)for mob in self.mobjects])
        self.wait()
        


def consTerminal():
        term = RoundedRectangle(
            stroke_width=5, 
            corner_radius= 0.3,
            width = 5,
            height = 5,
            fill_color = BLACK, 
            fill_opacity = 0.9, 
            stroke_color = polarNight2
        )
        return term