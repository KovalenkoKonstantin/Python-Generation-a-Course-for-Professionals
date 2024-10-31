def picture(name: str):
    """
    Отображает изображение из указанного пути.

    :param name: Имя файла изображения, которое находится в папке 'D:\\images'.
    """
    from IPython.display import Image, display
    display(Image(filename=f'D:\\images\\{name}'))