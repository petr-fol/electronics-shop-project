class InstantiateCSVError(Exception):
    def __init__(self, message='Файл item.csv поврежден'):
        super().__init__(message)
