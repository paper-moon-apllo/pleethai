class Common:
    # Check value in list or not
    def contains(list, value, filter):
        if list is not None:
            for item in list:
                if filter(item, value):
                    return True
        return False
