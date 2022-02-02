from dataclasses import dataclass  # імортуємо модуль, який описує тип даних

dataclass()


class RecordDataClass:  # зазначаємо, яке поле, що означає у лісті
    mark_name: str
    price: int
    year: int


marks_list = [{
    'marks': 'all_of_the_marks'
    # далі, мають бути прописанні об'єкти зверху з їхніми типами даних (як я поняв), часу розібратись не вистачило,
    # до кінця :(
}]
