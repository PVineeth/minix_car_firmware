#MiniX Language
#Version: 1.0.0
import threading

class Commands:

    recognized_commands = ['Go', 'Forward', 'Backward', 'Right', 'Left', 'Apply', 'Brake', 'Acc', 'SetMode', 'Manual', 'ATC']
    component_obj =['']  # Initialize the objects of the component list created in main as empty
    rcvcommglobal = 0 # Dummy Value

    def get_objects(self, obj):  # Getting a list of components class instances
        self.component_obj=obj  # obj[0] = motors

    def split_command(self, command):
        comm = command.split(b'=')  # We receive commands in this form X=Y. Mind it no spaces!
        print (comm[0].decode())
        print (comm[1].decode())
        return comm

    def set_acc(self):
        self.component_obj[2].set_speed(self.rcvcommglobal[1].decode())
    
    def process_command(self, rcvcommand):
        rcvcomm = self.split_command(rcvcommand)    # First let's split the command.
        self.rcvcommglobal = rcvcomm
        if((rcvcomm[0].decode() == self.recognized_commands[0])  or (rcvcomm[0].decode() == self.recognized_commands[5])):  # Let's check to whose component this command belongs to. Here it belongs to the motor.
            if(rcvcomm[1].decode() == self.recognized_commands[1]):  # Go Forward! & Set the gear to forward. FIX IT
                self.component_obj[2].go_forward()  # We forgot to set the Enable bit to 1! FIX IT.
            elif(rcvcomm[1].decode() == self.recognized_commands[2]):  # Go Backward! & Set the gear to backward. FIX IT
                self.component_obj[2].go_backward()  # We forgot to set the Enable bit to 1! FIX IT.
            elif(rcvcomm[1].decode() == self.recognized_commands[3]):  # Go Right! Set steering to right. FIX IT
                self.component_obj[2].go_right()  # Keep Left Wheels On. Right Off. FIX IT (EN Bit)
            elif(rcvcomm[1].decode() == self.recognized_commands[4]):  # Go Left! Set steering to left. FIX IT
                self.component_obj[2].go_left()  # Keep Right Wheels On. Left Off. FIX IT (EN Bit)
            elif(rcvcomm[1].decode() == self.recognized_commands[6]):  # Apply brake. Rapid Deceleration. It's different from a crash!
                self.component_obj[2].apply_brakes()

        if((rcvcomm[0].decode() == self.recognized_commands[7])): # Set Car speed / Acceleration
            setcarspeed = threading.Thread(target=self.set_acc)
            setcarspeed.start()
            setcarspeed.join()
            # Thread Exits


    










