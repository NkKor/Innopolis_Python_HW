class IncorrectUserIdError(Exception):
    def __init__(self,message,custom_data=None):
        super().__init__(message)
        self.custom_data=custom_data

def check_id(id: int):
    if len(str(id)) == 6:
        print("Пользовательский ID корректен")
    else:
        raise IncorrectUserIdError("IncorrectUserIdError", custom_data={"Не корректный ID": "ID пользователя должен быть 6и значным целым числом"})


try:
    user_id = int(input())
    check_id(user_id)
except IncorrectUserIdError as e:
    print(e, e.custom_data)
except ValueError as e:
    print("Ошибка коррктности ввода ID: ID должен состоять из 6 цифр")
