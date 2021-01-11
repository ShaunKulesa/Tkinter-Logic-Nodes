import tkinter as tk     # python 3
# import Tkinter as tk   # python 2
from tkinter import * 
from PIL import ImageTk,Image  

class Example(tk.Frame):
    """Illustrate how to drag items on a Tkinter canvas"""

    def __init__(self, parent):
        tk.Frame.__init__(self, parent)

        # create a canvas
        self.canvas = tk.Canvas(width=1920, height=1080, background="#232323")
        self.canvas.pack(fill="both", expand=True)

        self._rects = {}

        # this data is used to keep track of an
        # item being dragged
        self._drag_data = {"x": 0, "y": 0, "item": None}

        # create a couple of movable objects
        self.create_token(100, 100, "grey")

        # add bindings for clicking, dragging and releasing over
        # any object with the "token" tag
        self.canvas.tag_bind("token", "<ButtonPress-1>", self.drag_start)
        self.canvas.tag_bind("token", "<ButtonRelease-1>", self.drag_stop)
        self.canvas.tag_bind("token", "<B1-Motion>", self.multi_drag)
        root.bind('f', self.run)
        self.canvas.bind("<1>", lambda event: root.focus_set())


    def _create_circle(self, x, y, r, **kwargs):
        return self.create_oval(x-r, y-r, x+r, y+r, **kwargs)
    tk.Canvas.create_circle = _create_circle

    def run(self, event=None):
        time_get = self.timer_entry.get()
        print(time_get)
        time.sleep(int(time_get))
        print("time over")

    def create_token(self, x, y, color):
        """Create a token at the given coordinate in the given color"""

        # for i in range(20):
        #     big = self.canvas.create_line(i*100, 0, 90, 1080*100, fill="black")
        # for i in range(20):
        #     big = self.canvas.create_line(1080*100, 0, 90, i*100, fill="black")

        
        timer_body = self.canvas.create_rectangle(0, 20, 150, 60, fill="#3f3f3f", outline = '#3f3f3f', tags = 'token')
        timer_head = self.canvas.create_rectangle(0, 0, 150, 20, fill="#9d353f", outline = '#9d353f', tags = 'token')
        timer_title = self.canvas.create_text(20,10,fill="white", text="Timer")
        timer_seconds_subtitle = self.canvas.create_text(30,50,fill="white", text="Seconds")
        self.timer_entry = tk.Entry(width=15, bg="#595959", bd=0, insertbackground="white", fg="white", text="1")
        timer_entry_canvas = self.canvas.create_window(100, 50, window=self.timer_entry)
        timer_input = self.canvas.create_circle(0, 50, 4, fill="#cc7f33", outline="#cc7f33")
        timer_output = self.canvas.create_circle(150, 30, 4, fill="#cc3333", outline="#cc3333")
        timer_ends_subheading = self.canvas.create_text(110,30,fill="white", text="Timer Ends")

        # self.canvas.tag_raise(clock)

        _tokens = [timer_title, timer_body, timer_head, timer_seconds_subtitle, timer_entry_canvas, timer_input, timer_output, timer_ends_subheading]

        for t in _tokens:
            self._rects[t] = [_ for _ in _tokens if _ is not t]
        
        print_body = self.canvas.create_rectangle(0, 20, 150, 60, fill="#3f3f3f", outline = '#3f3f3f', tags = 'token')
        print_head = self.canvas.create_rectangle(0, 0, 150, 20, fill="#9d353f", outline = '#9d353f', tags = 'token')
        print_title = self.canvas.create_text(20,10,fill="white", text="Print")
        print_seconds_subtitle = self.canvas.create_text(30,50,fill="white", text="String")
        self.print_entry = tk.Entry(width=15, bg="#595959", bd=0, insertbackground="white", fg="white", text="1")
        print_entry_canvas = self.canvas.create_window(100, 50, window=self.print_entry)
        print_input = self.canvas.create_circle(0, 50, 4, fill="#cc7f33", outline="#cc7f33")
        print_output = self.canvas.create_circle(150, 30, 4, fill="#cc3333", outline="#cc3333")
        print_ends_subheading = self.canvas.create_text(110,30,fill="white", text="Output")

        _tokens = [print_title, print_body, print_head, print_seconds_subtitle, print_entry_canvas, print_input, print_output, print_ends_subheading]

        for p in _tokens:
            self._rects[p] = [_ for _ in _tokens if _ is not p]        

        

    def drag_start(self, event):
        """Begining drag of an object"""
        # record the item and its location
        self._drag_data["item"] = self.canvas.find_closest(event.x, event.y)[0]
        self._drag_data["x"] = event.x
        self._drag_data["y"] = event.y

    def drag_stop(self, event):
        """End drag of an object"""
        # reset the drag information
        self._drag_data["item"] = None
        self._drag_data["x"] = 0
        self._drag_data["y"] = 0

    def drag(self, event):
        """Handle dragging of an object"""
        # compute how much the mouse has moved
        delta_x = event.x - self._drag_data["x"]
        delta_y = event.y - self._drag_data["y"]
        # move the object the appropriate amount
        self.canvas.move(self._drag_data["item"], delta_x, delta_y)
        # record the new position
        self._drag_data["x"] = event.x
        self._drag_data["y"] = event.y

    def multi_drag(self, event):
        """Handle dragging of an object"""
        # compute how much the mouse has moved
        delta_x = event.x - self._drag_data["x"]
        delta_y = event.y - self._drag_data["y"]
        item = self._drag_data["item"]
        # move the object the appropriate amount
        for t in [item] + self._rects[item]:
            self.canvas.move(t, delta_x, delta_y)

        # record the new position
        self._drag_data["x"] = event.x
        self._drag_data["y"] = event.y

        # record the new position
        self._drag_data["x"] = event.x
        self._drag_data["y"] = event.y

if __name__ == "__main__":
    root = tk.Tk()
    Example(root).pack(fill="both", expand=True)
    root.mainloop()
