def parse_collection(text):
    if not isinstance(text, str):
        return None

    try:
        material, kg = text.split(':')
        material = material.strip()

        if not material:
            return None

        return material.title(), float(kg)
    except (ValueError, TypeError):
        return None


def weight_average(weights_csv):
    if not isinstance(weights_csv, str):
        return None

    try:
        values = [int(r.strip()) for r in weights_csv.split(',')]

        if not values:
            return None

        return sum(values) // len(values)
    except (ValueError, TypeError, ZeroDivisionError):
        return None


def net_points(text):
    if not isinstance(text, str):
        return None

    try:
        points, penalty = text.split('|')
        total = float(points) * 2 - float(penalty)
        return max(total, 0)
    except (ValueError, TypeError):
        return None


def main():
    print("==== Running parse_collection ====")
    user_input = input("Enter material:weight in kg (e.g. paper:12): ")
    result = parse_collection(user_input)
    print("Material and Weight:", result)

    print("\n==== Running weight_average ====")
    user_input = input("Enter weights in kg as CSV (e.g. 5,12,20): ")
    result = weight_average(user_input)
    print("Average Weight:", result)

    print("\n==== Running net_points ====")
    user_input = input("Enter points|penalty (e.g. 80|10): ")
    result = net_points(user_input)
    print("Net Points:", result)


if __name__ == "__main__":
    main()