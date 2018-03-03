from tkinter import * # import all defintions from tkinter
import NearestPoints # import nearest points module

radius = 2

class NearestPointsGUI:    
    def __init__(self):
        self.points = [] # initialize list to store points
        window = Tk()
        window.title("Find Nearest Point")

        # create canvas
        self.canvas = Canvas(window, width = 400, height = 200)
        self.canvas.pack()

        # bind left mouse click to addPoint
        self.canvas.bind("<Button-1>", self.addPoint)

        self.shortestDist = StringVar()
        # create label to display distance of closest points
        Label(window, textvariable = self.shortestDist).pack()

        window.mainloop() # create event loop

    def addPoint(self, event):
        if not self.isTooCloseToOtherPoints(event.x, event.y):
            self.addThisPoint(event.x, event.y)

    def addThisPoint(self, x, y):
        # display this point
        self.canvas.create_oval(x - radius, y - radius, x + radius,
            y + radius)
        # add this point to self.points list
        self.points.append([x, y])
        if len(self.points) > 2:
            p1, p2 = NearestPoints.nearestPoints(self.points)
            self.canvas.delete("line")
            self.canvas.create_line(self.points[p1][0],
                self.points[p1][1], self.points[p2][0], self.points[p2][1],
                tags = "line")
            self.shortestDist.set(NearestPoints.distance(self.points[p1][0],
                self.points[p1][1], self.points[p2][0], self.points[p2][1]))

    def isTooCloseToOtherPoints(self, x, y):
        for i in range(len(self.points)):
            if NearestPoints.distance(x, y, self.points[i][0],
                    self.points[i][1]) <= 2 * radius:
                return True
        return False

NearestPointsGUI() # create GUI
