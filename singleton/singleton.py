class Singelton(object):
    """
    implements Singelton class
    """
    __instance = None
    def __init__(self):
        """ Virtually private constructor. """
        if Singelton.__instance != None:
            raise Exception("This Class is Singelton!")
        else:
            Singelton.__instance = self


    @staticmethod
    def get_instance():
        """
        static access method
        """
        if Singelton.__instance == None:
            Singelton()
        return Singelton.__instance

s = Singelton()
print (s)

s = Singelton.get_instance()
print (s)

s = Singelton.get_instance()
print (s)

