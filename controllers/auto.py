from . import BaseController

class Controller(BaseController):
    """
    An autoregressive controller that predicts the car's response based on previous states and actions.
    """
    def __init__(self):
        self.previous_errors = []

    def update(self, target_lataccel, current_lataccel, state):
        # Calculate the error between target and current lateral acceleration
        error = target_lataccel - current_lataccel

        # Append the error to the history
        self.previous_errors.append(error)
        
        # Use a simple moving average of the last few errors as the control signal
        #window_size = 5
        window_size=5
        if len(self.previous_errors) > window_size:
            self.previous_errors = self.previous_errors[-window_size:]
        
        # Calculate the average error
        avg_error = sum(self.previous_errors) / len(self.previous_errors)
        
        # Scale the average error by a factor to determine the control action
        control_action = avg_error * 0.3
        
        return control_action

