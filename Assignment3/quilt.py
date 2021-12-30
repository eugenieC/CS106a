import sys
import tkinter

def draw_bars(canvas, x, y, width, height, num_lines):
    """
    1.draw lightblue rectangle
    2.draw n lines
    """
    canvas.create_rectangle(x, y, x+width, y+height, outline='lightblue') 
    for i in range(0,num_lines):
        canvas.create_line(x+i*(width/(num_lines-1)),y,x+i*(width/(num_lines-1)),y+height,fill='black') 

def draw_eye(canvas, x, y, width, height, num_lines):
    """
    1.draw lightblue rectangle
    2.draw yellow oval
    3.draw n line from center
    """
    canvas.create_rectangle(x, y, x+width, y+height, outline='lightblue') 
    canvas.create_oval(x, y, x+width, y+height,outline='yellow', fill='yellow')
    for i in range(0,num_lines):
        canvas.create_line(x+(width/2),y+(height/2),x+i*(width/(num_lines-1)),y+height,fill='black') 



def draw_bowtie(canvas, x, y, width, height, num_lines):
    """
    1.draw lightblue rectangle
    2.draw red bowtie
    """
    canvas.create_rectangle(x, y, x+width, y+height, outline='lightblue') 
    for i in range(0,num_lines):
        canvas.create_line(x,y+i*(height/(num_lines-1)),x+width,y+height-i*(height/(num_lines-1)),fill='red') 


def draw_quilt(canvas, width, height, n):
    """
    Given a canvas which has the dimensions given by the parameters
    width and height, draw a whole quilt on it.  The quilt should
    be comprised of a n-by-n grid of patches (where n is parameter
    that is passed into this function).
    """
    sub_width = int(width / n)  #round down
    sub_height = int(height / n) #round down

    # loop over rows and columns of patches
    for row in range(n):
        for col in range(n):
            # Draw one patch of the grid of patches
            choice = (row + col) % 3
            if (choice==0):
                draw_bars(canvas, col*sub_width, row*sub_height, sub_width, sub_height, n)
            elif (choice==1):
                draw_bowtie(canvas, col*sub_width, row*sub_height, sub_width, sub_height, n)
            elif (choice==2):
                draw_eye(canvas, col*sub_width, row*sub_height, sub_width, sub_height, n)


######## DO NOT MODIFY ANY CODE BELOW THIS LINE ###########

# main() code is complete and should not be modified.
# There are 5 command lines that work here,
# with width/height/n being positive integers.
#  -bars width height num_lines
#  -eye width height num_lines
#  -bowtie width height num_lines
#  -quilt width height n
# e.g. run like this in the terminal:
#  py quilt.py -bars 600 400 10


# This function is provided to you and should not be modified.
# It creates a window that contains a drawing canvas that you
# will use to make your drawings.
def make_canvas(width, height):
    """
    DO NOT MODIFY
    Creates and returns a drawing canvas of the
    of the given int size, ready for drawing.
    """
    top = tkinter.Tk()
    top.minsize(width=width + 10, height=height + 10)
    top.title('quilt')
    canvas = tkinter.Canvas(top, width=width + 2, height=height + 2,background='lightgrey')
    canvas.pack()
    canvas.xview_scroll(8, 'units')  # add this so (0, 0) works correctly
    canvas.yview_scroll(8, 'units')  # otherwise it's clipped off

    return canvas


def main():
    # Standard first line of main to get args
    args = sys.argv[1:]

    if len(args) != 4:
        print('usage: (one of -bars, -eye, -bowtie, -quilt) width height n')
        return

    # Parse width/height/n from command line, giving a helpful
    # error message if it fails.
    try :
        width = int(args[1])
        height = int(args[2])
        n = int(args[3])
    except Exception as e:
        print("Error parsing int width/height/n from command line:" + ' '.join(args))
        return

    # Tricky: we do all the drawing in a try, so that if it takes an exception,
    # we can still do the mainloop() at the end. If we do not do this, an exception
    # causes no graphics output to appear which makes debugging hard.
    try:
        if args[0] == '-bars':
            canvas = make_canvas(width * 2, height * 2)
            # Can change to fast_draw=False .. drawing plays out more slowly
            draw_bars(canvas, 0, 0, width, height, n)
            draw_bars(canvas, width, height, width, height, n)

        if args[0] == '-eye':
            canvas = make_canvas(width * 2, height * 2)
            draw_eye(canvas, 0, 0, width, height, n)
            draw_eye(canvas, width, height, width, height, n)

        if args[0] == '-bowtie':
            canvas = make_canvas(width * 2, height * 2)
            draw_bowtie(canvas, 0, 0, width, height, n)
            draw_bowtie(canvas, width, height, width, height, n)

        if args[0] == '-quilt':
            canvas = make_canvas(width, height)
            draw_quilt(canvas, width, height, n)

    # Print out exception from draw
    except Exception as e:
        print(e)

    """
    Calls the tkinter.mainloop(), typically last line of main().
    This version checks that there is a window on screen first,
    doing nothing if there is no window.
    """
    if tkinter._default_root:
        tkinter._default_root.update()
        tkinter.mainloop()


if __name__ == '__main__':
    main()
