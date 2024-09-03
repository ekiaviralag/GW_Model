import pandas as pd
import os
import flopy
import numpy as np
# from colorit import *

#Version 3 updated based on V1. It reads the new zones data and also considers GHB scalar factor for the GHB Cells.

print("*****!Reminder: Make sure that the latest version of ""Coarse Fraction"" and ZONE files has been used!!!*****")

print("Reading PVAL Spreadsheet")
PVAL = pd.read_excel("InputForGHB/PVAL.xlsx", sheet_name = "Sheet1")
GHB_Kscalar = dict(zip(PVAL["ZONE"],PVAL["GHB_Kscalar"]))
print("Reading Cell Specific Zone info")
LSZones = pd.read_excel("InputForGHB/KZones_updated_20221123.xlsx", sheet_name = "Formatted")


LSZones["L_R_C"] = LSZones["Lay"].map(str)+"_"+LSZones["Row"].map(str)+"_"+LSZones["Col"].map(str)
LSZones["GHB_Kscalar"] = LSZones["Zones"].map(GHB_Kscalar)
LSZoneMap = dict(zip(LSZones["L_R_C"],LSZones["GHB_Kscalar"]))


print("Reading GHB Info!")

NC_L1 = pd.read_excel("InputForGHB/North_Cells_C2V/GHB_c2v_north_cells_v6.xlsx", sheet_name = 'L1_GHB')
NC_L1.drop(columns = ["NodeID_nearest","Starts_Dry","Goes_Dry","Always_Dry"],inplace = True)
NC_L1["Lay"] = 1
NC_L1["L_R_C"] = NC_L1["Lay"].map(str)+"_"+NC_L1["r_c"].map(str)
NC_L3 = pd.read_excel("InputForGHB\\North_Cells_C2V\\GHB_c2v_north_cells_v6.xlsx", sheet_name = 'L31_GHB')
NC_L3.drop(columns = ["NodeID_Nearest"],inplace = True)
NC_L3.rename(columns = {'L3_thick':'Thickness'}, inplace = True)
NC_L3["Lay"] = 3
NC_L3["L_R_C"] = NC_L3["Lay"].map(str)+"_"+NC_L3["r_c"].map(str)
NC_L4 = pd.read_excel("InputForGHB\\North_Cells_C2V\\GHB_c2v_north_cells_v6.xlsx", sheet_name = 'L32_GHB')
NC_L4.drop(columns = ["NodeID_Nearest"],inplace = True)
NC_L4.rename(columns = {'L3_thick':'Thickness'}, inplace = True)
NC_L4["Lay"] = 4
NC_L4["L_R_C"] = NC_L4["Lay"].map(str)+"_"+NC_L4["r_c"].map(str)
NC_L5 = pd.read_excel("InputForGHB\\North_Cells_C2V\\GHB_c2v_north_cells_v6.xlsx", sheet_name = 'L33_GHB')
NC_L5.drop(columns = ["NodeID_Nearest"],inplace = True)
NC_L5.rename(columns = {'L3_thick':'Thickness'}, inplace = True)
NC_L5["Lay"] = 5
NC_L5["L_R_C"] = NC_L5["Lay"].map(str)+"_"+NC_L5["r_c"].map(str)
NC_L6 = pd.read_excel("InputForGHB\\North_Cells_C2V\\GHB_c2v_north_cells_v6.xlsx", sheet_name = 'L4_GHB')
NC_L6.drop(columns = ["NodeID_Nearest"],inplace = True)
NC_L6["Lay"] = 6
NC_L6["L_R_C"] = NC_L6["Lay"].map(str)+"_"+NC_L6["r_c"].map(str)


