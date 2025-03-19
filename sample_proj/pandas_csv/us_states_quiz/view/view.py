import turtle
from sample_proj.pandas_csv.us_states_quiz.helper.io import get_file_path as rf


class View:
    """
    A class to handle the graphical user interface for the U.S. States Quiz game.
    This class uses the `turtle` module to display a map of the U.S. and interact with the user.
    """

    def __init__(self):
        """
        Initializes the View class.
        Sets up the screen, loads the U.S. map image, and prepares the view for the game.
        """
        self.file_name = 'blank_states_img.gif'  # File name of the U.S. map image
        self.screen = turtle.Screen()  # Create a turtle screen object

        # Set up the view with the U.S. map image
        self.setup_view(image_path=self.set_image())

        # Uncomment the line below to enable debugging mouse click coordinates
        # turtle.onscreenclick(self.get_mouse_click_coor)

    def get_state_from_user(self, correct):
        """
        Prompts the user to enter the name of a U.S. state.

        Args:
            correct (int): The number of correctly guessed states so far.

        Returns:
            str: The user's input, formatted in title case (e.g., "New York").
        """
        user_answer = self.screen.textinput(
            title=f'{correct}/50 States Correct',  # Display progress in the prompt title
            prompt='Insert state name'  # Prompt the user for input
        )
        return user_answer.title()  # Convert the input to title case

    def get_mouse_click_coor(self, x, y):
        """
        Debugging method to print the coordinates of a mouse click on the screen.

        Args:
            x (float): The x-coordinate of the mouse click.
            y (float): The y-coordinate of the mouse click.
        """
        print(x, y)

    def setup_view(self, image_path):
        """
        Configures the turtle screen with the U.S. map image and sets up the window.

        Args:
            image_path (str): The path to the U.S. map image file.
        """
        self.screen.setup(width=750, height=600)  # Set the screen size
        self.screen.title('U.S. States Game')  # Set the window title
        self.screen.addshape(image_path)  # Add the image as a turtle shape
        turtle.shape(image_path)  # Set the turtle cursor to the U.S. map image

    def mark_on_map(self, coordinate):
        """
        Marks a state's name on the map at the specified coordinates.

        Args:
            coordinate (tuple): A tuple containing the x-coordinate, y-coordinate, and state name.
                                Example: (x, y, "California")
        """
        t = turtle.Turtle()  # Create a new turtle object
        t.hideturtle()  # Hide the turtle cursor
        t.penup()  # Lift the pen to avoid drawing lines
        t.goto(coordinate[0], coordinate[1])  # Move the turtle to the specified coordinates
        t.write(coordinate[2])  # Write the state name at the coordinates

    def set_image(self):
        """
        Reads and returns the path to the U.S. map image file.

        Returns:
            str: The path to the U.S. map image file.
        """
        return rf(file_name=self.file_name)  # Use the `read_file` function to get the image path

    def exit(self):
        """
        Exits the game and closes the turtle screen when the user clicks on the window.
        """
        # Uncomment the line below to keep the window open until manually closed
        # turtle.mainloop()
        self.screen.exitonclick()  # Close the window when the user clicks on it
        turtle.bye()