"""Class to store a message (operator overload; union types; default parameters)."""

class Message:
    to: str
    content: str
    important: bool

    def __init__(self, recipient: str, message_content: str, importance_flag: bool) -> None:
        """Construct a message."""
        self.to = recipient
        self.content = message_content
        self.important = importance_flag

    def __str__(self) -> str:
        """Convert message to a string."""
        return f'Message to: {self.to}\nImportant? {self.important}\n"{self.content}"'

    def __mul__(self, factor: int) -> None:
        """Multiplication operator overload."""
        original: str = self.content
        for loop_number in range(1, factor):
            self.content += " " + original
        

msg: Message = Message("Erin", "Great Job!", False)
#msg * 100
print(msg)