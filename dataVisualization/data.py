import json
import numpy as np
from tabulate import *
import plot
# measures = dict()
# measuresInsights = list()


def readFileSecuencial(fileName):
    measures = dict()
    with open(fileName, "r") as f:
        content = f.readlines()

    try:
        for line in content:
            parsedLine = line.replace("\n", "").strip()
            parsedContent = parsedLine.split(":")
            if parsedContent[0] not in list(measures.keys()):
                # 2 refers to MatrixMultiplication secuential test
                # 3 refers to pi_approximation secuential-parallel tests
                if len(parsedContent) > 2:
                    measures[parsedContent[0]] = [
                        [float(parsedContent[1]), float(
                            parsedContent[2]), float(parsedContent[3])]
                    ]
                else:
                    measures[parsedContent[0]] = [float(parsedContent[1])]
            else:
                if len(parsedContent) > 2:
                    measures[parsedContent[0]].append(
                        [float(parsedContent[1]), float(parsedContent[2]), float(parsedContent[3])])
                else:
                    measures[parsedContent[0]].append(float(parsedContent[1]))

        print("File parsed succesfully!")
        return measures
    except:
        raise Exception("An error occured")


def readFileParallel(fileName):
    measures = dict()
    measuresTabulation = dict()
    with open(fileName, "r") as f:
        content = f.readlines()

    try:
        """
        {
            "300": [
                    [
                        "2",
                        0.099284
                    ],
                    ...
                    ],
                    ...
        }
        """
        for line in content:
            parsedLine = line.replace("\n", "").strip()
            parsedContent = parsedLine.split(":")

            if parsedContent[0] not in list(measures.keys()):
                measures[parsedContent[0]] = list()
            if parsedContent[0] not in list(measuresTabulation.keys()):
                measuresTabulation[parsedContent[0]] = {}
            if parsedContent[3] not in list(measuresTabulation[parsedContent[0]].keys()):
                measuresTabulation[parsedContent[0]][parsedContent[3]] = list()

            measures[parsedContent[0]].append(
                [parsedContent[1], float(parsedContent[2])])

            measuresTabulation[parsedContent[0]][parsedContent[3]].append(
                float(parsedContent[2]))

        print("File parsed succesfully!")
        return measures, measuresTabulation
    except:
        raise Exception("An error occured")


def dataInsigthsSecuencial(measures):
    measuresInsights = list()
    for measure in measures.items():
        measureTimesAsArr = np.array(measure[1])
        measuresInsights.append((measure[0], np.average(measureTimesAsArr)))
    return measuresInsights


def dataInsigthsParallel(measures):
    # print("while entry: ", measures)
    # print("\n")
    measuresInsights = list()
    keys = list(measures.keys())
    allThreads = dict()
    for matrixSize in keys:
        allThreads[matrixSize] = {}
        for threadMeasure in measures[matrixSize]:
            if threadMeasure[0] not in list(allThreads[matrixSize].keys()):
                allThreads[matrixSize][threadMeasure[0]] = [threadMeasure[1]]
            else:
                allThreads[matrixSize][threadMeasure[0]].append(
                    threadMeasure[1])
    # threadsAvg = []
    for matrixSize in allThreads:
        """
        {
        "300"": {
            "1":[0.67, 0.56, ...],
            "2":[0.67, 0.56, ...],
            ...
            },
        "600"": {
            "1":[0.67, 0.56, ...],
            "2":[0.67, 0.56, ...],
            ...
            },
        }
        To
        [["300", 0.56], ["600",0.67]]
        """
        threadsAvg = []
        for threadKey in allThreads[matrixSize]:
            measureTimesAsArrByThread = np.array(
                allThreads[matrixSize][threadKey])
            measureTimesAsArrByThreadAvg = np.average(
                measureTimesAsArrByThread)
            threadsAvg.append(measureTimesAsArrByThreadAvg)
        measureTimesAsArr = np.array(threadsAvg)
        measuresInsights.append((matrixSize, np.average(measureTimesAsArr)))
    # # print("while exit: ", measures)
    # # print("\n")
    return measuresInsights


