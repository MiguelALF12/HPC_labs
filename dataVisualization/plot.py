from matplotlib import pyplot as plt
plt.rcParams["figure.figsize"] = (15, 6)


def makeSecuencialPlot(measuresInsights):
    # fig = plt.figure()
    # ax = fig.add_subplot(111)
    matrixSizes_x = []
    timeConsumedByEachSize_y = []

    for measure in measuresInsights:
        matrixSizes_x.append(measure[0])
        timeConsumedByEachSize_y.append(measure[1])

    plt.plot(matrixSizes_x, timeConsumedByEachSize_y, label="Secuencial")
    plt.xlabel('Matrix sizes')
    plt.ylabel('Time consumed')
    # plot title
    plt.title("Secuencial")
    plt.legend(loc="upper left")
    # ax.grid()
    plt.show()


def makeParallelPlot(measuresInsights, title, label):
    # fig = plt.figure()
    # ax = fig.add_subplot(111)

    for measures in measuresInsights:
        # {numberOfThreads/Proccess: [...]} - measure is the key
        matrixSizes_x = []
        timeConsumedByEachSize_y = []
        for item in measuresInsights[measures]:
            # [...] -> [[],[],...] - item is the one list of the whole list
            matrixSizes_x.append(item[0])
            timeConsumedByEachSize_y.append(item[1])
        plt.plot(matrixSizes_x, timeConsumedByEachSize_y,
                 label=measures+" "+label)

    plt.xlabel('Matrix sizes')
    plt.ylabel('Time consumed')
    # plot title
    plt.title(title)
    plt.legend(loc="upper left")
    # ax.grid()
    plt.show()


def getAxis(measuresInsights):
    matrixSizes_x = []
    timeConsumedByEachSize_y = []
    for measure in measuresInsights:
        matrixSizes_x.append(measure[0])
        timeConsumedByEachSize_y.append(measure[1])
    return (matrixSizes_x, timeConsumedByEachSize_y)


def makeGeneralPlot(*argv):
    secuencialAxis = getAxis(argv[0])
    plt.plot(secuencialAxis[0], secuencialAxis[1], label="Secuencial")
    # It doesnt matter which of the measures is selected, all neeed to have the same values.

    for measureInsigths in range(1, 3):
        # [measureInsights1, measureInsights1, ...]
        label = "Processes" if measureInsigths % 2 == 0 else "Thread"
        measure_to_analyze = argv[measureInsigths]
        # print("foo: ", label, measure_to_analyze)
        for size_of_measure in measure_to_analyze:
            # measure_to_analyze = {numberOfThreads/Proccess: [...]} - size_of_measure is the key
            current_measure_axis = getAxis(measure_to_analyze[size_of_measure])
            plt.plot(
                current_measure_axis[0], current_measure_axis[1], label=size_of_measure+" "+label)

    # threadAxis =
    # processAxis =

    plt.xlabel('Matrix sizes')
    plt.ylabel('Time consumed')
    # plot title
    plt.title("Todo")
    plt.legend(loc="upper left")
    # ax.grid()
    plt.show()


def makeSpeedupPlot(speedups):
    # print(speedups)
    matrix_sizes_x = ["300", "600", "900", "1200", "1500",
                      "1800", "2100", "2400", "2700", "3000"]
    for speedupValues in speedups:
        for totalParallelUnits in speedupValues:
            plt.plot(matrix_sizes_x, speedupValues[totalParallelUnits]
                     [1:-1], label=speedupValues[totalParallelUnits][-1])

    plt.xlabel('Matrix sizes')
    plt.ylabel('SpeedUp')
    plt.title(
        "Speedup con relación a los tamaños de matrices, en cada variación del algoritmo")
    plt.legend(loc="upper left")
    plt.show()


def traverseMeanData(means):
    pi_approximation_aux = []
    errors_aux = []
    time_consumed_aux = []
    for measure in means:
        print("\n")
        pi_approximation_aux.append(measure[0])
        errors_aux.append(measure[1])
        time_consumed_aux.append(measure[2])

    return pi_approximation_aux, errors_aux, time_consumed_aux


def oneDataOrMany(measures):
    measuresAvg = None
    measuresSpeedUp = None
    # True - measures with label meaning multiple data
    if len(measures) > 1:
        return True
    else:  # False - mone list of arrays with measures, one data
        return False