SC_L1 = pd.read_excel("InputForGHB\\South_Cells_WW\\GHB_ww_cells_v3.xlsx", sheet_name = 'L1GHB')
SC_L1.drop(columns = ["WW_cellID"],inplace = True)
SC_L1["Lay"] = 1
SC_L1["L_R_C"] = SC_L1["Lay"].map(str)+"_"+SC_L1["r_c"].map(str)
SC_L3 = pd.read_excel("InputForGHB\\South_Cells_WW\\GHB_ww_cells_v3.xlsx", sheet_name = 'L31GHB')
SC_L3.drop(columns = ["WW_cellID"],inplace = True)
SC_L3["Lay"] = 3
SC_L3["L_R_C"] = SC_L3["Lay"].map(str)+"_"+SC_L3["r_c"].map(str)
SC_L4 = pd.read_excel("InputForGHB\\South_Cells_WW\\GHB_ww_cells_v3.xlsx", sheet_name = 'L32GHB')
SC_L4.drop(columns = ["WW_cellID"],inplace = True)
SC_L4["Lay"] = 4
SC_L4["L_R_C"] = SC_L4["Lay"].map(str)+"_"+SC_L4["r_c"].map(str)
SC_L5 = pd.read_excel("InputForGHB\\South_Cells_WW\\GHB_ww_cells_v3.xlsx", sheet_name = 'L33GHB')
SC_L5.drop(columns = ["WW_cellID"],inplace = True)
SC_L5["Lay"] = 5
SC_L5["L_R_C"] = SC_L5["Lay"].map(str)+"_"+SC_L5["r_c"].map(str)
SC_L6 = pd.read_excel("InputForGHB\\South_Cells_WW\\GHB_ww_cells_v3.xlsx", sheet_name = 'L4GHB')
SC_L6.drop(columns = ["WW_cellID"],inplace = True)
SC_L6["Lay"] = 6
SC_L6["L_R_C"] = SC_L6["Lay"].map(str)+"_"+SC_L6["r_c"].map(str)

WC_L1 = pd.read_excel("InputForGHB\\West_Cells_C2V\\GHB_c2v_west_cells_L1L2diffL3_L6.xlsx", sheet_name = 'L1_GHB')
WC_L1.drop(columns = ["NodeID_nearest","Updated_Node"],inplace = True)
WC_L1["Lay"] = 1
WC_L1["L_R_C"] = WC_L1["Lay"].map(str)+"_"+WC_L1["r_c"].map(str)
WC_L2 = pd.read_excel("InputForGHB\\West_Cells_C2V\\GHB_c2v_west_cells_L1L2diffL3_L6.xlsx", sheet_name = 'L2_GHB')
WC_L2.drop(columns = ["NodeID_nearest","Updated_Node","NodeID_nearest","Starts_Dry","Goes_Dry","Always_Dry"],inplace = True)
WC_L2.rename(columns = {'L2_thick':'Thickness'}, inplace = True)
WC_L2["Lay"] = 2
WC_L2["L_R_C"] = WC_L2["Lay"].map(str)+"_"+WC_L2["r_c"].map(str)
WC_L3 = pd.read_excel("InputForGHB\\West_Cells_C2V\\GHB_c2v_west_cells_L1L2diffL3_L6.xlsx", sheet_name = 'L31_GHB')
WC_L3.drop(columns = ["NodeID_Nearest","Updated_Node"],inplace = True)
WC_L3.rename(columns = {'L3_thick':'Thickness'}, inplace = True)
WC_L3["Lay"] = 3
WC_L3["L_R_C"] = WC_L3["Lay"].map(str)+"_"+WC_L3["r_c"].map(str)
WC_L4 = pd.read_excel("InputForGHB\\West_Cells_C2V\\GHB_c2v_west_cells_L1L2diffL3_L6.xlsx", sheet_name = 'L32_GHB')
WC_L4.drop(columns = ["NodeID_Nearest","Updated_Node"],inplace = True)
WC_L4.rename(columns = {'L3_thick':'Thickness'}, inplace = True)
WC_L4["Lay"] = 4
WC_L4["L_R_C"] = WC_L4["Lay"].map(str)+"_"+WC_L4["r_c"].map(str)
WC_L5 = pd.read_excel("InputForGHB\\West_Cells_C2V\\GHB_c2v_west_cells_L1L2diffL3_L6.xlsx", sheet_name = 'L33_GHB')
WC_L5.drop(columns = ["NodeID_Nearest","Updated_Node"],inplace = True)
WC_L5.rename(columns = {'L3_thick':'Thickness'}, inplace = True)
WC_L5["Lay"] = 5
WC_L5["L_R_C"] = WC_L5["Lay"].map(str)+"_"+WC_L5["r_c"].map(str)
WC_L6 = pd.read_excel("InputForGHB\\West_Cells_C2V\\GHB_c2v_west_cells_L1L2diffL3_L6.xlsx", sheet_name = 'L4_GHB')
WC_L6.drop(columns = ["NodeID_Nearest","Updated_Node"],inplace = True)
WC_L6["Lay"] = 6
WC_L6["L_R_C"] = WC_L6["Lay"].map(str)+"_"+WC_L6["r_c"].map(str)