def speedUp(parallelTime, secuencialInsigths):
    speedUpRow = []
    # print("info to speedup: ", secuencialInsigths,
    #       parallelTime)
    for measure in range(0, len(secuencialInsigths)):
        if isinstance(secuencialInsigths[measure], np.ndarray) and isinstance(parallelTime[measure], np.ndarray):
            # pi_approximation
            speedUpRow.append(
                secuencialInsigths[measure][2]/parallelTime[measure][2])
        else:
            # montecarlo
            speedUpRow.append(
                secuencialInsigths[measure][1]/parallelTime[measure])
    return speedUpRow


def tabulateSecuencialData(measures, measuresInsights):
    headers = ["Iteración", "300", "600", "900", "1200", "1500",
               "1800", "2100", "2400", "2700", "3000"]

    rows = []
    for iteration in range(1, 11):
        row = []
        for matrix_size in measures:
            data = measures[matrix_size][iteration-1]
            row.append(data)
        row.insert(0, iteration)
        rows.append(row)
    threadAvg = ["Promedio"]
    for avg in measuresInsights:
        threadAvg.append(avg[1])

    rows.append(threadAvg)
    print(tabulate(rows, headers=headers))


def tabulateParallelData(measuresTabulation, measuresInsights, secuencialInsigths, label):
    headers = ["Iteración", "300", "600", "900", "1200", "1500",
               "1800", "2100", "2400", "2700", "3000"]
    speedUpRowsToReturn = {}
    for totalParallelUnits in measuresTabulation:
        print(label)
        print(totalParallelUnits, " ------------------\n")
        rows = []
        for iteration in range(1, 11):
            row = []
            for matrixSize in measuresTabulation[totalParallelUnits]:
                data = np.array(
                    measuresTabulation[totalParallelUnits][matrixSize][str(iteration)])
                dataAvg = np.average(data)
                row.append(dataAvg)
            # row.insert(0, iteration)
            rows.append(row)

        threadAvg = ["Avg"]
        for avg in measuresInsights[totalParallelUnits]:
            threadAvg.append(avg[1])

        rows.append(threadAvg)
        speedupRow = speedUp(threadAvg, secuencialInsigths)
        rows.append(speedupRow)
        # plot.makeSpeedupPlot(speedupRow, totalParallelUnits+" "+label)
        print(tabulate(rows, headers=headers, showindex=True))
        print("\n\n")
        rows[-1].append(totalParallelUnits+" "+label)
        speedUpRowsToReturn[totalParallelUnits] = rows[-1]
    return speedUpRowsToReturn


def dataInsigthsSecuencialPi_approximation(measures, **kwargs):
    measuresInsights = list()
    for measure in measures.items():
        measureTimesAsArr = np.array(measure[1])
        # print("MEASURE TO AVG AS ARR: ", measureTimesAsArr)
        measuresInsights.append(np.mean(measureTimesAsArr, axis=0))
        # print("These are the insights-avg: ", measuresInsights)
    return_values = []
    return_values.append(measuresInsights)
    if "secuencialReferent" in kwargs.keys():
        speedup = speedUp(measuresInsights, kwargs["secuencialReferent"])
        return_values.append(speedup)
    return return_values[0] if len(return_values) == 1 else return_values


def tabulateSecuencialDataPi_approximation(measures,  measuresInsights, plotTitle):

    headers = ["10000", "100000", "1000000",
               "10000000", "100000000", "1000000000"]
    rows = []

    for pi_approximation_data in range(1, 11):
        row = []
        for num_of_iterations in measures:
            data = measures[num_of_iterations][pi_approximation_data-1]
            row.append(data)
        # row.insert(0, pi_approximation_data)
        rows.append(row)

    if isinstance(measuresInsights[0], list):
        measuresMean = measuresInsights[0]
        speedupRow = measuresInsights[1]
        # slicedMeasureInsight = []
        # for measure in range(0, len(measuresInsights)):
        #     slicedMeasureInsight.append(measuresInsights[measure])
        #     newArray = np.append(
        #         measuresInsights[measure], speedupRow[measure])
        #     measuresInsights[measure] = newArray
        # rows.append(slicedMeasureInsight)
        rows.append(measuresMean)
        rows.append(speedupRow)
    else:
        rows.append(measuresInsights)

    print(tabulate(rows, headers=headers, showindex=True,
          colalign=('center',), tablefmt="rounded_outline"))

    # plot.makeSecuencialPlotPi_approximation(
    #     measuresInsights=measuresInsights, title=plotTitle)
