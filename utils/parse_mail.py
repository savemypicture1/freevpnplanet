import re


class Parser:
    PASSWORD_REGEX = r'password:\*\\n\\n\*(.*?)\*\\n\\n'
    CONFIRM_REGEX = r'REGISTRATION \( (.*?) \)'

    def parse(self, regex: str, text: str) -> str | None:
        match = re.search(regex, text)
        if match:
            return match.group(1)
        else:
            return None

    def get_password(self, text: str) -> str | None:
        return self.parse(self.PASSWORD_REGEX, text)

    def get_confirm_link(self, text: str) -> str | None:
        return self.parse(self.CONFIRM_REGEX, text)


parser = Parser()
