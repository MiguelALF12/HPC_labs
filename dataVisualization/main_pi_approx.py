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


def print_information(*args):
    """
    0 - montecarlo_secuencial_meausures
    1 - needle_secuencial_meausures
    2 - montecarlo_secuencial_meausures_insights
    3 - needle_secuencial_meausures_insights
    4 - montecarlo_thread_meausures
    5 - needle_thread_meausures
    6 - montecarlo_thread_meausures_insights
    7 - needle_thread_meausures_insights
    8 - montecarlo_secuencial_compilation_optimized_meausures
    9 - needle_secuencial_compilation_optimized_measures
    10 - montecarlo_secuencial_compilation_optimized_meausures_insights
    11 - needle_secuencial_compilation_optimized_measures_insights
    12 - montecarlo_thread_compilation_optimized_meausures
    13 - needle_thread_compilation_optimized_measures
    14 - montecarlo_thread_compilation_optimized_meausures_insights
    15 - needle_thread_compilation_optimized_measures_insights
    """
    print("SECUENCIAL MEASURES-------------------- ")
    print("Montecarlo: ", json.dumps(
        args[0], indent=2), "\n")
    print("Needles: ", json.dumps(args[1], indent=2), "\n")
    # print("\n\n")
    print("SECUENCIAL INSIGTHS-------------------- ")
    print("Montecarlo: ", args[2], "\n")
    print("Needles: ", args[3], "\n")
    print("\n\n")
    print("THREAD MEASURES-------------------- ")
    print("Montecarlo: ", json.dumps(args[4], indent=2), "\n")
    print("Needles: ", json.dumps(args[5], indent=2), "\n")
    print("\n\n")
    print("THREAD INSIGHTS-------------------- ")
    print("Montecarlo: ", args[6], "\n")
    print("Needles: ", args[7], "\n")
    print("\n\n")
    print("SECUENCIAL COMPILATION-BASED OPTIMIZATION MEASURES-------------------- ")
    print("Montecarlo: ", json.dumps(
        args[8], indent=2), "\n")
    print("Needles: ", json.dumps(
        args[9], indent=2), "\n")
    print("\n\n")
    print("SECUENCIAL COMPILATION-BASED OPTIMIZATION INSIGTHS-------------------- ")
    print("Montecarlo: ",
          args[10], "\n")
    print("Needles: ", args[11], "\n")
    print("\n\n")
    print("THREADS COMPILATION-BASED OPTIMIZATION MEASURES-------------------- ")
    print("Montecarlo: ", json.dumps(
        args[12], indent=2), "\n")
    print("Needles: ", json.dumps(
        args[13], indent=2), "\n")
    print("\n\n")
    print("THREADS COMPILATION-BASED OPTIMIZATION INSIGHTS-------------------- ")
    print("Montecarlo: ",
          args[14], "\n")
    print("Needles: ", args[15], "\n")
    print("\n\n")


def tabulate(*args):
    """
    0 - montecarlo_secuencial_meausures
    1 - needle_secuencial_meausures
    2 - montecarlo_secuencial_meausures_insights
    3 - needle_secuencial_meausures_insights
    4 - montecarlo_thread_meausures
    5 - needle_thread_meausures
    6 - montecarlo_thread_meausures_insights
    7 - needle_thread_meausures_insights
    8 - montecarlo_secuencial_compilation_optimized_meausures
    9 - needle_secuencial_compilation_optimized_measures
    10 - montecarlo_secuencial_compilation_optimized_meausures_insights
    11 - needle_secuencial_compilation_optimized_measures_insights
    12 - montecarlo_thread_compilation_optimized_meausures
    13 - needle_thread_compilation_optimized_measures
    14 - montecarlo_thread_compilation_optimized_meausures_insights
    15 - needle_thread_compilation_optimized_measures_insights
    """
    print("\n\n")
    print("MONTECARLO SECUENCIAL")
    data.tabulateSecuencialDataPi_approximation(
        args[0], args[2], plotTitle="Secuencial execution of Montecarlo's algorithm")
    print("\n\n")
    print("MONTECARLO THREAD")
    data.tabulateSecuencialDataPi_approximation(
        args[4], args[6], plotTitle="Parallel execution of Montecarlo's algorithm")
    print("\n\n")
    print("NEEDLE SECUENCIAL")
    data.tabulateSecuencialDataPi_approximation(
        args[1], args[3], plotTitle="Secuencial execution of Buffon needle's problem")
    print("\n\n")
    print("NEEDLE THREAD")
    data.tabulateSecuencialDataPi_approximation(
        args[5], args[7], plotTitle="Parallel execution of Buffon needle's problem")
    print("\n\n")
    print("MOTNECARLO SECUENCIAL - COMPILATION OPTIMIZED")
    data.tabulateSecuencialDataPi_approximation(
        args[8], args[10], plotTitle="Secuencial execution of Montecarlo's algorithm with a compilation-based optimization")
    print("\n\n")
    print("MONTECARLO THREAD - COMPILATION OPTIMIZED")
    data.tabulateSecuencialDataPi_approximation(
        args[12], args[14], plotTitle="Parallel execution of Montecarlo's algorithm with a compilation-based optimization")
    print("\n\n")
    print("NEEDLE SECUENCIAL - COMPILATION OPTIMIZED")
    data.tabulateSecuencialDataPi_approximation(
        args[9], args[11], plotTitle="Secuencial execution of Buffon needle's problem with a compilation-based optimization")
    print("\n\n")
    print("NEEDLE THREAD - COMPILATION OPTIMIZED")
    data.tabulateSecuencialDataPi_approximation(
        args[13], args[15], plotTitle="Parallel execution of Buffon needle's problem with a compilation-based optimization")
    print("\n\n")


