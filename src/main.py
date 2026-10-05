def get_office_status(person_detected):
    if person_detected:
        return "in office"
    else:
        return "out of office"

person_detected = False
status = get_office_status(person_detected)
print(status)