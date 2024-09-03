##updated for retreiving data thru 2023
## Process output data to increase efficiency
rm(list = ls())
library(ggplot2)
library(plotly)
library(rgl)
library(akima)
library(sf)
library(raster)
library(mapplots)
library(htmlwidgets)
# ## MAPBOX TOKEN
# Sys.setenv('MAPBOX_TOKEN' = 'pk.eyJ1IjoibmlnZWxraW5uZXkxOTkzIiwiYSI6ImNrcjZwMmFtbzFrZWsyb3BkcWtkdWxwN3AifQ.2uoOmGYL6fIpM2K7wuUsyg')
setwd('Z:/Arvin Edison SGMA/EKI Work Products/GW Model and DST/Model Update WY2023/Inputs_Scripts/GHB/Southern (WW)')
head <- scan('wwgfm_hist_2023.hds')
len <- length(head)
df <- read.csv('XYZ_coord.csv')
head(df)
numofgrids = dim(df)[1]
numoflayers = 4
numofSP = len/numofgrids/numoflayers
First_SP = as.Date('1985-10-01')
Last_SP = as.Date('2023-09-30')
Date_seq <- seq(First_SP, Last_SP, by = 'month')
Colname <- paste('Head', format(Date_seq, '%Y%m'), sep = '')

Lay1 <- df[, c('IB1', 'row', 'column', 'Cell', 'X_coord', 'Y_coord', 'LSE', 'L1_Bot', 'L2_Bot', 'L3_Bot', 'L4_Bot')]
Lay2 <- df[, c('IB2', 'row', 'column', 'Cell', 'X_coord', 'Y_coord', 'LSE', 'L1_Bot', 'L2_Bot', 'L3_Bot', 'L4_Bot')]
Lay3 <- df[, c('IB3', 'row', 'column', 'Cell', 'X_coord', 'Y_coord', 'LSE', 'L1_Bot', 'L2_Bot', 'L3_Bot', 'L4_Bot')]
Lay4 <- df[, c('IB4', 'row', 'column', 'Cell', 'X_coord', 'Y_coord', 'LSE', 'L1_Bot', 'L2_Bot', 'L3_Bot', 'L4_Bot')]
for(idx in 1:length(Colname)){
  Lay1[, idx + 11] <- head[(1 + dim(df)[1] * (4 * (idx - 1) + 0)) : (dim(df)[1] * (4 * (idx - 1) + 1))]
  Lay2[, idx + 11] <- head[(1 + dim(df)[1] * (4 * (idx - 1) + 1)) : (dim(df)[1] * (4 * (idx - 1) + 2))]
  Lay3[, idx + 11] <- head[(1 + dim(df)[1] * (4 * (idx - 1) + 2)) : (dim(df)[1] * (4 * (idx - 1) + 3))]
  Lay4[, idx + 11] <- head[(1 + dim(df)[1] * (4 * (idx - 1) + 3)) : (dim(df)[1] * (4 * (idx - 1) + 4))]
  print(Colname[idx])
}
names(Lay1)[12:dim(Lay1)[2]] <- names(Lay2)[12:dim(Lay2)[2]] <-
  names(Lay3)[12:dim(Lay3)[2]] <- names(Lay4)[12:dim(Lay4)[2]] <- Colname
## Some hydrograph
par(mfrow = c(2, 2))
plot(Date_seq, Lay1[11000, 12:dim(Lay1)[2]], type = 'l', xlab = 'Date', ylab = 'Head', main = 'Basin')
plot(Date_seq, Lay1[17078, 12:dim(Lay1)[2]], type = 'l', xlab = 'Date', ylab = 'Head', main = 'Intermediate')
## Some hydrograph
par(mfrow = c(2, 2))
plot(Date_seq, Lay1[11000, 12:dim(Lay1)[2]], type = 'l', xlab = 'Date', ylab = 'Head', main = 'Basin')
plot(Date_seq, Lay1[17078, 12:dim(Lay1)[2]], type = 'l', xlab = 'Date', ylab = 'Head', main = 'Intermediate')
plot(Date_seq, Lay1[18378, 12:dim(Lay1)[2]], type = 'l', xlab = 'Date', ylab = 'Head', main = 'High')
plot(Date_seq, Lay1[11000, 12:dim(Lay1)[2]], type = 'l', xlab = 'Date', ylab = 'Head', main = 'Together', ylim = c(170, 2250))
lines(Date_seq, Lay1[17078, 12:dim(Lay1)[2]], col = 2)
lines(Date_seq, Lay1[18378, 12:dim(Lay1)[2]], col = 4)
for(idx in 1:length(Colname)){
  t <- Colname[idx]
  save_df_L1 <- Lay1[, c('IB1', 'row', 'column', 'Cell', 'X_coord', 'Y_coord', 'LSE', 'L1_Bot', 'L2_Bot', 'L3_Bot', 'L4_Bot', t)]
  write.csv(save_df_L1, file = paste('WW_output/L1/', t, '.csv', sep = ''), row.names = FALSE)
  save_df_L2 <- Lay2[, c('IB2', 'row', 'column', 'Cell', 'X_coord', 'Y_coord', 'LSE', 'L1_Bot', 'L2_Bot', 'L3_Bot', 'L4_Bot', t)]
  write.csv(save_df_L2, file = paste('WW_output/L2/', t, '.csv', sep = ''), row.names = FALSE)
  save_df_L3 <- Lay3[, c('IB3', 'row', 'column', 'Cell', 'X_coord', 'Y_coord', 'LSE', 'L1_Bot', 'L2_Bot', 'L3_Bot', 'L4_Bot', t)]
  write.csv(save_df_L3, file = paste('WW_output/L3/', t, '.csv', sep = ''), row.names = FALSE)
  save_df_L4 <- Lay4[, c('IB4', 'row', 'column', 'Cell', 'X_coord', 'Y_coord', 'LSE', 'L1_Bot', 'L2_Bot', 'L3_Bot', 'L4_Bot', t)]
  write.csv(save_df_L4, file = paste('WW_output/L4/', t, '.csv', sep = ''), row.names = FALSE)
  print(t)
}

