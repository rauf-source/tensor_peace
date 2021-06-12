class RenderAnim:
    from pyvirtualdisplay import Display
    import matplotlib.pyplot as plt
    from matplotlib import animation, rc

    def __init__(self, env):
        #         initialize frame with empty list
        self.frame = []
        self.fig = self.plt.figure()

#     initializing display
        self.display = self.Display(visible=0, size=(1400, 900))
#         display.start()
#         self.plt.imshow(env.render('rgb_array'))
        self.plt.grid(False)
#    adding frame to compose animation

    def add_frame(self, frame):
        self.frame.append(frame)
#  animating

    def animate(self):
        self.display.start()
        an = self.animation.ArtistAnimation(
            self.fig, self.frame, interval=100, repeat_delay=1000, blit=True)
        self.rc('animation', html='jshtml')
        return an
