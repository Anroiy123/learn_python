import numpy as np

def combine_rooms(room_1, room_2):
    result = np.empty(7, dtype=object)
    for i in range(7):
        if room_1[i] > 0:
            result[i] = room_1[i]
        elif room_2[i] > 0:
            result[i] = room_2[i]
        else:
            result[i] = None
    return result

room_1 = np.array([1, 2, -3, 4, 5, 6, -7])
room_2 = np.array([8, 9, 10, 11, 12, -13, -14])
final_list = combine_rooms(room_1, room_2)
print(final_list)