import flet
from flet import (Page, FilePicker, Text,
                  ElevatedButton, Row, Column, FilePickerResultEvent)


def main(page: Page):   
# 2) CREATE THE EVENT FOR FILEPICKER (TO OPEN THE FILEPICKER DIR WINDOW)
    def select_file(e: FilePickerResultEvent):
        page.add(filepicker)
        filepicker.pick_files("Select file...")
# 3) CREATE THE FUNCTION OF EVENT
    def return_file(e: FilePickerResultEvent): 
        file_path.value = e.files[0].path
        file_path.update()

    row_filepicker = Row(vertical_alignment="center")
    file_path = Text(value="Selected file path", expand=1)
# 1) CREATE A FILEPICKER:
    filepicker = FilePicker(on_result=return_file)
    
    row_filepicker.controls.append(
        ElevatedButton(
            text="Select file...", on_click=select_file))
    # ADD THE PATH (if you will select it)
    row_filepicker.controls.append(
        file_path)
        
    page.add(row_filepicker)
    
if __name__ == '__main__':
    flet.app(target=main)