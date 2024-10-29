from manim import *

class TestScene(Scene):
    def construct(self):
        text = Text("¡Manim está funcionando!")
        self.play(Write(text))
        self.wait(2)