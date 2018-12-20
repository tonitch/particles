from tkinter import *
import random


class App(Frame):
    def __init__(self, master):
        super().__init__(master)
        self.main()
        self.mainloop()

    def main(self):
        self.Wscreen = 1920 # self.master.winfo_screenwidth()
        self.Hscreen = 1080 # self.master.winfo_screenheight()
        self.master.title("Particules")

        canvas = Canvas(self.master, width=self.Wscreen, height=self.Hscreen)
        canvas.pack()

        self.setup(canvas)

    def setup(self, canvas):
        self.master.update()
        canvas.Wscreen = self.Wscreen
        canvas.Hscreen = self.Hscreen
        self.nbrPart = 500

        canvas.particles = []

        canvas.particles.append(Particle(canvas))

        self.update(canvas)

    def update(self, canvas):
        self.master.update()
        canvas.delete(ALL)

        for part in canvas.particles:
            part.update()

        if len(canvas.particles) < self.nbrPart:
            canvas.particles.append(Particle(canvas))

        self.after(10, lambda: self.update(canvas))


class Particle():
    def __init__(self, canvas):
        self.canvas = canvas
        self.size = 5
        self.screenFace = random.randint(0, 3)
        if self.screenFace == 0:  # top
            self.x = random.randint(0, self.canvas.winfo_width())
            self.y = self.canvas.winfo_height() + random.randint(10,100)
            self.xspeed = random.uniform(-1,1)
            self.yspeed = -random.uniform(0.5,2)
        elif self.screenFace == 1:  # right
            self.x = self.canvas.winfo_width() + random.randint(10,100)
            self.y = random.randint(0, self.canvas.winfo_height())
            self.xspeed = -random.uniform(0.5,2)
            self.yspeed = random.uniform(-1,1)
        elif self.screenFace == 2:  # bottom
            self.x = random.randint(0, self.canvas.winfo_width())
            self.y = -random.randint(10,100)
            self.xspeed = random.uniform(-1,1)
            self.yspeed = random.uniform(0.5,2)
        elif self.screenFace == 3:  # left
            self.x = -random.randint(10,100)
            self.y = random.randint(0, self.canvas.winfo_height())
            self.xspeed = random.uniform(0.5,2)
            self.yspeed = random.uniform(-1,1)

    def update(self):
        self.canvas.create_oval(self.x-self.size,
                                self.y-self.size,
                                self.x+self.size,
                                self.y+self.size,
                                fill="green")

        self.x = self.x + self.xspeed
        self.y = self.y + self.yspeed


        if self.screenFace == 0:  # top
            if self.y < 0:
                self.canvas.particles.remove(self)
        elif self.screenFace == 1:  # right
            if self.x < 0:
                self.canvas.particles.remove(self)
        elif self.screenFace == 2:  # bottom
            if self.y > self.canvas.Hscreen:
                self.canvas.particles.remove(self)
        elif self.screenFace == 3:  # left
            if self.x > self.canvas.Wscreen:
                self.canvas.particles.remove(self)


if __name__ == "__main__":
    root = Tk()
    App(root)
