# Hope Trygstad

# This module contains the methods and information about my Button class.
# I used this module for my Yahtzee lab and my Palindrome lab so far.

# importing graphics
from graphics import *

# making the class itself
class Button:

    """Buttons are rectangles that are labeled with a centered text, drawn in
a window. It can do: activate(), deactivate(), clicked(p), and getLabel().
If it's clicked, the button is active and p is in it."""

    # constructor with parameters
    def __init__(self, win, center, width, height, label):
        """creates a button in the shape of a rectangle with parameters
        of the window, center(in form of a point), width, height, and
        label(in form of a string)."""

        # creating all variables out of parameters so we can use them later
        
        # dividing width and height by two so I can use the center and half
        # the width or height to actually draw the button
        w, h = width/2.0, height/2.0
        x, y = center.getX(), center.getY()
        self.xmax, self.xmin = x+w, x-w
        self.ymax, self.ymin = y+h, y-h
        # making the corner points of the rectangle
        p1 = Point(self.xmin, self.ymin)
        p2 = Point(self.xmax, self.ymax)
        # drawing the rectangle for the button
        self.rect = Rectangle(p1, p2)
        self.rect.setFill("lightgray")
        self.rect.draw(win)
        # making the label for the button
        self.label = Text(center, label)
        self.label.draw(win)
        self.deactivate()

    def clicked(self, p):
        """Returns true if the button is active/available AND p, the point they
        clicked, is inside. Parameter is just p."""
        # making sure it only is true if all three are true, p falls within
        # the button's x and y values
        return (self.active and
                self.xmin <= p.getX() <= self.xmax and
                self.ymin <= p.getY() <= self.ymax)

    def getLabel(self):
        "returns the label string of that particular button. No parameters."
        # just getting the text inside the button
        return self.label.getText()

    def activate(self):
        "makes the button available. No parameters."
        # changing the way the button looks to make it clearly active
        self.label.setFill("black")
        self.rect.setWidth(2)
        # what being active actually means(setting it to true)
        self.active = True

    def deactivate(self):
        "makes the button unavailable. No parameters."
        # changing the way the button looks to make it clearly inactive
        self.label.setFill("darkgray")
        self.rect.setWidth(1)
        # what being inactive actually means(setting active to false)
        self.active = False

    def setLabel(self, win, newText):
        self.label.setText(newText)
        self.label.draw(win)

    def undraw(self):
        self.undraw()
    
