def find_highest_averaged_predictions(coordinate_prediction_lists):
    averages = []
    for coordinate_prediction_list in coordinate_prediction_lists:
        total = 0
        for prediction in coordinate_prediction_list:
            total = prediction[1] + total
        averages.append(total / len(coordinate_prediction_list))
    # find the biggest average and get the index
    print(averages)
    index = averages.index(max(averages))
    print(index)
    return coordinate_prediction_lists[index]