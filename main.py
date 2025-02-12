import math

def calculate_number_of_luminaires():
    """
    Рассчитывает количество светильников для освещения комнаты на основе введенных пользователем данных.
    """
    while True:
        try:
            # Запрашиваем данные у пользователя
            area = float(input("Введите площадь комнаты (м²): "))
            if area <= 0:
                print("Площадь комнаты должна быть положительным числом. Попробуйте снова.")
                continue

            required_illuminance = float(input("Введите требуемую освещенность (лк): "))
            if required_illuminance <= 0:
                print("Требуемая освещенность должна быть положительным числом. Попробуйте снова.")
                continue

            luminous_flux = float(input("Введите световой поток одного светильника (лм): "))
            if luminous_flux <= 0:
                print("Световой поток должен быть положительным числом. Попробуйте снова.")
                continue

            utilization_factor = float(input("Введите коэффициент использования светового потока (от 0.4 до 0.9): "))
            if utilization_factor <= 0 or utilization_factor > 1:
                print("Коэффициент использования светового потока должен быть в диапазоне (0, 1]. Попробуйте снова.")
                continue

            # Расчет количества светильников
            number_of_luminaires = (required_illuminance * area) / (luminous_flux * utilization_factor)
            number_of_luminaires = math.ceil(number_of_luminaires)  # Округляем вверх

            # Вывод результата
            print(f"Необходимое количество светильников: {number_of_luminaires}")
            break  # Выход из цикла после успешного расчета

        except ValueError:
            print("Ошибка: введены некорректные данные. Пожалуйста, введите числа.")
        except Exception as e:
            print(f"Произошла ошибка: {e}. Попробуйте снова.")

# Запуск функции расчета
calculate_number_of_luminaires()