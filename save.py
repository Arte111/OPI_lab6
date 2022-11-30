from openpyxl import load_workbook


class Saver:
    def __init__(self, filename):
        self.filename = filename

    def add_on_top(self, data):
        # append don't work here, I don't know why
        work_book = load_workbook(self.filename)
        sheet = work_book.active  # do active one page
        sheet.insert_rows(1)  # add row on the top
        for cols, value in enumerate(data):
            sheet.cell(row=1, column=cols + 1).value = value

        work_book.save(self.filename)
