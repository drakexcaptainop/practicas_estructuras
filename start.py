import manimlib as ml

class TestScene(ml.Scene):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
    
    def construct(self) -> None:
        text = ml.Text( 'Hello!' )
        self.play(ml.Write(text))
        
        text.move_to( ( ml.np.array([0, 5, -10]) ) )
        self.play()
        return 