def elaboratePlot(pi_approximation_y, errors_y, time_consumed_y, speedUps_y, line_legacy, speedUp_line_legacy, title):

    num_of_iterations_x = ["10000", "100000", "1000000",
                           "10000000", "100000000", "1000000000"]
    data_to_plot_y = [pi_approximation_y, errors_y, time_consumed_y]
    y_labels = ['PI approximation', 'error %', 'time consumed']

    if len(speedUps_y) > 0:
        y_labels.append('speed up')
        data_to_plot_y.append(speedUps_y)

    if len(pi_approximation_y) > 1 and len(errors_y) > 1 and len(time_consumed_y) > 1:  # one plot multiple lines
        for data_index in range(0, len(data_to_plot_y)):
            for points in range(len(data_to_plot_y[data_index])):
                # ax.grid()
                if len(line_legacy) == 0:
                    label = y_labels[data_index]
                else:
                    if data_index == len(data_to_plot_y)-1:
                        # print("points: ", points, len(
                        #     data_to_plot_y[data_index]),
                        #     data_to_plot_y[data_index], "\n")
                        label = speedUp_line_legacy[points]
                    else:
                        label = line_legacy[points]

                plt.plot(num_of_iterations_x,
                         data_to_plot_y[data_index][points], label=label)
            plt.xlabel('# of iterations')
            plt.title(title+"("+y_labels[data_index]+")")
            plt.legend(loc="upper left")
            # plt.savefig(data_title_key.replace(' ', '_')+y_labels[data_index]+".png")
            plt.show()
    else:
        for data_index in range(0, len(data_to_plot_y)):
            plt.plot(num_of_iterations_x,
                     data_to_plot_y[data_index][0], label=y_labels[data_index])
            plt.xlabel('# of iterations')
            plt.title(title)
            plt.legend(loc="upper left")
            # plt.savefig(data_title_key.replace(' ', '_')+y_labels[data_index]+".png")
            plt.show()


def makePlotPi_approximation(data):
    # **kwargs = [measuresInsights, title, allInOne]
    """
    data = {
                        One measure         Multiple measures
        "plot_title": [1,2,3,4, ... ] || [[1,2,3],[4,5,6,], ...], -> One plot
        ....
    }
    """

    pi_approximation_y = []
    errors_y = []
    time_consumed_y = []
    speedUps_y = []
    # data_to_plot_y = [pi_approximation_y, errors_y, time_consumed_y]
    # y_labels = ['PI approximation', 'error %', 'time consumed']
    line_legacy = []
    speedUp_line_legacy = []
    measuresAvg = None
    measuresSpeedUp = None

    for title, data in data.items():
        # print(data, len(data))
        # print(len(data) > 2)
        if len(data) > 2:  # plot with multiple lines
            # Many
            for insights in data:
                if len(insights[0]) == 2:
                    measuresAvg = insights[0][0]
                    # measuresSpeedUp = insights[0][1]
                    print(title, insights[1], "\n")
                    speedUps_y.append(insights[0][1])
                    speedUp_line_legacy.append(insights[1])
                else:
                    measuresAvg = insights[0]

                parametersToMeasure = traverseMeanData(measuresAvg)
                pi_approximation_y.append(parametersToMeasure[0])
                errors_y.append(parametersToMeasure[1])
                time_consumed_y.append(parametersToMeasure[2])
                line_legacy.append(insights[1])

        else:  # Plot with one line
            if len(data) == 2:
                measuresAvg = data[0]
                # measuresSpeedUp = data[1]
                speedUps_y.append(data[1])
            else:
                measuresAvg = data

            parametersToMeasure = traverseMeanData(measuresAvg)
            pi_approximation_y.append(parametersToMeasure[0])
            errors_y.append(parametersToMeasure[1])
            time_consumed_y.append(parametersToMeasure[2])

            # if measuresSpeedUp != None:  # there is a speedUp measure
            #     speedUps_y.append(measuresSpeedUp)

        print("PI-APPROX: ", pi_approximation_y)
        print("\n")
        print("ERRORS: ", errors_y)
        print("\n")
        print("TIME CONSUMED: ", time_consumed_y)
        print("\n")
        print("SPEEDUP: ", speedUps_y)
        print("\n")
        print("LINE LEGACY: ", line_legacy)
        print("\n")
        print("SPEEDUP LEGACY: ", speedUp_line_legacy)
        print("\n")

        elaboratePlot(pi_approximation_y, errors_y, time_consumed_y,
                      speedUps_y, line_legacy, speedUp_line_legacy, title)
        pi_approximation_y = []
        errors_y = []
        time_consumed_y = []
        speedUps_y = []
        line_legacy = []
        speedUp_line_legacy = []


# makePlot()