ConcatDF = pd.concat([NC_L1,NC_L3,NC_L4,NC_L5,NC_L6,SC_L1,SC_L3,SC_L4,SC_L5,SC_L6,WC_L1,WC_L2,WC_L3,WC_L4,WC_L5,WC_L6])
# ConcatDF.to_csv("ConcatDF.csv", index = False)

os.chdir("../../../Model/Model/Run460")

path2 = os.getcwd()
# two_up =  os.path.abspath(path.join(__file__ ,"../.."))
model = flopy.mf6.MFSimulation.load(sim_name = "mfsim.nam", load_only=["dis","ghb"])
# model = flopy.mf6.MFSimulation.load()
model_names = model.model_names
gwf = model.get_model('mf6model')
dis = gwf.dis
top = dis.top
bottom = dis.botm.get_data()
ibound = dis.idomain.get_data()

print("Done Laoding MODFLOW")
BottomElev = []
for layer in range(1,7):
    for row in range(1,221):
        for col in range(1,173):
            BottomElev.append([layer,row,col,bottom[layer-1][row-1][col-1]+0.01])
BotmDF = pd.DataFrame(BottomElev, columns = ["Lay","Row","Col","BotmElev"])          
BotmDF["L_R_C"] = BotmDF["Lay"].map(str)+"_"+BotmDF["Row"].map(str)+"_"+BotmDF["Col"].map(str)
# BotmDF.to_csv("BottomDF.csv", index = False)
BotmElevMap = dict(zip(BotmDF["L_R_C"],BotmDF["BotmElev"]))

print("Done with Bottom Layers")
CellThickness = []
for layer in range(1,7):
    for row in range(1,221):
        for col in range(1,173):
            if layer == 1:
                CellThickness.append([layer,row,col,top[row-1][col-1]-bottom[layer-1][row-1][col-1]])
            else:
                CellThickness.append([layer,row,col,bottom[layer-2][row-1][col-1]-bottom[layer-1][row-1][col-1]])
ThicknessDataFrame = pd.DataFrame(CellThickness, columns = ["Lay","Row","Col","Thickness"])
ThicknessDataFrame["L_R_C"] = ThicknessDataFrame["Lay"].map(str)+"_"+ThicknessDataFrame["Row"].map(str) + "_" + ThicknessDataFrame["Col"].map(str)
# ThicknessDataFrame.to_csv("ThicknessDF.csv", index = False)
ThicknessMap = dict(zip(ThicknessDataFrame["L_R_C"],ThicknessDataFrame["Thickness"]))


print("Done With Thickness")
IBOUNDLIST = []
for layer in range(1,7):
    for row in range(1,221):
        for col in range(1,173):
            IBOUNDLIST.append([layer,row,col,ibound[layer-1][row-1][col-1]])
iboundDF = pd.DataFrame(IBOUNDLIST, columns = ["Lay","Row","Col","IBOUND"])          
iboundDF["L_R_C"] = iboundDF["Lay"].map(str)+"_"+iboundDF["Row"].map(str)+"_"+iboundDF["Col"].map(str)
# iboundDF.to_csv("iboundDF.csv", index = False)
iboundMap = dict(zip(iboundDF["L_R_C"],iboundDF["IBOUND"]))