def plotMultipleGraphs(*args):
    """
    0 - montecarlo_secuencial_meausures_insights - DB_SEC
    1 - needle_secuencial_meausures_insights - ND_SEC
    2 - montecarlo_thread_meausures_insights - DB_THR
    3 - needle_thread_meausures_insights - ND_THR
    4 - montecarlo_secuencial_compilation_optimized_meausures_insights - DB_SEC_COMP_OPT
    5 - needle_secuencial_compilation_optimized_measures_insights - ND_SEC_COMP_OPT
    6 - montecarlo_thread_compilation_optimized_meausures_insights - DB_THR_COMP_OPT
    7 - needle_thread_compilation_optimized_measures_insights - ND_THR_COMP_OPT


    ** NEED TO DEFINE THIS FOR FUTURE UPDATES

    options: Obj
        - "type": one plot with measure (1) or with multiple measures (2). Multiple measures (2) will run all the data given graphsSet.
        - "measureIndex": Decide what to plot according to indexes from above. Can be null if "type" == 2, else return Error.
    options: {
        "type": 1,
        "measureIndex": <0-15>, 
        "graphsSet":{
            <plot title>: <data to add in one plot>
        }
    }

    example for one plot:

        * For one plot with
        * For one plot


    """
    # MULTIPLE PLOTS - ONE MEASURE ON EACH ONE
    # plot.makePlotPi_approximation(data={
    #     "Secuencial execution of Montecarlo's dartoboard algorithm": args[0]
    # })
    # plot.makePlotPi_approximation(data={
    #     "Secuencial execution of Buffon needle's problem": args[1]
    # })
    # plot.makePlotPi_approximation(data={
    #     "Parallel execution of Montecarlo's dartoboard algorithm": args[2]
    # })
    # plot.makePlotPi_approximation(data={
    #     "Parallel execution of Buffon needle's problem": args[3]
    # })
    # plot.makePlotPi_approximation(data={
    #     "Secuencial execution of Montecarlo's dartboard algorithm with a compilation-based optimization": args[4]
    # })
    # plot.makePlotPi_approximation(data={
    #     "Secuencial execution of Buffon needle's problem with a compilation-based optimization": args[5]
    # })
    # plot.makePlotPi_approximation(data={
    #     "Secuencial execution of Montecarlo's dartboard algorithm with a compilation-based optimization": args[6]
    # })
    # plot.makePlotPi_approximation(data={
    #     "Parallel execution of Buffon needle's problem with a compilation-based optimization": args[7]
    # })

    # MULTIPLES PLOTS - MULTIPLES MEASURES ON EACH ONE
    plot.makePlotPi_approximation(data={
        "Execution comparison of Montecarlo's dartboard algorithm (secuencial, parallel, compilation-based optimization)": [[args[0], "DB_SEC"], [args[2], "DB_THR"], [args[4], "DB_SEC_COMP_OPT"], [args[6], "DB_THR_COMP_OPT"]],
        "Execution comparison of Buffon needle's problem (secuencial, parallel, compilation-based optimization)": [[args[1], "ND_SEC"], [args[3], "ND_THR"], [args[5], "ND_SEC_COMP_OPT"], [args[7], "ND_THR_COMP_OPT"]]
    })


