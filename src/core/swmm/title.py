from core.project_base import Section


class Title(Section):
    """SWMM descriptive title"""

    SECTION_NAME = "[TITLE]"

    def __init__(self):
        Section.__init__(self)

        ## str: Descriptive title
        self.title = "SWMM Project"

