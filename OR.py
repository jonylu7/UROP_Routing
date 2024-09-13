import elkai
import numpy as np
import json
def saveAsJSON():
    return

def prunCostMatrix(costMatrix,orders):
    prunnedCostMatrix=[]
    for index,orderx in enumerate(orders):
        row=[]
        for ordery in orders:
            row.append(costMatrix[orderx-1][ordery-1])
        prunnedCostMatrix.append(row)
    return np.array(prunnedCostMatrix)




def solvePrunnedCostMatrix(costMatrix,orders):
    tempSol=elkai.DistanceMatrix(costMatrix.tolist()).solve_tsp()
    sol=[]
    for t in tempSol:
        sol.append(orders[t])

    return sol


def solveTSP(costMatrix,orders):
    prunnedCostMatrix=prunCostMatrix(costMatrix,orders)
    costMatrixSol=solvePrunnedCostMatrix(prunnedCostMatrix,orders)

    totalCost=0
    for i in range(len(costMatrixSol)-1):
        totalCost+=costMatrix[costMatrixSol[i],costMatrixSol[i+1]]
    return costMatrixSol,totalCost


def generateSolutionPath(pathMatrix,costMatrixSol):
    solutionPath=[0]
    for i in range(len(costMatrixSol)-1):
        solutionPath+=pathMatrix[costMatrixSol[i]][costMatrixSol[i+1]]
    return solutionPath






