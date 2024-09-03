rm(list = ls())
setwd('Z:/Arvin Edison SGMA/EKI Work Products/GW Model and DST/Model Update WY2023/Inputs_Scripts/GHB/Southern (WW)')

## Initial condition
WWL1_IC <- read.csv('WW_output/L1/Head199409.csv')
WWL2_IC <- read.csv('WW_output/L2/Head199409.csv')
WWL3_IC <- read.csv('WW_output/L3/Head199409.csv')

df <- read.csv('GHB_AE_wW_mapping.csv')
df <- df[, c('CellID', 'row', 'column', 'active_V2', 'Cell')]

df$Head_L1_199409 <- 0
df$Head_L2_199409 <- 0
df$Head_L3_199409 <- 0
for(iidx in 1:dim(df)[1]){
  idx_L1 <- which(WWL1_IC$Cell == df$Cell[iidx])
  idx_L2 <- which(WWL2_IC$Cell == df$Cell[iidx])
  idx_L3 <- which(WWL3_IC$Cell == df$Cell[iidx])
  df$Head_L1_199409[iidx] <- WWL1_IC$Head199409[idx_L1]
  df$Head_L2_199409[iidx] <- WWL2_IC$Head199409[idx_L2]
  df$Head_L3_199409[iidx] <- WWL3_IC$Head199409[idx_L3]
  print(iidx)
}

write.csv(df, file = 'AE_WW_InitialHead.csv')

## AE outermost grids
ndf <- read.csv('GHB_AE_WW_outermost.csv')

df <- df[which(df$CellID %in% ndf$CellID),]

GHB_df_L1 <- df[, c('CellID', 'row', 'column', 'active_V2', 'Cell')]
GHB_df_L2 <- df[, c('CellID', 'row', 'column', 'active_V2', 'Cell')]
GHB_df_L3 <- df[, c('CellID', 'row', 'column', 'active_V2', 'Cell')]
GHB_colname <- list.files('WW_output/L1')[109:456] # 1999-10 to 2023-09
for(jjdx in 1:length(GHB_colname)){
  add_col_name <- substr(GHB_colname[jjdx], 1, 10)
  GHB_df_L1[, add_col_name] = 0
  GHB_df_L2[, add_col_name] = 0
  WW_L1 <- read.csv(paste('WW_output/L1/', GHB_colname[jjdx], sep = ''))
  WW_L2 <- read.csv(paste('WW_output/L2/', GHB_colname[jjdx], sep = ''))
  WW_L3 <- read.csv(paste('WW_output/L3/', GHB_colname[jjdx], sep = ''))
  
  for(kkdx in 1:dim(df)[1]){
    idx_L1 <- which(WW_L1$Cell == GHB_df_L1$Cell[kkdx])
    GHB_df_L1[kkdx, add_col_name] = WW_L1[idx_L1, add_col_name]
  }
  
  for(kkdx in 1:dim(df)[1]){
    idx_L2 <- which(WW_L2$Cell == GHB_df_L2$Cell[kkdx])
    GHB_df_L2[kkdx, add_col_name] = WW_L2[idx_L2, add_col_name]
  }  
  
  for(kkdx in 1:dim(df)[1]){
    idx_L3 <- which(WW_L3$Cell == GHB_df_L3$Cell[kkdx])
    GHB_df_L3[kkdx, add_col_name] = WW_L3[idx_L3, add_col_name]
  }  
  
  print(jjdx)
}

# 
write.csv(GHB_df_L1, file = 'ArvinGHB/GHB_AE_WW_L1.csv')
write.csv(GHB_df_L2, file = 'ArvinGHB/GHB_AE_WW_L2.csv')
write.csv(GHB_df_L3, file = 'ArvinGHB/GHB_AE_WW_L3.csv')
