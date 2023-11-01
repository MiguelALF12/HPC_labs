import data
import plot
import os
import json


def searchInFolder(folder_path, search_param):
    if os.path.exists(folder_path) and os.path.isdir(folder_path):
        # List all files in the folder
        files = os.listdir(folder_path)
        # Print the names of the files
        for file_name in files:
            if search_param == file_name.split(".")[0]:
                print("for files: ", search_param, file_name)
                return folder_path+"/"+file_name
    else:
        return ""


def loadParallelInfo(measures, measures_insigths, measureTabulation, file_path):
    # def loadParallelInfo(measures, file_path):
    for key in measures:
        file_name = searchInFolder(file_path, key)
        if len(file_name) > 0 and measures[key] == None:
            measures[key], measureTabulation[key] = data.readFileParallel(
                file_name)
            # print("foo: ", measureTabulation[key])
            measures_insigths[key] = data.dataInsigthsParallel(
                measures[key])
    return measures, measures_insigths, measureTabulation
    # return measures


if __name__ == "__main__":
    secuencial_meausures = None
    secuencial_meausures_insights = None
    threads_meausures = {
        "5": None,
        "15": None,
        "25": None
    }
    process_meausures = {
        "5": None,
        "15": None,
        "25": None
    }
    threads_meausures_insights = {
        "5": None,
        "15": None,
        "25": None
    }
    process_meausures_insights = {
        "5": None,
        "15": None,
        "25": None
    }
    threads_meausures_tabulation = {
        "5": None,
        "15": None,
        "25": None
    }
    process_meausures_tabulation = {
        "5": None,
        "15": None,
        "25": None
    }

    # Parsing logs
    # Secuencial
    secuencial_meausures = data.readFileSecuencial("logs/matrixSecuencial.log")
    secuencial_meausures_insights = data.dataInsigthsSecuencial(
        secuencial_meausures)

    # Threads
    threads_meausures, threads_meausures_insights, threads_meausures_tabulation = loadParallelInfo(
        threads_meausures, threads_meausures_insights, threads_meausures_tabulation, "logs/threads")
    # threads_meausures = loadParallelInfo(threads_meausures, "logs/threads")
    # Process

    process_meausures, process_meausures_insights, process_meausures_tabulation = loadParallelInfo(
        process_meausures, process_meausures_insights, process_meausures_tabulation, "logs/process")

    # Print the info
    # print("Secuencial -------------------- ")
    # print("measures: ", json.dumps(secuencial_meausures, indent=2), "\n")
    # print("insights: ", json.dumps(secuencial_meausures_insights, indent=2), "\n")
    # print("\n\n")
    # print("Threads -------------------- ")
    # print("measures: ", json.dumps(threads_meausures, indent=2), "\n")
    # print("insigths: ", json.dumps(threads_meausures_insights, indent=2), "\n")
    # print("tabulation: ", json.dumps(
    #     threads_meausures_tabulation, indent=2), "\n")
    # print("\n\n")
    # print("Process -------------------- ")
    # print("measures: ", json.dumps(process_meausures, indent=2), "\n")
    # print("insigths: ", json.dumps(process_meausures_insights, indent=2), "\n")
    # print("tabulation: ", json.dumps(
    #     process_meausures_tabulation, indent=2), "\n")
    # print("\n\n")

    # Plot
    # plot.makeSecuencialPlot(secuencial_meausures_insights)
    # plot.makeParallelPlot(threads_meausures_insights,
    #                       "Ejecución por Threads", "Threads")
    # plot.makeParallelPlot(process_meausures_insights,
    #                       "Ejecución por Procesos", "Procesos")
    # plot.makeGeneralPlot(secuencial_meausures_insights,
    #                      threads_meausures_insights, process_meausures_insights)
    print("SECUENCIAL")
    data.tabulateSecuencialData(secuencial_meausures,
                                secuencial_meausures_insights)
    print("\n\n")
    threadSpeedUp = data.tabulateParallelData(
        threads_meausures_tabulation, threads_meausures_insights, secuencial_meausures_insights, "THREADS")
    processSpeedUp = data.tabulateParallelData(
        process_meausures_tabulation, process_meausures_insights, secuencial_meausures_insights, "PROCESS")
    plot.makeSpeedupPlot([threadSpeedUp, processSpeedUp])
