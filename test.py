class Info:

    class Setting:
        level = "INFO"
        prefix = "[LOG]"

    def show(self, message):
        print(f"{self.Setting.prefix} ({self.Setting.level}) {message}")


L1 = Info()
L1.name = 'ali'
L1.show("Hello World")
