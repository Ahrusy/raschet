def calculate_number_of_luminaires():
    """
    Рассчитывает количество светильников для освещения комнаты на основе введенных пользователем данных.
    """
    try:
        # Запрашиваем данные у пользователя
        area = float(input("Введите площадь комнаты (м²): "))
        required_illuminance = float(input("Введите требуемую освещенность (лк): "))
        luminous_flux = float(input("Введите световой поток одного светильника (лм): "))
        utilization_factor = float(input("Введите коэффициент использования светового потока (от 0.4 до 0.9): "))

        # Проверка корректности коэффициента использования
        if utilization_factor <= 0 or utilization_factor > 1:
            raise ValueError("Коэффициент использования светового потока должен быть в диапазоне (0, 1].")

        # Расчет количества светильников
        number_of_luminaires = (required_illuminance * area) / (luminous_flux * utilization_factor)
        number_of_luminaires = round(number_of_luminaires)

        # Вывод результата
        print(f"Необходимое количество светильников: {number_of_luminaires}")

    except ValueError as e:
        print(f"Ошибка ввода данных: {e}")

# Запуск функции расчета
calculate_number_of_luminaires()