class SasiError(RuntimeError):
    def __init__(self):
        super(SasiError, self).__init__()
    def __str__(self):
        return "Job Not Found Error"
