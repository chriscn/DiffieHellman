from manim import *

class MixingColours(Scene):
    def construct(self):
        alice = Text("Alice").shift(LEFT * 3).shift(UP * 2)
        bob = Text("Bob").shift(RIGHT * 3).shift(UP * 2)

        alice_square = Square(color=YELLOW).shift(LEFT * 3).set_fill(opacity=0.5)
        bob_square = Square(color=YELLOW).shift(RIGHT * 3).set_fill(opacity=0.5)

        common_starting_colour = Text("Alice and Bob both publicly agree to use the same shared colour yellow.", size=0.5).shift(DOWN* 2)

        self.play(Create(alice, runtime=4), Create(bob, runtime=4))
        self.play(Create(alice_square, runtime=10), Create(bob_square, runtime=10), Create(common_starting_colour, runtime=10))
        self.wait(3)
        
        secret_colours = Text("Alice and Bob now pick random secret colours that they don't tell one another.", size=0.5).shift(DOWN * 2)
        alice_secret = Square(color=RED).shift(LEFT * 5.5).set_fill(opacity=0.25)
        bob_secret = Square(color=TEAL).shift(RIGHT * 5.5).set_fill(opacity=0.25)

        self.play(Uncreate(common_starting_colour))
        self.play(Create(secret_colours), Create(alice_secret), Create(bob_secret))
        self.wait(5)
        
        mix_colours = Text("They now mix their secret colour with the inital shared colour.", size=0.5).shift(DOWN *2)

        alice_secret_copy = alice_secret.copy()
        bob_secret_copy = bob_secret.copy()

        self.play(Uncreate(secret_colours))
        self.play(Create(mix_colours), ApplyMethod(alice_secret_copy.shift, RIGHT * 2.5), ApplyMethod(bob_secret_copy.shift, LEFT * 2.5))
        self.play(Uncreate(alice_secret_copy), Uncreate(alice_square), Uncreate(bob_secret_copy), Uncreate(bob_square))

        alice_secret_mixed = Square(color=ORANGE).shift(LEFT * 3).set_fill(opacity=0.5)
        bob_secret_mixed = Square(color=BLUE).shift(RIGHT * 3).set_fill(opacity=0.5)
        mixed_colours = Text("Alice and Bob now have their mixed colours, which they'll now swap to each other.", size=0.5).shift(DOWN * 2)
        expensive = Text("One assumes that mixture seperation is impossible.", size=0.5).shift(DOWN * 2.5)


        self.play(Uncreate(mix_colours))        
        self.play(Create(mixed_colours), Create(expensive), Create(alice_secret_mixed), Create(bob_secret_mixed))
        self.wait(5)

        swapped = Text("They've now swapped their mixed colours.", size = 0.5).shift(DOWN * 2)
        self.play(Uncreate(mixed_colours), Uncreate(expensive), ApplyMethod(alice_secret_mixed.shift, RIGHT * 6), ApplyMethod(bob_secret_mixed.shift, LEFT * 6))
        self.play(Create(swapped))
        self.wait(2)

        original_colours = Text("They'll now reapply their orignal secret colour.", size=0.5).shift(DOWN * 2)
        self.play(Uncreate(swapped))
        self.play(Create(original_colours), ApplyMethod(alice_secret.shift, RIGHT * 2.5), ApplyMethod(bob_secret.shift, LEFT * 2.5))
        self.wait(2)

        shared_secret = Text("By reappling their originally individual secret colours they've arrived at a common secret.", size=0.5).shift(DOWN * 2)
        alice_shared = Square(color=LIGHT_BROWN).set_fill(opacity=1).shift(LEFT * 3)
        bob_shared = Square(color=LIGHT_BROWN).set_fill(opacity=1).shift(RIGHT * 3)

        self.play(Uncreate(original_colours), Uncreate(alice_secret), Uncreate(bob_secret), Uncreate(alice_secret_mixed), Uncreate(bob_secret_mixed))
        self.play(Create(shared_secret), Create(alice_shared), Create(bob_shared))
        self.wait(5)

class Maths(Scene):
    def construct(self):
        text = Text("Hello, World")
        self.play(Create(text))