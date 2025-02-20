from manim import *

class AreaUnderCurve(Scene):
    def construct(self):
        # Define the axes
        axes = Axes(
            x_range=[0, 10, 1],
            y_range=[0, 10, 1],
            axis_config={"color": WHITE},
        )

        # Define the function
        def func(x):
            return 0.1 * x**2

        # Create the graph of the function
        graph = axes.plot(func, color=BLUE)

        # Create the area under the curve
        area = axes.get_area(graph, x_range=[2, 8], color=BLUE, opacity=0.5)

        # Create labels
        labels = axes.get_axis_labels(x_label="x", y_label="F(x)")

        # Create vertical lines at the integration limits
        line_a = axes.get_vertical_line(axes.c2p(2, func(2)), color=WHITE)
        line_b = axes.get_vertical_line(axes.c2p(8, func(8)), color=WHITE)
        dot_a = Dot(axes.c2p(2, func(2)), color=WHITE)
        dot_b = Dot(axes.c2p(8, func(8)), color=WHITE)

        # Add everything to the scene
        self.add(axes, labels)
        impulse_text = MathTex(r"\vec{J}", r"=", r"\int_a^b", r"\vec{F}(x)", r"\ dx", color=WHITE).shift(2*LEFT).scale(1.3)
        self.play(Write(impulse_text))
        self.play(Create(graph))
        self.play(Indicate(graph, scale_factor=1.2, color=YELLOW), Indicate(impulse_text[3], scale_factor=1.5, color=YELLOW))
        self.play(Create(line_a), Create(line_b), Create(dot_a), Create(dot_b))
        self.play(Indicate(dot_a, scale_factor=1.2, color=YELLOW), 
                  Indicate(dot_b, scale_factor=1.2, color=YELLOW),
                  Indicate(impulse_text[2], scale_factor=1.5, color=YELLOW),
                  Indicate(impulse_text[4], scale_factor=1.5, color=YELLOW),
                  Indicate(line_a, scale_factor=1.2, color=YELLOW),
                  Indicate(line_b, scale_factor=1.2, color=YELLOW))
        self.wait(1)

        self.play(FadeIn(area))
        self.wait(1)

        # Pulse the area
        
        # Add the text "Impulse (J)" centered on the area
        self.play(Indicate(area, scale_factor=1.2, color=YELLOW), Indicate(impulse_text[0], scale_factor=1.5, color=YELLOW))
        self.wait(2)
        self.play(FadeOut(area), FadeOut(impulse_text), FadeOut(graph), FadeOut(line_a), FadeOut(line_b), FadeOut(dot_a), FadeOut(dot_b))
        self.wait(1)