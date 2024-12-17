def calculate_cost(area, material_cost, installation_cost, additional_services_cost):
    total_area_cost = float(area) * float(material_cost)
    total_installation_cost = float(installation_cost)
    total_additional_services_cost = float(additional_services_cost)

    total_cost = total_area_cost + total_installation_cost + total_additional_services_cost

    return f'Общая стоимость: {total_cost:.2f} руб.'