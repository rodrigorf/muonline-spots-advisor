import time

class HeaderGenerator:
    
    def __init__(self, header_text, header_width):
        self.header_text = header_text
        self.header_width = header_width
        
    def generate_header(self):
        top_bot_border = "+" + "*" * self.header_width + "+"
        header_text = f"|{'{:^{}}'.format(self.header_text, self.header_width)}|"
        comment_header = f"{top_bot_border}\n{header_text}\n{top_bot_border}\n\n"
        print(comment_header)
