import pandas
from sample_proj.pandas_csv.us_states_quiz.helper.io import read_file as rf


class StateData:
    """
        A class to handle U.S. state data, including loading state information from a CSV file,
        finding coordinates for a given state, and validating user input.
    """

    def __init__(self):
        self.file_name = '50_states.csv'
        self.state_csv = None

        self.upload_data()


    def upload_data(self):
        """
        Reads the state data from the CSV file and stores it in a pandas DataFrame.
        """
        self.state_csv = pandas.read_csv(rf(file_name=self.file_name))


    def find_state_coordinate(self, user_input):
        """
        Finds the coordinates (x, y) and the name of a state based on user input.

        Args:
            user_input (str): The name of the state to search for.

        Returns:
            tuple: A tuple containing the x-coordinate, y-coordinate, and state name.
                   Example: (139, -77, "New York")

        Raises:
            IndexError: If the state is not found in the DataFrame.
        """
        state_data = self.state_csv.state
        state_coor = self.state_csv[state_data == user_input]
        return (state_coor.iloc[0]['x'].item(),
                state_coor.iloc[0]['y'].item(),
                state_coor.iloc[0]['state'])


    def validate_input_state(self,input_state):
        """
            Validates whether a given state name exists in the list of states.

            Args:
                input_state (str): The state name to validate.

            Returns:
                bool: True if the state exists in the list, False otherwise.
        """
        state_data = self.state_csv.state
        state_list = state_data.values.tolist()

        return input_state in state_list