if __name__ == "__main__":
    montecarlo_secuencial_meausures = None
    montecarlo_thread_meausures = None
    montecarlo_secuencial_compilation_optimized_meausures = None
    montecarlo_thread_compilation_optimized_meausures = None

    needle_secuencial_meausures = None
    needle_thread_meausures = None
    needle_secuencial_compilation_optimized_measures = None
    needle_thread_compilation_optimized_measures = None

    # Parsing logs
    # Secuencial
    montecarlo_secuencial_meausures = data.readFileSecuencial(
        "logs/pi_approx/montecarlo_measures_secuencial.log")
    montecarlo_secuencial_meausures_insights = data.dataInsigthsSecuencialPi_approximation(
        montecarlo_secuencial_meausures)

    needle_secuencial_meausures = data.readFileSecuencial(
        "logs/pi_approx/needle_measures_secuencial.log")
    needle_secuencial_meausures_insights = data.dataInsigthsSecuencialPi_approximation(
        needle_secuencial_meausures)

    # Threads
    montecarlo_thread_meausures = data.readFileSecuencial(
        "logs/pi_approx/montecarlo_measures_parallel.log")
    montecarlo_thread_meausures_insights = data.dataInsigthsSecuencialPi_approximation(
        montecarlo_thread_meausures, secuencialReferent=montecarlo_secuencial_meausures_insights)
    needle_thread_meausures = data.readFileSecuencial(
        "logs/pi_approx/needle_measures_parallel.log")
    needle_thread_meausures_insights = data.dataInsigthsSecuencialPi_approximation(
        needle_thread_meausures, secuencialReferent=needle_secuencial_meausures_insights)

    # OPTIMIZED BY COMPILATION
    # Secuencial
    montecarlo_secuencial_compilation_optimized_meausures = data.readFileSecuencial(
        "logs/pi_approx/montecarlo_measures_secuencial_compilation_optimized.log")
    montecarlo_secuencial_compilation_optimized_meausures_insights = data.dataInsigthsSecuencialPi_approximation(
        montecarlo_secuencial_compilation_optimized_meausures)

    needle_secuencial_compilation_optimized_measures = data.readFileSecuencial(
        "logs/pi_approx/needle_measures_secuencial_compilation_optimized.log")
    needle_secuencial_compilation_optimized_measures_insights = data.dataInsigthsSecuencialPi_approximation(
        needle_secuencial_compilation_optimized_measures)

    # Threads
    montecarlo_thread_compilation_optimized_meausures = data.readFileSecuencial(
        "logs/pi_approx/montecarlo_measures_parallel_compilation_optimized.log")
    montecarlo_thread_compilation_optimized_meausures_insights = data.dataInsigthsSecuencialPi_approximation(
        montecarlo_thread_compilation_optimized_meausures, secuencialReferent=montecarlo_secuencial_compilation_optimized_meausures_insights)

    needle_thread_compilation_optimized_measures = data.readFileSecuencial(
        "logs/pi_approx/needle_measures_parallel_compilation_optimized.log")
    needle_thread_compilation_optimized_measures_insights = data.dataInsigthsSecuencialPi_approximation(
        needle_thread_compilation_optimized_measures, secuencialReferent=needle_secuencial_compilation_optimized_measures_insights)

    # print_information(montecarlo_secuencial_meausures,
    #                   needle_secuencial_meausures,
    #                   montecarlo_secuencial_meausures_insights,
    #                   needle_secuencial_meausures_insights,
    #                   montecarlo_thread_meausures,
    #                   needle_thread_meausures,
    #                   montecarlo_thread_meausures_insights,
    #                   needle_thread_meausures_insights,
    #                   montecarlo_secuencial_compilation_optimized_meausures,
    #                   needle_secuencial_compilation_optimized_measures,
    #                   montecarlo_secuencial_compilation_optimized_meausures_insights,
    #                   needle_secuencial_compilation_optimized_measures_insights,
    #                   montecarlo_thread_compilation_optimized_meausures,
    #                   needle_thread_compilation_optimized_measures,
    #                   montecarlo_thread_compilation_optimized_meausures_insights,
    #                   needle_thread_compilation_optimized_measures_insights)

    # tabulate(montecarlo_secuencial_meausures,
    #          needle_secuencial_meausures,
    #          montecarlo_secuencial_meausures_insights,
    #          needle_secuencial_meausures_insights,
    #          montecarlo_thread_meausures,
    #          needle_thread_meausures,
    #          montecarlo_thread_meausures_insights,
    #          needle_thread_meausures_insights,
    #          montecarlo_secuencial_compilation_optimized_meausures,
    #          needle_secuencial_compilation_optimized_measures,
    #          montecarlo_secuencial_compilation_optimized_meausures_insights,
    #          needle_secuencial_compilation_optimized_measures_insights,
    #          montecarlo_thread_compilation_optimized_meausures,
    #          needle_thread_compilation_optimized_measures,
    #          montecarlo_thread_compilation_optimized_meausures_insights,
    #          needle_thread_compilation_optimized_measures_insights)

    # # Graphication
    plotMultipleGraphs(montecarlo_secuencial_meausures_insights,
                       needle_secuencial_meausures_insights,
                       montecarlo_thread_meausures_insights,
                       needle_thread_meausures_insights,
                       montecarlo_secuencial_compilation_optimized_meausures_insights,
                       needle_secuencial_compilation_optimized_measures_insights,
                       montecarlo_thread_compilation_optimized_meausures_insights,
                       needle_thread_compilation_optimized_measures_insights)

    # # dartboard
    # plot.makeSecuencialPlotPi_approximation(dataSetToPlot=[montecarlo_secuencial_meausures_insights, montecarlo_secuencial_compilation_optimized_meausures_insights,
    #                                         montecarlo_thread_meausures_insights, montecarlo_thread_compilation_optimized_meausures_insights], setTitle="Dartboard comparison")
    # # needles
    # plot.makeSecuencialPlotPi_approximation(dataSetToPlot=[needle_secuencial_meausures_insights, needle_thread_compilation_optimized_measures_insights,
    #                                         needle_thread_meausures_insights, needle_thread_compilation_optimized_measures_insights], setTitle="Buffon needles problem")