print("Done With IBound")




# os.chdir("Z:\Arvin Edison SGMA\EKI Work Products\GW Model and DST\Model\Calibration\Workflow\GHB")    
TempList = []
for layer in range(1,7):
    Kh = np.loadtxt("ModelArrays/NPF_TXTFiles/Kh.npf_layer%d.txt"%layer, delimiter = " ")
    for row in range(1,221):
        for col in range(1,173):
            TempList.append([layer,row,col,Kh[row-1][col-1]])
KhDataFrame = pd.DataFrame(TempList, columns = ["Lay","Row","Col","Kh"])
KhDataFrame["L_R_C"] = KhDataFrame["Lay"].map(str)+"_"+KhDataFrame["Row"].map(str) + "_" + KhDataFrame["Col"].map(str)
KhMap = dict(zip(KhDataFrame["L_R_C"],KhDataFrame["Kh"]))

ConcatDF["Kh"] = ConcatDF["L_R_C"].map(KhMap)
ConcatDF["BotmElev"] = ConcatDF["L_R_C"].map(BotmElevMap)
ConcatDF["Thickness_update"] = ConcatDF["L_R_C"].map(ThicknessMap)
ConcatDF["IBOUND"] = ConcatDF["L_R_C"].map(iboundMap)
# ConcatDF = ConcatDF[ConcatDF["Kh"] != -999]
ConcatDF = ConcatDF[ConcatDF["IBOUND"] == 1]
CellNames = ConcatDF["L_R_C"].values
# ConcatDF["Conductance"] = ConcatDF["Kh"] *(ConcatDF["Thickness"]*ConcatDF["Width"]/ConcatDF["Distance"])
ConcatDF["GHB_Kscalar"] = ConcatDF["L_R_C"].map(LSZoneMap)
ConcatDF["Conductance"] = ConcatDF["GHB_Kscalar"] * ConcatDF["Kh"] *(ConcatDF["Thickness_update"]*ConcatDF["Width"]/ConcatDF["Distance"])
# ConcatDF.to_csv("QAQC_v5.csv")

print("Writing GHB package!")
os.chdir("../../../Model Update WY2023/Inputs_Scripts/GHB")
path3 = os.getcwd()

file1 = open("AEGFM_WY23update.ghb", 'w')
file1.write('#MODFLOW6 General Head Boundary Package \n')
file1.write('BEGIN OPTIONS\n')
file1.write('  PRINT_INPUT\n')
file1.write('  SAVE_FLOWS\n')
file1.write('END OPTIONS\n')
file1.write('\n')
file1.write('BEGIN DIMENSIONS\n')
file1.write('  MAXBOUND 2375\n')
file1.write('END DIMENSIONS\n\n\n')
file1.close

for SP in range(1,349):
    print(SP)
    file1 = open("AEGFM_WY23update.ghb", 'a')
    file1.write("BEGIN PERIOD %d\n"%SP)
    for names in CellNames:
        TempDF= ConcatDF[ConcatDF["L_R_C"] ==names]
        TempData = TempDF[["Lay","row","column","Head_SP%d"%SP,"BotmElev","Conductance"]]
        
        HeadCheck = TempData["Head_SP%d"%SP].values[0]
        BotmCheck = TempData["BotmElev"].values[0]
        if HeadCheck > BotmCheck:
            TempData = TempDF[["Lay","row","column","Head_SP%d"%SP,"Conductance"]]
        else:
            TempData = TempDF[["Lay","row","column","BotmElev","Conductance"]]
        np.savetxt(file1,TempData,fmt ='%d\t\t%d\t\t%d\t\t%f\t\t%f\t\t')
    file1.write('\n')
    file1.write("END PERIOD\n")
    file1.write('\n')
    file1.close() 

print("GHB package updated using NFP package values!")

