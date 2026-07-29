from docscrub.cleaners.whitespace import remove_extra_whitespace


class Cleaner:

    def __init__(self):
        self.cleaners = [
            remove_extra_whitespace
        ]

    def clean(self, text: str) -> str:
        """
        Clean raw text using registered cleaners.
        """

        for cleaner in self.cleaners:
            text = cleaner(text)

        return text